"""
Node definition for Worlds
"""

import pygame
import pygame.font
import pygame.image
from pygame.locals import *
import sys
import WorldApp
import Transition

# A global dict of node names to nodes.
allNodes = {}

def isNode(n):
    if type(n) == type(""):
        return allNodes.has_key(n)
    else:
        return isinstance(n, Node)

def findNode(name):
    try:
        return allNodes[name]
    except KeyError:
        print "Couldn't find node %s" % (name)
        return ErrorNode(name)

def findJumpNode(char):
    if type(char) == type(1):
        if 0 < char < 256:
            char = chr(char)
        else:
            return None
    try:
        return allNodes['jump_' + char]
    except KeyError:
        return None

def setJumpNode(char, name):
    allNodes['jump_' + char] = name
    
def countNodes():
    return len(allNodes)

def validateAllNodes():
    for node in allNodes.values():
        if type(node) == type(""):
            if not isNode(node):
                print "String node %s is not a node" % (node)
        else:
            if not hasattr(node, 'onValidate'):
                print "%s has no onValidate() method:" % (node)
                print dir(node)
            else:
                node.onValidate()
        
def dumpAllNodes(fout):
    fout.write("<nodes>\n")
    for node in allNodes.values():
        if type(node) == type(""):
            if not isNode(node):
                print "String node %s is not a node" % (node)
        else:
            if not hasattr(node, 'onDump'):
                print "%s has no onDump() method:" % (node)
                print dir(node)
            else:
                node.onDump(fout)
        fout.write("\n")
    fout.write("</nodes>\n")
        
class Node:
    """
    Abstract class that defines the interface to all Nodes
    """

    name = None
    
    def __init__(self, name):
        allNodes[name] = self
        self.name = name

    def __repr__(self):
        ri = self.getReprInfo()
        if ri != None:
            ri = " [" + ri + "]"
        else:
            ri = ""
        return "<Node %s (%s)%s>" % (self.name, self.__class__.__name__, ri)

    def getReprInfo(self):
        """Overridable to add info to the __repr__ string."""
        pass

    def getName(self):
        return self.name

    def getImage(self, worldapp):
        """Return a Surface to display for this node"""
        pass

    def getBackColor(self, worldapp):
        """Return a color to backfill the view with for this node"""
        return (0,0,0)
    
    def onEnter(self, worldapp):
        """Called when the node is entered"""
        pass

    def onLeave(self, worldapp):
        """Called when the node is left"""
        pass

    def getTransitionClass(self, toNode):
        """
        Called to get a transition when leaving us for toNode.
        Called after onLeave.
        """
        pass
    
    def onEvent(self, event, xpos, worldapp):
        """
        Called to process events.
        Can return:
           Node -      next node.
           string -    name of next node.
        """
        pass

    def onValidate(self):
        """
        Called to check that everything is OK. Print messages
        if something is amiss.
        """
        pass

    def onDump(self, fout):
        """
        Called to dump this node to fout.
        """
        print "Node %s has no onDump impl" % self.name

    def onDumpAttrs(self, fout):
        """
        Called to write attributes of the node to an XML dump.
        """
        fout.write(" name='%s'" % self.name)

class ErrorNode(Node):
    """Display an erroneous node name"""
    def __init__(self, name):
        Node.__init__(self, name)

    def getImage(self, worldapp):
        import pygame.font
        font = pygame.font.Font(None, 100)
        text = font.render("  (" + self.name + ")  ", 1, (255, 0, 0), (255, 255, 0))
        return text

    def onEvent(self, event, xpos, worldapp):
        if event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN:
            return worldapp.getHomeNode()
        

class NullNode(ErrorNode):
    """Built-in implementation that does nothing."""
    def __init__(self):
        ErrorNode.__init__(self, "null")

    def onDump(self, fout):
        fout.write("<null")
        self.onDumpAttrs(fout)
        fout.write(" />")

