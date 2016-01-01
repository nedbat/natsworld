"""
Menu nodes for Nat's world.
"""

import pygame
import pygame.font
from pygame.locals import *
import Node
import WorldApp

class MenuNode(Node.Node):
    def __init__(self, name, choices):
        """
        Choices is a list:
        [ (text, callable), (text, callable), ... ]
        """
        Node.Node.__init__(self, name)
        self.choices = choices

    def getMenuSize(self):
        """Overridable to give the size of the menu"""
        return (300, len(self.choices) * self.getTextSkip())

    def getMenuColor(self):
        """Overridable for the color of the menu background"""
        return (0,0,0)

    def getTextColor(self):
        """Overridable for the color of the menu text"""
        return (240, 230, 128)
    
    def getOverColor(self):
        """Overridable for the color of menu text being hovered over"""
        return (255, 255, 255)
    
    def getFont(self):
        return pygame.font.Font(None, 40)

    def getTextSkip(self):
        return 40

    def getMenuPos(self):
        return None
    
    def getImage(self):
        backsurf = pygame.Surface(self.background.get_size())
        
        menusurf = pygame.Surface(self.getMenuSize())
        menusurf.fill(self.getMenuColor())

        font = self.getFont()

        for i in range(len(self.choices)):
            text, callable = self.choices[i]
            if i == self.mouseover:
                color = self.getOverColor()
            else:
                color = self.getTextColor()
            linesurf = font.render(text, 1, color)
            menusurf.blit(linesurf, (0, i * self.getTextSkip()))

        pos = self.getMenuPos()
        if pos == None:
            pos = (
                (backsurf.get_width() - menusurf.get_width()) / 2,
                (backsurf.get_height() - menusurf.get_height()) / 2
            )

        menusurf.set_alpha(200)

        backsurf.fill((0,0,0))
        backsurf.blit(self.background, (0,0))
        backsurf.blit(menusurf, pos)
        self.pos = pos
        return backsurf

    def onEnter(self):
        prevNode = WorldApp.WorldApp().getNode()
        if prevNode != self:
            self.prevNode = prevNode
            scr = WorldApp.WorldApp().getScreen()
            self.background = pygame.Surface(scr.get_size())
            self.background.blit(scr, (0,0))
            self.mouseover = -1
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        
    def onEvent(self, event):
        ret = None

        if hasattr(event, 'pos'):
            pos = (event.pos[0] - self.pos[0], event.pos[1] - self.pos[1])
            if 0 <= pos[0] < self.getMenuSize()[0]:
                nChoice = pos[1] / self.getTextSkip()
                if 0 <= nChoice < len(self.choices):
                    pass
                else:
                    nChoice = -1
            else:
                nChoice = -1

        mover = self.mouseover
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE and event.mod == 0:
                ret = self.prevNode
            elif event.key == K_DOWN:
                mover = (self.mouseover + 1) % len(self.choices)
            elif event.key == K_UP:
                mover = (self.mouseover - 1) % len(self.choices)
            elif event.key == K_RETURN:
                if self.mouseover >= 0:
                    ret = self.doChoice(self.choices[self.mouseover][1])
        elif event.type == MOUSEBUTTONDOWN:
            if nChoice >= 0:
                ret = self.doChoice(self.choices[nChoice][1])
            else:
                ret = self.prevNode
        elif event.type == MOUSEMOTION:
            mover = nChoice

        if ret == None:        
            if mover != self.mouseover:
                self.mouseover = mover
                ret = self
            
        return ret

    def doChoice(self, choice):
        return choice()
