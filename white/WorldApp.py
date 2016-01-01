"""
Nat's World
Ned Batchelder, 11/2001
"""

import pygame
import pygame.display
import pygame.font
import pygame.image
import pygame.mixer
import pygame.time
import pygame.transform
from pygame.locals import *

import Node

# Constants

black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)

class WorldApp:

    # This class is a singleton of sorts (the Borg pattern from ASPN's Python
    # cookbook).  All instances share the same state.
    # (http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/66531)

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

    # Properties
    
    gameTitle = ""
    screenSize = (800, 600)
    fullScreen = 0
    debug = 0
    creditRoll = None
    creditSong = None
    
    #
    # Members
    #
    
    screen = None

    view = None
    viewPos = None
    
    node = Node.NullNode()

    #
    # Property setters
    #
    
    def setTitle(self, gameTitle):
        self.gameTitle = gameTitle

    def setScreenSize(self, screenSize):
        self.screenSize = screenSize

    def getScreenSize(self):
        return self.screenSize

    def setFullScreen(self, fullScreen):
        self.fullScreen = fullScreen

    def setDebug(self, debug):
        self.debug = debug

    def setHomeNode(self, homeNode):
        self.node = homeNode
        if type(self.node) == type(""):
            self.node = Node.findNode(self.node)

    def setCreditRoll(self, creditRoll):
        self.creditRoll = creditRoll
        
    def setCreditSong(self, creditSong):
        self.creditSong = creditSong
        
    def getScreen(self):
        "Get a reference to the current screen"
        return self.screen

    def getNode(self):
        "Get the current node"
        return self.node

    #
    # Methods
    #
        
    # Initialize everything.
    def doInit(self):
        pygame.mixer.pre_init(44100, 16, 1)
        pygame.init()
        #flags = HWSURFACE|DOUBLEBUF   # These flags make things not work!
        flags = 0
        if self.fullScreen:
            flags = flags | FULLSCREEN
        depth = pygame.display.mode_ok(self.screenSize, flags, 24)
        self.screen = pygame.display.set_mode(self.screenSize, flags, depth)
        pygame.display.set_caption(self.gameTitle)
        pygame.mouse.set_visible(1)
        
        # Create the view surface.
        self.view = pygame.Surface(self.screen.get_size())
        self.view.fill(black)
        self.viewPos = Rect(0, 0, self.view.get_width(), self.view.get_height())

    def doTerm(self):
        pygame.quit()
        
    # Display the title.
    def doTitle(self):
        # Create centered text.
        font = pygame.font.Font(None, 48)
        text = font.render(self.gameTitle, 1, red)
        textpos = text.get_rect()
        textpos.center = self.view.get_rect().center
        self.view.blit(text, textpos)

        # Display the view for one second.
        self.screen.blit(self.view, (0, 0))
        pygame.display.flip()
        pygame.time.delay(1000)

    # Display credits.        
    def doCredits(self):
        if self.creditRoll == None:
            return
        
        viewback = pygame.Surface(self.view.get_size())
        viewback.blit(self.view, (0,0))
        self.view.fill(black)

        roll = self.creditRoll
        font = pygame.font.Font(None, 30)
        lineskip = 40

        rollsurf = pygame.Surface((800, len(roll)*lineskip))
        ypos = 0
        for line in roll:
            color = yellow
            if type(line) == type(()):
                line, color = line
            linesurf = font.render(line, 1, color)
            leftmar = (rollsurf.get_width() - linesurf.get_width())/2
            rollsurf.blit(linesurf, (leftmar, ypos))
            ypos += lineskip

        # Play the song if we have one
        if self.creditSong:
            pygame.mixer.music.load(self.creditSong)
            pygame.mixer.music.play()
            
        # Now scroll the credits
        rollsurf.set_colorkey((0,0,0))
        topy = (self.view.get_height() - rollsurf.get_height())/2
        xpos = (self.view.get_width() - rollsurf.get_width())/2
        vbalpha = 255
        finaldelay = 1
        for ypos in range(self.view.get_height(), topy, -3):
            viewback.set_alpha(vbalpha)
            if vbalpha >= 2:
                vbalpha -= 2
            self.view.fill(black)
            self.view.blit(viewback, (0,0))
            self.view.blit(rollsurf, (xpos, ypos))
            self.screen.blit(self.view, (0, 0))
            pygame.display.flip()

            event = pygame.event.poll()

            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                finaldelay = 0
                break
            #pygame.time.delay(2)
            
        # Display the final image for 5 seconds.
        #pygame.time.set_timer(USEREVENT, 5000)
        
        if finaldelay:
            pygame.time.delay(5000)

    # Handle the logic of entering a node
    def enterNode(self, node):
        if (self.debug):
            print "Entering %s" % (node)

        try:            
            node.onEnter()
        except:
            pass

        # Get the image to display
        try:
            img = node.getImage()
        except:
            pass
        
        self.view.fill(black)
        vx, vy = self.view.get_size()
        pos = ( (vx-img.get_width())/2, (vy-img.get_height())/2 )
        #if (self.debug):
        #    print "Positioning at %d, %d" % pos
        self.view.blit(img, pos)
        self.screen.blit(self.view, self.viewPos)
        pygame.display.update(self.viewPos)

    def leaveNode(self, node):
        if (self.debug):
            print "Leaving %s" % (node)

        try:
            node.onLeave()
        except:
            pass
        
    def main(self):
        self.doInit()
        self.doTitle()

        self.view.fill(black)
        self.screen.blit(self.view, (0,0))
        pygame.display.flip()

        # Enter the first node
        self.enterNode(self.node)

        # Main event loop
        while 1:
            
            event = pygame.event.poll()

            # Quitting the game is always the same regardless of node.
            if event.type == QUIT:
                break

            # Let the node handle the event
            try:
                newnode = self.node.onEvent(event)
            except:
                pass

            # What did the node ask us to do?
            if type(newnode) == type(""):
                newnode = Node.findNode(newnode)

            if newnode != None:
                # Changing nodes
                self.leaveNode(self.node)
                self.enterNode(newnode)
                self.node = newnode

            # default handling if the node didn't want it.
            if newnode == None:
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    break
                
        self.leaveNode(self.node)
        
        # Clean up
        self.doCredits()
        self.doTerm()
