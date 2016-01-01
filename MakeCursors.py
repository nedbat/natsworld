"""
Make pygame cursors from an image file
"""

import pygame
import pygame.image
import pygame.cursors
    
def MakeCursors(filename, names):
    """
    MakeCursors(filename, names):
    Read the image at filename, creating 32x32 cursors.  Return a dictionary
    of cursors, assigned to the names in names.
    Colors in the image:
    black and white are black and white.
    Red and magenta are the hotspot (colored black or white, respectively).
    Any other color is transparent.
    """

    # Load the raw tile image
    try:
        tiles = pygame.image.load(filename)
    except pygame.error:
        raise pygame.error, 'Could not load image "%s" %s' % (filename, pygame.get_error())

    tileWidth = 32
    tileHeight = 32

    curs = {}

    tiles.lock()

    # Split it into individual tiles
    for ycur in range(tiles.get_height() / tileHeight):
        for xcur in range(tiles.get_width() / tileWidth):
            tileX = xcur * tileWidth
            tileY = ycur * tileHeight

            strings = []
            hot = (0,0)

            if len(names) > 0 and names[0] != '':            
                for y in range(tileY, tileY + tileHeight):
                    l = ''
                    for x in range(tileX, tileX + tileWidth):
                        clr = tiles.get_at((x, y))[:3]
                        # not sure why, but the colors are impure.  Force them to black, white, or green
                        pclr = map(lambda x: x > 100, clr)
                        if pclr == [0,0,0]:
                            l += 'X'
                        elif pclr == [1,1,1]:
                            l += '.'
                        elif pclr == [1,0,0]:
                            l += 'X'
                            hot = (x - tileX, y - tileY)
                        elif pclr == [1,0,1]:
                            l += '.'
                            hot = (x - tileX, y - tileY)
                        else:
                            l += ' '
                    strings.append(l)

                data = pygame.cursors.compile(strings, ".", "X")
                curs[names[0]] = ( (tileWidth, tileHeight), hot) + data

            names = names[1:]

    tiles.unlock()
    
    return curs


if __name__ == '__main__':
    pygame.init()
    print MakeCursors('cursors.bmp', ('arrow', 'forward', 'left', 'right'))
