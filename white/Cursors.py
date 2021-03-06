"""
Copyright 2001 Andrew Jones

This file is part of Pyzzle.

    Pyzzle is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    Pyzzle is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Pyzzle; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


"""

import pygame, pygame.cursors
from pygame.locals import *

def compile(strings, hotspot):
    "Local function to compile our cursors"
    data = pygame.cursors.compile(strings, ".", "X")
    return ( (len(strings), len(strings[0])), hotspot) + data
    
# [ xs.replace('a', 'A').replace('b', 'B') for xs in x ]

left = compile([
    "                        ",
    "            XX          ",
    "           X..X         ",
    "           X...X        ",
    "           X....X       ",
    "            X....X      ",
    "             X....X     ",
    "   XXXXXXXXXXXX....X    ",
    "  X..................XX ",
    "  X....................X",
    "   XXXXXXXXXXXXXX......X",
    "          X......X.....X",
    "          X......X.....X",
    "           XXXXXX......X",
    "          X......X.....X",
    "          X......X.....X",
    "           XXXXXX.....X ",
    "          X......X...X  ",
    "          X......X.XX   ",
    "           XXXXXXX      ",
    "                        ",
    "                        ",
    "                        ",
    "                        "], (4, 8))  #sized 24x24

right = compile([
    "                        ",
    "          XX            ",
    "         X..X           ",
    "        X...X           ",
    "       X....X           ",
    "      X....X            ",
    "     X....X             ",
    "   XX....XXXXXXXXXXXX   ",
    " XX..................X  ",
    "X....................X  ",
    "X......XXXXXXXXXXXXXX   ",
    "X......X.....X          ",
    "X......X.....X          ",
    "X......XXXXXX           ",
    "X......X.....X          ",
    "X......X.....X          ",
    " X.....XXXXXX           ",
    "  X....X.....X          ",
    "   XX..X.....X          ",
    "     XXXXXXX            ",
    "                        ",
    "                        ",
    "                        ",
    "                        "], (20, 8))  #sized 24x24

right180 = compile([
    "                        ",
    "          XX            ",
    "         X..X           ",
    "        X...X           ",
    "       X....X           ",
    "      X....X            ",
    "     X....X             ",
    "   XX....XXXXXXXX       ",
    " XX..........X...X      ",
    "X............X...X      ",
    "X......XXXXXXXXXX       ",
    "X......X.....X          ",
    "X......X.....X          ",
    "X......XXXXXX           ",
    "X......X.....X          ",
    "X......X.....X          ",
    " X.....XXXXXX           ",
    "  X....X.....X          ",
    "   XX..X.....X          ",
    "     XXXXXXX            ",
    "                        ",
    "                        ",
    "                        ",
    "                        "], (6, 16))  #sized 24x24

left180 = compile([
    "                        ",
    "            XX          ",
    "           X..X         ",
    "           X...X        ",
    "           X....X       ",
    "            X....X      ",
    "             X....X     ",
    "     XXXXXXXXXX....X    ",
    "    X...X............XX ",
    "    X...X..............X",
    "     XXXXXXXXXXXX......X",
    "          X......X.....X",
    "          X......X.....X",
    "           XXXXXX......X",
    "          X......X.....X",
    "          X......X.....X",
    "           XXXXXX.....X ",
    "          X......X...X  ",
    "          X......X.XX   ",
    "           XXXXXXX      ",
    "                        ",
    "                        ",
    "                        ",
    "                        "], (6, 16))  #sized 24x24

action = compile([
    "    XX XX XX XX         ",
    "   X..X..X..X..X        ",
    "   X..X..X..X..X        ",
    "   XXXXXXXXXXXXX        ",
    "   X...........X        ",
    "XXXX...........X        ",
    "X..X...........X        ",
    "X..X...........X        ",
    " X............X         ",
    "  X...........X         ",
    "   X..........X         ",
    "    XXXXXXXXXX          ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        "], (6, 7))  #sized 24x24

forward = compile([
    "                        ",
    "                        ",
    "        XX              ",
    "       X..X             ",
    "       X..X             ",
    "       X..X             ",
    "       X..X             ",
    "       X..X             ",
    "       X..XXX XX XX     ",
    "       X..X..X..X..X    ",
    "       X..X..X..X..X    ",
    "       XXXXXXXXXXXXX    ",
    "    XX X...........X    ",
    "   X..XX...........X    ",
    "   X..XX...........X    ",
    "    X..X...........X    ",
    "     X............X     ",
    "      X...........X     ",
    "       XX.........X     ",
    "        XXXXXXXXXX      ",
    "                        ",
    "                        ",
    "                        ",
    "                        "], (9, 3))  #sized 24x24

noaction = compile([
    "           XX           ",
    "          X..XXX        ",
    "        XXX..X..X       ",
    "       X..X..X..XXX     ",
    "       X..X..X..X..X    ",
    "       X..X..X..X..X    ",
    "       X..X..X..X..X    ",
    "       X..X..X..X..X    ",
    "       X..X..X..X..X    ",
    "       XXXXXXXXXXXXX    ",
    "       X...........X    ",
    "    XXXX...........X    ",
    "    X..X...........X    ",
    "    XX.X...........X    ",
    "     X............X     ",
    "      X...........X     ",
    "       XX.........X     ",
    "        XXXXXXXXXX      ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        "], (12, 3))
    
up = compile([
    "                        ",
    "                        ",
    "                        ",
    "   XXXX                 ",
    "   X..X                 ",
    "   X..X                 ",
    "   X..X                 ",
    "   X..X                 ",
    "   X..X                 ",
    "   X..XXXXXXXXXX        ",
    "   X..X..X..X..X        ",
    "  XXXXX..X..X..X        ",
    " X....X..X..X..X        ",
    "X.....X..X..X..X        ",
    "X...XXX..X..X..X        ",
    "X...XX.XX.XX.XXX        ",
    "X..............X        ",
    " X............X         ",
    "  X...........X         ",
    "   XX.........X         ",
    "    XXXXXXXXXX          ",
    "                        ",
    "                        ",
    "                        "], (5, 2))
 
down = compile([
    "                        ",
    "                        ",
    "                        ",
    "    XXXXXXXXXX          ",
    "   XX.........X         ",
    "  X...........X         ",
    " X............X         ",
    "X..............X        ",
    "X...XX.XX.XX.XXX        ",
    "X...XXX..X..X..X        ",
    "X.....X..X..X..X        ",
    " X....X..X..X..X        ",
    "  XXXXX..X..X..X        ",
    "   X..X..X..X..X        ",
    "   X..XXXXXXXXXX        ",
    "   X..X                 ",
    "   X..X                 ",
    "   X..X                 ",
    "   X..X                 ",
    "   X..X                 ",
    "   XXXX                 ",
    "                        ",
    "                        ",
    "                        "], (5, 21))
