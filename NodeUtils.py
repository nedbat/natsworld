"""
Utilities for nodes in Nat's World
"""

from Node import *
from Menu import *
from Utils import *

def nesw(name, **data):
    """
    Make four nodes for n, e, w, s from a location.
    Keys:
        images: ni, ei, wi, si.
        destinations: n, e, w, s.
    """

    name_ = name + ':'
    ret = []
    left = {'n': 'w', 'e': 'n', 's': 'e', 'w': 's'}
    right = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}
    
    # repair missing positions.
    for d in "nesw":
        if not data.has_key(d + 'i'):
            oldleft = left[d]
            oldright = right[d]
            left[oldright] = oldleft
            right[oldleft] = oldright
            
    # create the nodes                
    for d in "nesw":
        if data.has_key(d + 'i'):
            if data.has_key(d):
                node = lfr(
                        name_ + d,
                        data[d + 'i'],
                        name_ + left[d],
                        data[d],
                        name_ + right[d]
                        )
            else:
                node = lr(
                        name_ + d,
                        data[d + 'i'],
                        name_ + left[d],
                        name_ + right[d]
                        )
                
            ret.append(node)

    return ret


def clump(name, nodelist):
    """
    Make n nodes in a ring, like hub and spoke.  Nodelist is a list of nodes,
    where each entry is either an image, or an image and destination pair.
    """

    name_ = name + ':'
    ret = []
    
    nNodes = len(nodelist)
    for i, node in IndexLoop(nodelist):
        if len(node) >= 2:
            node = lfr(
                    name_ + str(i),
                    node[0],
                    name_ + str((i-1)%nNodes),
                    node[1],
                    name_ + str((i+1)%nNodes)
                    )
        else:
            node = lr(
                    name_ + str(i),
                    node[0],
                    name_ + str((i-1)%nNodes),
                    name_ + str((i+1)%nNodes)
                    )
        ret.append(node)
    return ret


def tableau(name, nodelist, left, right, **more):
    """
    Make n nodes in a line, like hub and spoke.  Nodelist is a list of nodes,
    where each entry is either an image, or an image and destination pair.
    left and right are the nodes to link the ends to.
    """

    name_ = name + ':'
    ret = []
    
    nNodes = len(nodelist)
    for i, node in IndexLoop(nodelist):
        if i == 0:
            l = left
        else:
            l = name_ + str(i-1)

        if i == nNodes-1:
            r = right
        else:
            r = name_ + str(i+1)
            
        if len(node) >= 2:
            node = lfr(name_ + str(i), node[0], l, node[1], r)
        else:
            node = lr(name_ + str(i), node[0], l, r)

        for extra in ('u', 'd', 'b'):
            if more.has_key(extra):
                setattr(node, extra, more[extra])
                
        ret.append(node)
    return ret

def tunnel(name, nodepairs, back, fwd):
    """
    Make a series of bf nodes forming a tunnel
    """

    name_ = name + ':'
    ret = []
    for i, nodepair in IndexLoop(nodepairs):
        if i == 0:
            b = back
        else:
            b = name_ + str(i-1) + 'b'
            
        if i == len(nodepairs)-1:
            f = fwd
        else:
            f = name_ + str(i+1) + 'f'
            
        nodef = bf(
                    name_ + str(i) + 'f',
                    nodepair[0],
                    name_ + str(i) + 'b',
                    f
                    )
        nodeb = bf(
                    name_ + str(i) + 'b',
                    nodepair[1],
                    name_ + str(i) + 'f',
                    b
                    )
        ret += [ nodef, nodeb ]

    return ret

def tunneloneway(name, nodes, back, fwd):
    """
    Make a series of bf nodes forming a one-way tunnel
    """
    name_ = name + ':'
    ret = []
    for i, node in IndexLoop(nodes):
        if i == len(nodes)-1:
            f = fwd
        else:
            f = name_ + str(i+1)

        ret += [
            bf(
                name_ + str(i),
                node,
                back,
                f
            )]

    return ret

def tunnelonewayskip(name, flen, nodes, back, fwd):
    """
    Make a series of lfr nodes.  The f direction for each is a short tuple
    of the next flen nodes in the sequence.  The result is a oneway tunnel
    with a sparse, randomly selected sequence of nodes.
    """

    name_ = name + ':'
    ret = []
    for i, node in IndexLoop(nodes):
        if i < len(nodes) - flen:
            f = [ name_ + str(j) for j in range(i+1, i+1+flen) ]
        else:
            f = [ name_ + str(j) for j in range(i+1, len(nodes)) ] + [fwd]

        ret += [
            bf(
                name_ + str(i),
                node,
                back,
                f
            )]

    return ret

def lfffr(name, ftuple, left, exit, right):
    """
    Make a series of lfr nodes connected to each other randomly by f
    """

    name_ = name + ':'
    ret = []
    for i, thisf in IndexLoop(ftuple):
        # The choices for this node is any in ftuple except itself,
        # plus exit.
        fs = [ name_ + str(f) for f in range(len(ftuple)) if f != i ]
        fs.append(exit)

        lfr_args = (
                    name_ + str(i),
                    thisf,
                    left,
                    fs,
                    right
                    )
        node = apply(lfr, lfr_args)
        ret += [node]

def photoalbum(name, nodes, exit):
    """
    Make a series of PhotoNode's linked together.
    """
    name_ = name + ':'
    ret = []
    for i, node in IndexLoop(nodes):
        if i == len(nodes)-1:
            f = exit
        else:
            f = name_ + str(i+1)

        ret += [
            PhotoNode(
                name_ + str(i),
                node,
                f,
                exit
            )]

    return ret

        
class ImgShortcut:
    """
    To make image pathnames easier
    """
    def __init__(self, fmt):
        self.fmt = fmt

    def __call__(self, arg):
        if type(arg) == type(1):
            return self.fmt % (arg)
        elif type(arg) == type(()) or type(arg) == type([]):
            return [ self.fmt % a for a in arg ]
        else:
            raise TypeError

class SongMenu(MenuNode):
    """A menu that plays songs"""
    def doChoice(self, song):
        if song == '':
            pygame.mixer.music.stop()
        else:            
            try:
                pygame.mixer.music.load('music\\' + song + '.mp3')
            except:
                try:
                    pygame.mixer.music.load('music\\' + song + '.wav')
                except:
                    pass
            pygame.mixer.music.play()

class NatWorldNode(Node.Node):
    def __init__(self, name, rect):
        Node.Node.__init__(self, name)
        self.rect = rect

    def getImage(self, wa):
        vw = wa.getView()
        self.background = pygame.Surface(vw.get_size(), 0, 16)
        self.background.blit(vw, (0,0))
        return self.background

    def onEnter(self, wa):
        self.prevNode = wa.getNode()
        self.app = WorldApp.WorldApp(wa)
        bigView = wa.getViewRect()
        bigH = bigView[3]
        bigW = bigView[2]
        littleView = Rect(
            self.rect[0] * bigW + bigView[0],
            self.rect[1] * bigH + bigView[1],
            self.rect[2] * bigW,
            self.rect[3] * bigH
            )
        self.app.setRecursive(littleView)
        self.app.setCursors('minicur.bmp', (
            'arrow',    'hand',
            'left',     'right',
            'up',       'down',
            'left180',  'right180',
            'forward',  'back',
            'x'
            ))
        self.app.run()

    def onEvent(self, event, xpos, wa):
        return self.prevNode
    