class ImgNode(Node):
    """Node that dispays an image from a file."""

    def __init__(self, name, imgName):
        Node.__init__(self, name)
        self.imgName = imgName

    def getReprInfo(self):
        return self.imgName

    def getImageSize(self, wa):
        """Return the size the image should be scaled to"""
        return wa.getViewSize()

    def getImage(self, wa):
        try:
            img = pygame.image.load(self.imgName).convert()
        except:
            print "Couldn't load", self.imgName
            print "%s, %s" % (sys.exc_info()[:2])
            font = pygame.font.Font(None, 100)
            img = font.render("  (" + self.imgName + ")  ", 1, (255, 0, 0), (255, 255, 0))

        vx, vy = self.getImageSize(wa)
        ix, iy = img.get_size()
        
        if ix != vx or iy != vy:
            # Scale uniformly to fit the view
            sx = vx * 1.0 / ix
            sy = vy * 1.0 / iy
            if sx <= sy: scale = sx  
            if sy <= sx: scale = sy
            #if (self.debug):
            #    print "Scaling %d, %d to %d, %d: %f" % (ix, iy, vx, vy, scale)
            #img = pygame.transform.rotozoom(img, 0, scale)
            img = pygame.transform.scale(img, (scale*ix, scale*iy))
           
        return img

    def onValidate(self):
        Node.onValidate(self)
        # Check that the image file exists
        import os
        if not os.access(self.imgName, os.R_OK):
            print "Missing image: %s uses %s" % (self.name, self.imgName)

    def onDumpAttrs(self, fout):
        Node.onDumpAttrs(self, fout)
        fout.write(" img='%s'" % self.imgName)

class StdNode(ImgNode):
    """Node that has hotspots for clicking to go to other nodes."""
    
    def __init__(self, name, imgName):
        ImgNode.__init__(self, name, imgName)
        self.actions = []

    def getHotspots(self, wa):
        """
        Return list of (rect, cursor, thing), where thing can be:
          Node -      next node
          string -    name of next node
          method -    call it on this node
        """
        turn = 0.15
        updn = 0.15
        f = self.chooseForward()
        wd, ht = wa.getViewSize()
        ret = []

        if f != None:
            ret += [(Rect(0, 0, wd, ht), 'forward', f)]

        if hasattr(self, 'b'):
            ret += [(Rect(0, ht*(1-updn), wd, ht*updn), 'back', self.b)]
            
        if hasattr(self, 'l'):
            ret += [(Rect(0, 0, turn*wd, ht), 'left', self.l)]
        elif hasattr(self, 'b'):
            ret += [(Rect(0, 0, turn*wd, ht), 'left180', self.b)]

        if hasattr(self, 'r'):            
            ret += [(Rect(wd*(1-turn), 0, wd*turn, ht), 'right', self.r)]
        elif hasattr(self, 'b'):
            ret += [(Rect(wd*(1-turn), 0, wd*turn, ht), 'right180', self.b)]

        if hasattr(self, 'u'):
            ret += [(Rect(0, 0, wd, ht*updn), 'up', self.u)]

        if hasattr(self, 'd'):
            ret += [(Rect(0, ht*(1-updn), wd, ht*updn), 'down', self.d)]

        for a in self.actions:
            ret += [(
                Rect(a[0][0]*wd, a[0][1]*ht, a[0][2]*wd, a[0][3]*ht),
                'hand',
                a[1]
                )]
            
        return ret

    hotspots = None
    actions = None

    def chooseForward(self):
        """f can be a sequence, meaning choose one at random."""
        if not hasattr(self, 'f'):
            return None
        
        f = self.f
        if type(f) == type(()) or type(f) == type([]):
            from random import choice
            f = choice(f)
            self.f_chosen = f
        return f
    
    def onEnter(self, wa):
        self.hotspots = self.getHotspots(wa)

    def onLeave(self, wa):
        self.hotspots = None

    def findExit(self, opts):
        "Search for an attribute in the list of opts"
        for a in opts:
            if hasattr(self, a):
                return getattr(self, a)
        return None
    
    def getTransitionClass(self, toNode):
        """Specify a transition to toNode."""
        def isExit(self, toNode, a):
            if type(a) != type(()):
                a = (a,)
            for a0 in a:
                if hasattr(self, a0):
                    return getattr(self, a0) == toNode
            return 0

        if type(toNode) != type(''):
            toNode = toNode.getName()

        if isExit(self, toNode, 'l'):
            return Transition.SlideRight
        elif isExit(self, toNode, 'r'):
            return Transition.SlideLeft
        elif isExit(self, toNode, 'u'):
            return Transition.SlideDown
        elif isExit(self, toNode, 'd'):
            return Transition.SlideUp
        elif isExit(self, toNode, ('f', 'f_chosen', 'b')):
            return Transition.Dissolve
        
    def onEvent(self, event, xpos, wa):
        "Handle events against the hotspots"

        ret = None

        if event.type == MOUSEMOTION:
            theCursor = 'x'
            for rect, cursor, thing in self.hotspots:
                if rect.collidepoint(xpos):
                    theCursor = cursor
            if type(theCursor) == type(""):
                theCursor = wa.getCursor(theCursor)
            pygame.mouse.set_cursor(*theCursor)
        elif event.type == MOUSEBUTTONDOWN:
            for rect, cursor, thing in self.hotspots:
                if rect.collidepoint(xpos):
                    ret = thing
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                ret = self.findExit(("l", "b", "prevNode"))
            elif event.key == K_RIGHT:
                ret = self.findExit(("r", "b", "prevNode"))
            elif event.key == K_UP or event.key == K_SPACE:
                ret = self.findExit(("f_chosen", "f", "prevNode"))
            elif event.key == K_DOWN:
                ret = self.findExit(("b", "prevNode"))
            else:
                if event.mod & KMOD_CTRL:
                    ret = findJumpNode(event.key)
        return ret

    def onValidate(self):
        ImgNode.onValidate(self)
        # Check that the destinations are nodes
        for a in ['f', 'l', 'r', 'b', 'u', 'd']:
            if hasattr(self, a):
                dest = getattr(self, a)
                if type(dest) == type([]):
                    for d in dest:
                        if not isNode(d):
                            print "Non-existant node reference: %s.%s[] --> %s" % (self.name, a, dest)
                elif not isNode(dest):
                    print "Non-existant node reference: %s.%s --> %s" % (self.name, a, dest)
        # Check that action destinations are nodes
        for a in self.actions:
            if not isNode(a[1]):
                print "Non-existant action node reference: %s --> %s" % (self.name, a[1])

    def onDump(self, fout):
        fout.write("<std")
        self.onDumpAttrs(fout)
        fout.write(" />")

