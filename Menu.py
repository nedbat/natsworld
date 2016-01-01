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
        [ (text, choiceArg, {key}), ... ]
        """
        Node.Node.__init__(self, name)
        self.choices = choices
        self.mouseover = -1

    def getReprInfo(self):
        if self.mouseover >= 0:
            return self.choices[self.mouseover][0]
        else:
            return "none"

    def getMenuSize(self, wa):
        """Overridable to give the size of the menu"""
        return (wa.getViewSize()[1]/2, len(self.choices) * self.getTextSkip(wa))

    def getMenuColor(self):
        """Overridable for the color of the menu background"""
        return (0,0,0)

    def getTextColor(self):
        """Overridable for the color of the menu text"""
        return (250, 240, 20)
    
    def getOverColor(self):
        """Overridable for the color of menu text being hovered over"""
        return (255, 255, 255)
    
    def getFont(self, wa):
        return pygame.font.Font(None, wa.getViewSize()[1]/20)

    def getTextSkip(self, wa):
        return wa.getViewSize()[1]/20

    def getMenuPos(self, wa):
        """Overridable to position the menu: None means center it"""
        return None
    
    def getImage(self, wa):
        return self.background

    def updateMenu(self, wa):
        backsurf = pygame.Surface(self.background.get_size(), 0, 16)
        
        menusurf = pygame.Surface(self.getMenuSize(wa), 0, 16)
        menusurf.fill(self.getMenuColor())

        font = self.getFont(wa)

        for i in range(len(self.choices)):
            text, callable = self.choices[i][:2]
            if i == self.mouseover:
                color = self.getOverColor()
            else:
                color = self.getTextColor()
            linesurf = font.render(text, 1, color)
            menusurf.blit(linesurf, (0, i * self.getTextSkip(wa)))

        menusurf.set_alpha(200)

        backsurf.blit(self.background, (0,0))
        backsurf.blit(menusurf, self.pos)
        wa.updateView(backsurf)

    def onEnter(self, wa):
        prevNode = wa.getNode()
        if prevNode != self:
            self.prevNode = prevNode
            vw = wa.getView()
            self.background = pygame.Surface(vw.get_size(), 0, 16)
            self.background.blit(vw, (0,0))
            self.mouseover = -2         # force a redraw on the first mousemotion
            self.pos = self.getMenuPos(wa)
            self.menuSize = self.getMenuSize(wa)
            if self.pos == None:
                self.pos = (
                    (self.background.get_width() - self.menuSize[0]) / 2,
                    (self.background.get_height() - self.menuSize[1]) / 2
                )

        pygame.mouse.set_cursor(*wa.getCursor('arrow'))
        
    def onEvent(self, event, xpos, wa):
        ret = None
        do = None
        
        if hasattr(event, 'pos'):
            pos = (xpos[0] - self.pos[0], xpos[1] - self.pos[1])
            if 0 <= pos[0] < self.getMenuSize(wa)[0]:
                posChoice = pos[1] / self.getTextSkip(wa)
                if 0 <= posChoice < len(self.choices):
                    pass
                else:
                    posChoice = -1
            else:
                posChoice = -1

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
                    do = self.mouseover
            elif 0 < event.key < 256:
                # is there a menu item with this as a shortcut key?
                char = chr(event.key)
                if char in "123456789":
                    do = int(char)-1
                else:
                    for i in range(len(self.choices)):
                        ch = self.choices[i]
                        if len(ch) >= 3:
                            if char == ch[2]:
                                do = i
                            
        elif event.type == MOUSEBUTTONDOWN:
            if posChoice >= 0:
                do = posChoice
            else:
                ret = self.prevNode

        elif event.type == MOUSEMOTION:
            mover = posChoice

        if ret == None:
            if do != None:
                ret = self.doChoice(self.choices[int(do)][1])
            elif mover != self.mouseover:
                self.mouseover = mover
                self.updateMenu(wa)
            
        return ret

    def doChoice(self, choice):
        """Overridable to execute a menu choice"""
        return choice
