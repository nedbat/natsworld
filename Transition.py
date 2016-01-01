"""
Transitions for Nat's World.
"""

import pygame
import pygame.time
from pygame.locals import *

# For debugging.
NSTEPS = 3
DELAY = 5

class Transition:
    """A Transition takes two surfaces, and transitions from one to the other."""

    def __init__(self, wa):
        self.wa = wa
        self.surf1 = None
        self.surf2 = None
        
    def setImages(self, surf1, surf2):
        self.surf1 = pygame.Surface(surf1.get_size())
        self.surf1.blit(surf1, (0,0))
        self.surf2 = pygame.Surface(surf2.get_size())
        self.surf2.blit(surf2, (0,0))
        
    def run(self):
        pass


class SlideTransition(Transition):

    def getDelta(self, r, nSteps):
        pass

    def getRect2(self, r):
        pass
    
    def run(self):
        r1 = Rect(self.wa.getViewRect())
        r2 = self.getRect2(r1)
        surf = pygame.Surface(r1.size)
        nsteps = NSTEPS
        dpos = self.getDelta(r1, nsteps)
        for i in range(1, nsteps):
            r1.move_ip(*dpos)
            r2.move_ip(*dpos)
            #print "Step ", i, r1, r2
            surf.blit(self.surf1, r1)
            surf.blit(self.surf2, r2)
            self.wa.updateView(surf, (0,0))
            if DELAY > 0:
                pygame.time.delay(DELAY)

class SlideLeft(SlideTransition):
    def getRect2(self, r): return r.move(r.width, 0)    
    def getDelta(self, r, nsteps): return (-r.width / nsteps, 0)

class SlideRight(SlideTransition):
    def getRect2(self, r): return r.move(-r.width, 0)    
    def getDelta(self, r, nsteps): return (r.width / nsteps, 0)

class SlideUp(SlideTransition):
    def getRect2(self, r): return r.move(0, r.height)    
    def getDelta(self, r, nsteps): return (0, -r.height / nsteps)

class SlideDown(SlideTransition):
    def getRect2(self, r): return r.move(0, -r.height)    
    def getDelta(self, r, nsteps): return (0, r.height / nsteps)

class Dissolve(Transition):
    
    def run(self):
        # Not sure why, but two surfaces whose alphas add to 255 look too dark.
        # (Brightness is non-linear?)
        # Add a boost to fudge it.

        boost = 70
        
        r = self.wa.getViewRect()
        surf = pygame.Surface(r.size)
        oa1 = self.surf1.get_alpha() or 255
        oa2 = self.surf2.get_alpha() or 255
        nsteps = NSTEPS
        da1 = oa1/nsteps
        da2 = oa2/nsteps
        a1 = oa1
        a2 = 0
        for i in range(1, nsteps):
            surf.fill((0,0,0))
            a1 -= da1
            a2 += da2
            #print "Step %d, a1 = %d, a2 = %d" % (i, a1, a2)
            self.surf1.set_alpha(a1+boost)
            self.surf2.set_alpha(a2+boost)
            surf.blit(self.surf1, r)
            surf.blit(self.surf2, r)
            self.wa.updateView(surf, (0,0))
            if DELAY > 0:
                pygame.time.delay(DELAY)

        self.surf1.set_alpha(oa1)
        self.surf2.set_alpha(oa2)