class lr(StdNode):
    def __init__(self, name, img, l, r):
        StdNode.__init__(self, name, img)
        self.l = l
        self.r = r

class lfr(StdNode):
    def __init__(self, name, img, l, f, r):
        StdNode.__init__(self, name, img)
        self.l = l
        self.f = f
        self.r = r

class bf(StdNode):
    def __init__(self, name, img, b, f):
        StdNode.__init__(self, name, img)
        self.b = b
        self.f = f
        
class deadend(StdNode):
    """A simple node that returns to the previous node when clicked."""
    def __init__(self, name, img):
        StdNode.__init__(self, name, img)

    def onEnter(self, wa):
        self.prevNode = wa.getNode()
        StdNode.onEnter(self, wa)

    def getHotspots(self, wa):
        wd, ht = wa.getViewSize()        
        return [
            (Rect(0, 0, wd, ht), wa.getCursor('back'), self.prevNode)
            ]


class PhotoNode(StdNode):
    """For looking at photos"""

    def __init__(self, name, imgname, next, exit):
        StdNode.__init__(self, name, imgname)
        self.f = next
        self.b = exit

    def getImageSize(self, wa):
        wd, ht = wa.getViewSize()
        bd = ht / 30
        return wd - 2*bd, ht - 2*bd

    def getBackColor(self, wa):
        return (255, 255, 255)

    def getHotspots(self, wa):
        wd, ht = wa.getViewSize()
        bd = ht / 15
        return [
            (Rect(0, 0, wd, ht), 'back', self.b),
            (Rect(bd, bd, wd-2*bd, ht-2*bd), 'arrow', self.f)
            ]

    def getTransitionClass(self, toNode):
        return None
