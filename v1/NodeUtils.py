"""
Utilities for nodes in Nat's World
"""

from Node import lr, lfr, bf

class stringer:
    "Any attribute is itself as a string"
    
    def __getattr__(self, name):
        return name

s = stringer()

def nesw(name, **i):
    """
    Make four nodes for n, e, w, s from a location.
    Keywords:
        images: ni, ei, wi, si.
        destinations: n, e, w, s.
    """

    name_ = name + ':'
    ret = []
    left = {'n': 'w', 'e': 'n', 's': 'e', 'w': 's'}
    right = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}
    
    # repair missing positions.
    for d in "nesw":
        if not i.has_key(d + 'i'):
            oldleft = left[d]
            oldright = right[d]
            left[oldright] = oldleft
            right[oldleft] = oldright
            
    # create the nodes                
    for d in "nesw":
        if i.has_key(d + 'i'):
            if i.has_key(d):
                node = lfr(
                        name_ + d,
                        i[d + 'i'],
                        name_ + left[d],
                        i[d],
                        name_ + right[d]
                        )
            else:
                node = lr(
                        name_ + d,
                        i[d + 'i'],
                        name_ + left[d],
                        name_ + right[d]
                        )
                
            ret.append(node)

    return ret

def tunnel(name, nodepairs, back, fwd):
    """
    Make a series of bf nodes forming a tunnel
    """

    name_ = name + ':'
    ret = []
    for i in range(len(nodepairs)):
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
                    nodepairs[i][0],
                    name_ + str(i) + 'b',
                    f
                    )
        nodeb = bf(
                    name_ + str(i) + 'b',
                    nodepairs[i][1],
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
    for i in range(len(nodes)):
        if i == len(nodes)-1:
            f = fwd
        else:
            f = name_ + str(i+1)

        ret += [
            bf(
                name_ + str(i),
                nodes[i],
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
    for i in range(len(ftuple)):
        # The choices for this node is any in ftuple except itself,
        # plus exit.
        fs = [ name_ + str(f) for f in range(len(ftuple)) if f != i ]
        fs.append(exit)

        lfr_args = (
                    name_ + str(i),
                    ftuple[i],
                    left,
                    fs,
                    right
                    )
        node = apply(lfr, lfr_args)
        ret += [node]
        
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
