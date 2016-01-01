"""
Nat's World
Ned Batchelder, 11/2001
"""
import WorldApp
import Node
from Node import lr, lfr, bf
from NodeUtils import *
from Menu import *

jul12 =     ImgShortcut(r'C:\img\vol2\20010712\dscf%04d.jpg')
nov4 =      ImgShortcut(r'C:\img\vol3\20011104\dscf%04d.jpg')
nov10 =     ImgShortcut(r'C:\img\vol3\20011110\dscf%04d.jpg')
nov11 =     ImgShortcut(r'C:\img\vol3\20011111\dscf%04d.jpg')
nov12 =     ImgShortcut(r'C:\img\vol3\20011112\dscf%04d.jpg')
libimg =    ImgShortcut(r'C:\img\libraryweb\library%d.jpg')

# Nodes for Nat's world

natsnodes = [
#    lfr('null', r'C:\img\vol1\20010408\dscf0038.jpg', 'hall:w', 'hall:w', 'hall:w'),

    # Inside the house: first floor

    nesw('hall',
        ni = jul12(28),     n = 'front43:n',
        ei = nov12(501),    e = 'livingroom:e',
        si = jul12(23),     s = 'playroom_right',
        wi = jul12(30),     w = 'diningroom_in',
    ),
    
    lr('playroom_right',    jul12(27),  'playroom_left',                        'hall:n'),
    lr('playroom_left',     jul12(25),  'hall:n',                               'playroom_right'),

    nesw('livingroom',
        ni = nov12(497),
        ei = nov12(494),
        si = nov12(495),    s = 'stereo_s',
        wi = nov12(496),    w = 'hall:w'
         ),

    lfr('stereo_s', nov12(498), 'stereo_e',     'menu_stereo',  'livingroom:n'),
    lfr('stereo_e', nov12(500), 'livingroom:n', 'porch:e',      'stereo_s'),
                            
    bf('porch:e',           jul12(37),   'porch:w',          'porch:e'),
    bf('porch:w',           jul12(41),   'porch:e',          'livingroom:n'),

    bf('diningroom_in',     r'C:\img\vol1\20010405\dscf0015.jpg',   'diningroom_out',   'diningroom_in'),
    bf('diningroom_out',    r'C:\img\vol1\20010508a\dscf0016.jpg',  'diningroom_in',    'hall:e'),

    nesw('front43',
        ni = nov4(17),
        ei = nov4(18),      e = 'allerton_hawthorne:e',
        si = nov10(381),    s = 'hall:s',
        wi = nov4(16),      w = 'markliesl:w'
    ),

    nesw('markliesl',
        ni = nov4(20),
        ei = nov4(21),  e = 'front43:e',
        si = nov4(22),
        wi = nov4(19),  w = 'allerton:0f'
    ),

    tunnel('allerton', [
        nov4((23, 24)),
        nov4((25, 26)),
        nov4((27, 28))
        ], 'markliesl:e', 'walnut_irving:n'
    ),

    nesw('walnut_irving',
        ni = nov4(29),
        ei = nov4(30),
        si = nov4(31),  s = 'allerton:2b',
        wi = nov4(32),  w = 'walnut:0f'
    ),

    tunnel('walnut', [
        (nov4(33), nov4(35)),
        (nov4(37), nov4(38)),
        (nov4(39), nov4(40))
        ], 'walnut_irving:e', 'walnut_cypress:w'
    ),

    nesw('walnut_cypress',
        ni = nov4(42),  n = 'cypress_milton:n',
        ei = nov4(43),  e = 'walnut:2b',
        si = nov4(44),
        wi = nov4(41),  w = 'walnut_cypress_walk'
    ),

    lfr('walnut_cypress_walk', nov4(47),      'walnut_cypress:s', 'walnut_cushing:w', 'walnut_cypress:n'),

    nesw('walnut_cushing',
        ni = nov4(52),  n = 'cushing:n',
        ei = nov4(50),  e = 'walnut_cypress:e',
        si = nov4(49),
        wi = nov4(51),
    ),

    bf('cushing:n', nov4(53), 'cushing:s', 'milton_cushing:e'),
    bf('cushing:s', nov4(54), 'cushing:n', 'walnut_cushing:s'),

    bf('milton_cushing:e', nov4(55), 'milton_cushing:s', 'milton:e'),
    bf('milton_cushing:s', nov4(56), 'milton_cushing:e', 'cushing:s'),

    nesw('milton',
        ni = nov4(58),
        ei = nov4(59),  e = 'cypress_milton:e',
        si = nov4(60),
        wi = nov4(57),  w = 'milton_cushing:s'
    ),

    nesw('cypress_milton',
        ni = nov4(63),  n = 'rt9_cypress:n',
        ei = nov4(14),
        si = nov4(61),  s = 'walnut_cypress:s',
        wi = nov4(57),  w = 'milton_cushing:s'
    ),

    nesw('rt9_cypress',
        ni = nov4(64),  n = 'cypress_brington:n',
        ei = nov4(65), 
        si = nov4(66),  s = 'cypress_milton:s',
        wi = nov4(67)
    ),

    nesw('cypress_brington',
        ni = nov4(69),  n = 'cypress_bridge:n',
        si = nov4(68),  s = 'rt9_cypress:s'
    ),

    nesw('cypress_bridge',
        ni = nov4(73),  n = 'cypress_tappan:n',
        ei = nov4(72), 
        si = nov4(71),  s = 'cypress_brington:s',
        wi = nov4(70)
    ),

    nesw('cypress_tappan',
        ni = nov4(74),  n = 'cypress_davis:n',
        si = nov4(75),  s = 'cypress_bridge:s',
        wi = nov4(76)
    ),
    
    nesw('cypress_davis',
        ni = nov4(77),  n = 'cypress_stanton:n',
        ei = nov4(78), 
        si = nov4(79),  s = 'cypress_tappan:s',
        wi = nov4(80),
    ),

    nesw('cypress_stanton',
        ni = nov4(81),  n = 'cypress_cvs:n',
        si = nov4(82),  s = 'cypress_davis:s',
    ),

    nesw('cypress_cvs',
        ni = nov4(84),  n = 'wash_cypress:s',
        si = nov4(85),  s = 'cypress_stanton:s',
        wi = nov4(83),  w = 'inside_cypress_cvs',
    ),

    lr('inside_cypress_cvs', nov4(86), 'cypress_cvs:s', 'cypress_cvs:s'),

    # North and south take a little turn at this point...

    nesw('wash_cypress',
        ni = nov4(89),  n = 'wash_to_beacon:0f',
        si = nov4(87),  s = 'libraryrenovation:0',
        wi = nov4(88),  w = 'cypress_cvs:s',
    ),

    tunneloneway('libraryrenovation', libimg(range(1,9)), 'wash_cypress:s', 'wash_cypress:s'),
                 
    tunnel('wash_to_beacon', [
        (nov4(90), nov4(91)),
        (nov4(92), nov4(93)),
        (nov4(94), nov4(95)),
        (nov4(96), nov4(98)),   # 97 is east on park st.
        (nov4(99), nov4(101)),  # 100 is east on crescent
        (nov4(102), nov4(103)),
        (nov4(104), nov4(105)),
        (nov4(106), nov4(107)),
        (nov4(108), nov4(110)), # 109 is east looking at the fire station.
        ], 'wash_cypress:s', 'beacon_wash:n'
    ),

    nesw('beacon_wash',
        ni = nov4(111),     n = 'wash_t:n',
        ei = nov4(112),
        si = nov4(113),     s = 'wash_to_beacon:8b',
        wi = nov4(114),
    ),

    nesw('wash_t',
        ni = nov4(122),
        ei = nov4(123),
        si = nov4(124),     s = 'beacon_wash:s',
        wi = nov4(125),     w = 'wash_wait_for_t:0',
    ),

    lfffr('wash_wait_for_t',
        nov4(range(118, 122) + range(126, 137)),
        'wash_t:s', 'wash_t_arrive_0', 'wash_t:n'
    ),

    lfr('wash_t_arrive_0', nov4(137), 'wash_t:s', 'wash_t_arrive_1', 'wash_t:n'),
    lfr('wash_t_arrive_1', nov4(138), 'wash_t:s', 'wash_t_arrive_2', 'wash_t:n'),
    lfr('wash_t_arrive_2', nov4(139), 'wash_t:w', 't_on_beacon_inbound:0', 'wash_t:e'),

    tunneloneway('t_on_beacon_inbound', nov4(range(140, 173)), 'wash_t:s', 'arlington_t:0'),

    tunneloneway('arlington_t', nov4((173, 175, 176, 177)), 'arlington_t:0', 'arlington_wait_for_t'),

    bf('arlington_wait_for_t', nov4(179), 'arlington_wait_for_t', 'arlington_wait_for_t:0'),
    
    lfffr('arlington_wait_for_t',
        nov4(range(178, 182)) +
            nov11((477, 478, 481, 482, 483, 484)),
        'arlington_wait_for_t', 'arlington_d_arrive', 'arlington_wait_for_t'
    ),

    lfr('arlington_d_arrive', nov4(182), 'arlington_wait_for_t', 't_on_beacon_outbound:0', 'arlington_wait_for_t'),
    
    tunneloneway('t_on_beacon_outbound', nov4(range(183, 212)), 't_on_beacon_outbound:0', 'broovill_t:n'),

    nesw('broovill_t',
        ni = nov4(214), 
        ei = nov4(215),     e = 'broovill_t2:e',
        si = nov4(212),
        wi = nov4(213),
    ),

    nesw('broovill_t2',
        ni = nov11(487),
        ei = nov4(219),
        si = nov4(216),     s = 'brooklineplace:0f',
        wi = nov4(220),     w = 'broovill_t:w',
    ),

    tunnel('brooklineplace', [
        nov4((221, 222)),
        nov4((224, 223)),
        nov4((225, 226))
        ], 'broovill_t2:w', 'videoplus:s'
    ),

    nesw('videoplus',
        ni = nov4(228),     n = 'brooklineplace:2b',
        ei = nov4(229),     e = 'rt9_brookline:0',
        si = nov4(230),     s = 'rt9_brooklineplace:s',
        wi = nov4(227),
    ),

    nesw('rt9_brooklineplace',
        ni = nov4(233),     n = 'videoplus:n',
        ei = nov4(234),     e = 'rt9_brookline:0',
        si = nov4(231),
        wi = nov4(232),
    ),

    lfffr('rt9_brookline',
        nov4(range(235, 240)), 'rt9_brookline:0', 'rt9_brookline_green', 'rt9_brooklineplace:w'
    ),

    bf('rt9_brookline_green', nov4(240), 'rt9_brooklineplace:w', 'rt9_brookline2:s'),

    nesw('rt9_brookline2',
        ni = nov4(245),     n = 'rt9_brooklineplace:w',
        ei = nov4(246),
        si = nov4(242),     s = 'rt9_brookline2_wait:0',
        wi = nov4(244),
    ),
    
    lfffr('rt9_brookline2_wait',
        nov4((241, 242, 243) * 2), 'rt9_brookline2:e', 'rt9_brookline2_green', 'rt9_brookline2:w'
    ),

    lfr('rt9_brookline2_green', nov4(247), 'rt9_brookline2:e', 'rt9_brookline3:s', 'rt9_brookline2:w'),

    nesw('rt9_brookline3',
        ni = nov4(248),     n = 'rt9_brookline2:n',
        ei = nov4(249),     e = 'rt9_pond:e',
        si = nov4(251),     s = 'brookhouse:0f',
        wi = nov4(250),
    ),

    tunnel('brookhouse', [
        nov4((253, 252)),
        nov4((254, 255)),
        nov4((256, 257))
        ], 'rt9_brookline3:n', 'pond_brookhouse:e'
    ),

    nesw('pond_brookhouse',
        ni = nov11(409),    n = 'pondtort9:0f',
        ei = nov11(410),
        si = nov4(258),     s = 'pondtoallerton:0f',
        wi = nov4(259),     w = 'brookhouse:2b',
    ),

    tunnel('pondtoallerton', [nov4((260, 261))], 'pond_brookhouse:n', 'pond_allerton:s'),

    nesw('pond_allerton',
        ni = nov4(264),     n = 'pondtoallerton:0b',
        ei = nov4(265),
        si = nov4(262),
        wi = nov4(263),     w = 'allerton_hawthorne:w',
    ),

    nesw('allerton_hawthorne',
        ni = nov10(375),
        ei = nov4(267),     e = 'pond_allerton:e',
        si = nov4(268),     s = 'hawthorne_driveway:s',
        wi = nov4(266),     w = 'front43:w',
    ),

    nesw('hawthorne_driveway',
        ni = nov10(370),    n = 'allerton_hawthorne:n',
        ei = nov10(368),
        si = nov10(369),
        wi = nov10(371),
    ),

    ## Walk to route 9 E trolley.

    tunnel('pondtort9', [nov11((412, 413))], 'pond_brookhouse:s', 'rt9_pond:n'),

    nesw('rt9_pond',
        ni = nov11(414),
        ei = nov11(417),    e = 'rt9underbridge:0f',
        si = nov11(415),    s = 'pondtort9:0b',
        wi = nov11(416),    w = 'rt9_brookline3:w',
    ),

    tunnel('rt9underbridge', [nov11((418, 419))], 'rt9_pond:w', 'rt9_shuntington:e'),

    nesw('rt9_shuntington',
        ni = nov11(423),
        ei = nov11(420),    e = 'rt9_shuntington2:s',
        si = nov11(425),    
        wi = nov11(421),    w = 'rt9underbridge:0b',
    ),

    nesw('rt9_shuntington2',
        ni = nov11(428),
        si = nov11(426),    s = 'shuntington_wait:0',
        wi = nov11(427),    w = 'rt9_shuntington:w',
    ),

    lfffr('shuntington_wait',
        nov11((426, 429, 430) * 2), 'rt9_shuntington:n', 'shuntington_arrive1', 'rt9_shuntington:s'
    ),

    lfr('shuntington_arrive1', nov11(431), 'rt9_shuntington2:n', 'shuntington_arrive2', 'rt9_shuntington2:w'),
    lfr('shuntington_arrive2', nov11(432), 'rt9_shuntington2:s', 't_on_rt9_inbound:0', 'rt9_shuntington2:n'),

    tunneloneway('t_on_rt9_inbound',
        nov11(range(433, 476)), 'shuntington_wait:0', 'arlington_t:0'
    ),
]

