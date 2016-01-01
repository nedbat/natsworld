"""
Nat's World
Ned Batchelder, 11/2001
"""

import pygame
import pygame.cursors
import pygame.display
import pygame.draw
import pygame.font
import pygame.image
import pygame.mixer
import pygame.time
import pygame.transform
from pygame.locals import *

import Node
import Transition

# Constants

black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)
yellow = (255,255,0)

class WorldApp:

    def __init__(self, parent = None):
        if not pygame.image.get_extended():
            raise "Must have pygame extended image support!"

        #print "Constructing a WorldApp!"
        if parent != None:
            self.screen = parent.screen
            self.screenSize = parent.screenSize
            self.debug = parent.debug
            self.cursors = parent.cursors
            self.homeNode = parent.homeNode
            self.gameTitle = parent.gameTitle
            self.creditRoll = parent.creditRoll
            self.creditSong = parent.creditSong
        else:
            self.screenSize = (800, 600)
            self.homeNode = Node.NullNode()

        self.node = Node.NullNode()
        self.viewSize = None

    # Properties

    gameTitle = None
    screenSize = None
    fullScreen = 0
    debug = 0
    caption = 0
    validateNodes = 0
    transitions = 1
    creditRoll = None
    creditSong = None
    recursive = 0
    
    #
    # Members
    #
    
    screen = None

    view = None
    viewRect = None

    homeNode = None
    node = None

    cursors = None
    
    #
    # Property setters and getters
    #
    
    def setTitle(self, gameTitle):
        self.gameTitle = gameTitle

    def getTitle(self):
        return self.gameTitle

    def setScreenSize(self, screenSize):
        self.screenSize = screenSize

    def getViewSize(self):
        return self.viewSize

    def getViewRect(self):
        return self.viewRect
    
    def setFullScreen(self, fullScreen):
        self.fullScreen = fullScreen

    def setDebug(self, debug):
        self.debug = debug

    def setCaption(self, caption):
        self.caption = caption
        
    def setValidateNodes(self, validateNodes):
        self.validateNodes = validateNodes

    def setTransitions(self, transitions):
        self.transitions = transitions
        
    def setHomeNode(self, homeNode):
        self.homeNode = homeNode

    def getHomeNode(self):
        return self.homeNode
    
    def setCreditRoll(self, creditRoll):
        self.creditRoll = creditRoll
        
    def setCreditSong(self, creditSong):
        self.creditSong = creditSong
        
    def getView(self):
        """Get a reference to the current view"""
        return self.view

    def getNode(self):
        "Get the current node"
        return self.node

    def setCursors(self, file, names):
        from MakeCursors import MakeCursors
        self.cursors = MakeCursors(file, names)

    def getCursor(self, name):
        try:
            return self.cursors[name]
        except KeyError:
            try:
                return self.cursors['arrow']
            except KeyError:
                return pygame.cursors.arrow

    def setRecursive(self, viewRect):
        """
        This game engine is recursive.
        viewRect is the rect on the screen to work in.
        """
        self.recursive = 1
        self.viewRect = viewRect
        self.viewSize = viewRect.size
        
    #
    # Methods
    #

    def safeApply(self, fn, *args):
        """Protect ourself from errors in a function call."""
        
        try:
            return fn(*args)
        except:
            if self.debug:
                print "safeApply Traceback:"
                import traceback
                traceback.print_exc(99)
            return None

    def doInit(self):
        """Initialize everything."""
        
        #pygame.mixer.pre_init(44100, 16, 1)
        pygame.init()
        #print pygame.display.Info()
        flags = 0
        if self.fullScreen:
            flags = flags | FULLSCREEN
        depth = pygame.display.mode_ok(self.screenSize, flags, 16)
        #print depth
        self.screen = pygame.display.set_mode(self.screenSize, flags, depth)
        #print "screen bits = ", self.screen.get_bitsize()
        #print self.screen.get_palette()

        if self.gameTitle != None:
            pygame.display.set_caption(self.gameTitle)
        pygame.mouse.set_visible(1)
        
    def createView(self):
        # Create the view surface.
        if self.viewSize == None:
            self.viewSize = self.screen.get_size()
            self.viewRect = Rect(0, 0, self.viewSize[0], self.viewSize[1])

        self.view = pygame.Surface(self.viewSize, 0, 16)
        #print "view bits = ", self.view.get_bitsize()
        self.view.fill(black)
        #print "View pos is %s" % (self.viewRect,)
        
    def doTerm(self):
        pygame.quit()
        

    def doTitle(self):
        """Display the title."""
        
        if self.gameTitle == None:
            return
        
        # Create centered text.
        font = pygame.font.Font(None, self.viewRect.height/8)
        text = font.render(self.gameTitle, 1, red)
        textpos = text.get_rect()
        textpos.center = self.view.get_rect().center
        self.updateView(text, textpos)

        # Display the view for one second.
        pygame.time.delay(1000)


    def doCredits(self):
        """Display credits."""
        
        if self.creditRoll == None:
            return
        
        viewback = pygame.Surface(self.view.get_size(), 0, 16)
        viewback.blit(self.view, (0,0))
        self.view.fill(black)

        roll = self.creditRoll
        font = pygame.font.Font(None, self.viewRect.height/20)
        lineskip = self.viewRect.height/15

        rollsurf = pygame.Surface((self.viewRect.width, len(roll)*lineskip), 0, 16)
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
            pygame.mixer.music.set_endevent(QUIT)
        else:
            # After some time, quit
            pygame.time.set_timer(QUIT, 10000)

        # Compute parameters for scrolling credits
        rollsurf.set_colorkey((0,0,0))
        topy = (self.view.get_height() - rollsurf.get_height())/2
        xpos = (self.view.get_width() - rollsurf.get_width())/2
        vbalpha = 255
        finaldelay = 1
        ydelta = (self.view.get_height() - topy) / 200
        if ydelta == 0:
            ydelta = 1
        nsteps = (self.view.get_height() - topy) / ydelta
        tdelta = 2000 / nsteps
        adelta = (255 / nsteps) + 1
        if adelta == 0:
            adelta = 1

        # Run the scroll        
        for ypos in range(self.view.get_height(), topy, -ydelta):
            viewback.set_alpha(vbalpha)
            if vbalpha >= adelta:
                vbalpha -= adelta
            self.view.fill(black)
            self.view.blit(viewback, (0,0))
            self.view.blit(rollsurf, (xpos, ypos))
            self.updateView()

            event = pygame.event.poll()

            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                finaldelay = 0
                break
            pygame.time.delay(tdelta)
            
        if finaldelay:
            pygame.event.wait()

        # clear the quit timer.
        pygame.time.set_timer(QUIT, 0)
        pygame.mixer.music.set_endevent(NOEVENT)
        
    def enterNode(self, node):
        """Handle the logic of entering a node"""
        
        if self.debug:
            print "Entering %s" % (node)

        self.safeApply(node.onEnter, self)

        # Get the image to display
        img = self.safeApply(node.getImage, self)

        # Let the old node specify a transition
        if self.transitions:
            tc = self.safeApply(self.node.getTransitionClass, node)
            if tc:
                if self.debug:
                    print "Using transition", tc
                t = tc(self)
                t.setImages(self.view, img)
                t.run()

        self.view.fill(self.safeApply(node.getBackColor, self))
        vx, vy = self.view.get_size()
        pos = (
            (vx-img.get_width())/2,
            (vy-img.get_height())/2
        )
        #if self.debug:
        #    print "Positioning at %d, %d" % pos
        self.updateView(img, pos)

        if self.caption:
            font = pygame.font.Font(None, self.viewRect.height/20)
            text = font.render(str(node), 1, white, black)
            textpos = text.get_rect()
            textpos.midbottom = self.view.get_rect().midbottom
            self.updateView(text, textpos)
            
        self.node = node
        
        # Fake a mousemotion event to get the cursor right.
        ev = pygame.event.Event(MOUSEMOTION, pos = pygame.mouse.get_pos())
        self.doEvent(ev)

    def leaveNode(self, node):
        """Handle the logic of leaving a node"""

        if self.debug:
            print "Leaving  %s" % (node)

        self.safeApply(node.onLeave, self)

    def updateView(self, img = None, pos = None):
        if 0:
            print "updateView,",
            print "screen = ", self.screen,
            print "img = ", img,
            print "pos = ", pos
        if img:
            #print "blitting at ", pos
            self.view.blit(img, pos or (0,0))
        self.screen.blit(self.view, self.viewRect)
        pygame.display.update(self.viewRect)
        
    def drawGrid(self):
        view2 = pygame.Surface(self.view.get_size(), 0, 16)
        view2.blit(self.view, (0,0))
        w, h = view2.get_size()
        for f in range(10):
            pygame.draw.line(view2, white, (0, f*h/10), (w, f*h/10))
            pygame.draw.line(view2, white, (f*w/10, 0), (f*w/10, h))
        self.screen.blit(view2, self.viewRect)
        pygame.display.update(self.viewRect)

    def doEvent(self, event):
        # Need to translate the mouse position to view coords, but
        # the event is readonly (why?).
        if hasattr(event, 'pos'):
            xpos = (
                event.pos[0] - self.viewRect.left,
                event.pos[1] - self.viewRect.top
            )
        else:
            xpos = (0,0)

        # Let the node handle the event
        return self.safeApply(self.node.onEvent, event, xpos, self)
        
    def run(self):
        if not self.recursive:
            self.doInit()
        self.createView()
        self.doTitle()

        if self.validateNodes:
            Node.validateAllNodes()
            
        # This made it look worse!
        #pal = pygame.image.load(r'c:\ned\nat\world\common.pal')
        #self.screen.set_palette(pal.get_palette())
        
        # Enter the first node
        self.node = self.homeNode
        if type(self.node) == type(""):
            self.node = Node.findNode(self.node)
        self.enterNode(self.node)

        # Main event loop
        while 1:
            
            event = pygame.event.wait()

            #if self.debug:
            #    print "Event: ", event
                
            # Quitting the game is always the same regardless of node.
            if event.type == QUIT:
                break

            newnode = self.doEvent(event)

            # What did the node ask us to do?
            if type(newnode) == type(""):
                newnode = Node.findNode(newnode)

            if newnode != None:
                # Changing nodes
                self.leaveNode(self.node)
                self.enterNode(newnode)

            # default handling if the node didn't want it.
            if newnode == None:
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    # Quit the game
                    break
                if self.debug and event.type == KEYDOWN and event.key == K_3:
                    self.drawGrid()

        self.leaveNode(self.node)
        
        # Clean up
        self.doCredits()

        if not self.recursive:
            self.doTerm()
