"""
Node definition for Worlds
"""

import Cursors

import pygame
from pygame.locals import *
import WorldApp

# A global dict of node names to nodes.
allNodes = {}

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

class Node:
    """
    Abstract class that defines the interface to all Nodes
    """

    name = None
    
    def __init__(self, name):
        allNodes[name] = self
        self.name = name

    def __repr__(self):
        return "<Node %s (%s)>" % (self.name, self.__class__.__name__)
    
    def getImage(self):
        "Return a Surface or filename to display for this node"
        pass

    def onEnter(self):
        "Called when the node is entered"
        pass

    def onLeave(self):
        "Called when the node is left"
        pass

    def onEvent(self, event):
        """
        Called to process events.
        Can return:
           Node -      next node.
           string -    name of next node.
        """
        pass

class ErrorNode(Node):
    def __init__(self, name):
        Node.__init__(self, name)

    def getImage(self):
        import pygame, pygame.font
        font = pygame.font.Font(None, 100)
        text = font.render("  (" + self.name + ")  ", 1, (255, 0, 0), (255, 255, 0))
        return text

# Built-in implementation that does nothing.
class NullNode(ErrorNode):
    def __init__(self):
        ErrorNode.__init__(self, "null")
        
# Node that has hotspots for clicking to go to other nodes.
class StdNode(Node):

    def __init__(self, name, imgName):
        Node.__init__(self, name)
        self.imgName = imgName

    imgName = None

    def getImage(self):
        img = pygame.image.load(self.imgName).convert()

        vx, vy = WorldApp.WorldApp().getScreenSize()
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

    def getHotspots(self):
        """
        Return list of (rect, cursor, thing), where thing can be:
          Node -      next node
          string -    name of next node
          method -    call it on this node
        """
        pass

    hotspots = None

    def onEnter(self):
        self.hotspots = self.getHotspots()

    def onLeave(self):
        self.hotspots = None

    def findExit(self, opts):
        "Search for an attribute in the list of opts"
        for a in opts:
            if hasattr(self, a):
                return getattr(self, a)
        return None
    
    def onEvent(self, event):
        "Handle events against the hotspots"

        ret = None
        
        if event.type == MOUSEMOTION:
            theCursor = pygame.cursors.arrow
            for rect, cursor, thing in self.hotspots:
                if rect.collidepoint(event.pos):
                    theCursor = cursor
            pygame.mouse.set_cursor(*theCursor)
        elif event.type == MOUSEBUTTONDOWN:
            for rect, cursor, thing in self.hotspots:
                if rect.collidepoint(event.pos):
                    ret = thing
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                ret = self.findExit(("l", "b"))
            elif event.key == K_RIGHT:
                ret = self.findExit(("r", "b"))
            elif event.key == K_UP or event.key == K_SPACE:
                ret = self.findExit(("f_chosen", "f"))
            elif event.key == K_DOWN:
                ret = self.findExit(("b"))
            else:
                if event.mod & KMOD_CTRL:
                    ret = findJumpNode(event.key)
        return ret

turn = 0.15

class lr(StdNode):
    def __init__(self, name, img, l, r):
        StdNode.__init__(self, name, img)
        self.l = l
        self.r = r
        
    def getHotspots(self):
        wd, ht = WorldApp.WorldApp().getScreenSize()
        return [
            (Rect(0, 0, turn*wd, ht), Cursors.left, self.l),
            (Rect(wd*(1-turn), 0, turn*wd, ht), Cursors.right, self.r)
            ]

class lfr(StdNode):
    def __init__(self, name, img, l, f, r):
        StdNode.__init__(self, name, img)
        self.l = l
        self.f = f
        self.r = r
        
    def getHotspots(self):
        f = self.f
        # f can be a sequence, meaning choose one at random.
        if type(f) == type(()) or type(f) == type([]):
            from random import choice
            f = choice(f)
            self.f_chosen = f

        wd, ht = WorldApp.WorldApp().getScreenSize()        
        return [
            (Rect(0, 0, turn*wd, ht), Cursors.left, self.l),
            (Rect(wd*turn, 0, wd*(1-2*turn), ht), Cursors.forward, f),
            (Rect(wd*(1-turn), 0, wd*turn, ht), Cursors.right, self.r)
            ]

class bf(StdNode):
    def __init__(self, name, img, b, f):
        StdNode.__init__(self, name, img)
        self.b = b
        self.f = f
        
    def getHotspots(self):
        wd, ht = WorldApp.WorldApp().getScreenSize()        
        return [
            (Rect(0, 0, wd*turn, ht), Cursors.left180, self.b),
            (Rect(wd*turn, 0, wd*(1-2*turn), ht), Cursors.forward, self.f),
            (Rect(wd*(1-turn), 0, wd*turn, ht), Cursors.right180, self.b)
            ]