class StereoMenu(MenuNode):
    def __init__(self):
        MenuNode.__init__(
            self, 'menu_stereo', [
                ('Play: Stand',             'Stand'),
                ('Play: Head Over Feet',    'Head Over Feet'),
                ('Stop',                    '')
                ]
        )

    def doChoice(self, song):
        if song == '':
            pygame.mixer.music.stop()
        else:            
            try:
                pygame.mixer.music.load('music\\' + song + '.wav')
            except:
                try:
                    pygame.mixer.music.load('music\\' + song + '.mp3')
                except:
                    pass
            pygame.mixer.music.play()

smenu = StereoMenu()
        
# Main flow for Nat's world

def main():
    import getopt
    import sys

    def usage():
        print "Options:"
        print "\t-d\tDebug mode"
        print "\t-f\tFull screen"
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "df")
    except getopt.GetoptError:
        # print help information and exit:
        usage()
        return

    debug = 0
    fullscreen = 0
    
    for o, a in opts:
        if o == "-d":
            debug = 1
        if o == "-f":
            fullscreen = 1

    if debug:
        print '%d nodes' % (Node.countNodes())

    if debug:
        Node.setJumpNode('t', 'wash_t:n')
        Node.setJumpNode('a', 'arlington_t:0')
        Node.setJumpNode('u', 'broovill_t:n')
        Node.setJumpNode('0', 'hall:w')
    
    nw = WorldApp.WorldApp()
    
    nw.setTitle("Nat's World")
    nw.setScreenSize((800, 600))
    nw.setFullScreen(fullscreen)
    nw.setDebug(debug)
    nw.setHomeNode('hall:w')

    nw.setCreditRoll([
        ("Nat's World", (255,50,50)),
        "Conception: Ned",
        "Photography: Ned & Max",
        "Programming: Ned",
        "Direction: Nat",
        "Walking: Nat, Max & Ned",
        "Set Design: Sue",
        "Key Grip: Ben",
        "Catering: Sue",
        "Transportation: MBTA",
        "Music: R.E.M., Alanis Morrisette & Max"
    ])
    #nw.setCreditSong('music\\maxneverhood.wav')
    
    nw.main()

if __name__ == '__main__': main()

## Morgue:
##outside_north.file = (r'C:\img\vol1\20010317\dscf0004')
##high_43_west.file = (r'C:\img\vol1\20010318\dscf0002')
##high_43_east.file = (r'C:\img\vol1\20010318\dscf0001')
##high_43_south.file = (r'C:\img\vol1\20010318\dscf0004')
##high_st_north.file = (r'C:\img\vol1\20010318\dscf0005')
##high_walnut_red.file = (r'C:\img\vol1\20010318\dscf0008')
##high_walnut_green.file = (r'C:\img\vol1\20010318\dscf0007')
