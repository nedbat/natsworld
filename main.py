"""
Nat's World
Ned Batchelder, 11/2001
"""
import WorldApp
from Node import *
from NodeUtils import *
from Menu import *

img = 'Q:\\img\\'

mar17c =    ImgShortcut(img+r'vol1\20010317c\dscf%04d.jpg')
apr7a =     ImgShortcut(img+r'vol1\20010407a\dscf%04d.jpg')
apr7b =     ImgShortcut(img+r'vol1\20010407b\dscf%04d.jpg')
apr7c =     ImgShortcut(img+r'vol1\20010407c\dscf%04d.jpg')
apr16a =    ImgShortcut(img+r'vol1\20010416a\dscf%04d.jpg')
may27a =    ImgShortcut(img+r'vol1\20010527a\dscf%04d.jpg')
jul03 =     ImgShortcut(img+r'vol2\20010703\dscf%04d.jpg')
jul04 =     ImgShortcut(img+r'vol2\20010704\dscf%04d.jpg')
jul06 =     ImgShortcut(img+r'vol2\20010706\dscf%04d.jpg')
jul12 =     ImgShortcut(img+r'vol2\20010712\dscf%04d.jpg')
aug5 =      ImgShortcut(img+r'vol2\20010805\dscf%04d.jpg')
nov4 =      ImgShortcut(img+r'vol3\20011104\dscf%04d.jpg')
nov10 =     ImgShortcut(img+r'vol3\20011110\dscf%04d.jpg')
nov11 =     ImgShortcut(img+r'vol3\20011111\dscf%04d.jpg')
nov12 =     ImgShortcut(img+r'vol3\20011112\dscf%04d.jpg')
libimg =    ImgShortcut(img+r'libraryweb\library%d.jpg')
nov16 =     ImgShortcut(img+r'vol3\20011116\dscf%04d.jpg')
nov17 =     ImgShortcut(img+r'vol3\20011117\dscf%04d.jpg')
nov23 =     ImgShortcut(img+r'vol3\20011123\dscf%04d.jpg')
nov30 =     ImgShortcut(img+r'vol3\20011130\dscf%04d.jpg')
edited =    ImgShortcut(img+r'edited\dscf%04d.jpg')
dec8 =      ImgShortcut(img+r'vol3\20011208\dscf%04d.jpg')
dec16 =     ImgShortcut(img+r'vol3\20011216\dscf%04d.jpg')
jan19 =     ImgShortcut(img+r'vol3\20020119\dscf%04d.jpg')
feb23 =     ImgShortcut(img+r'vol3\20020223\dscf%04d.jpg')
feb24 =     ImgShortcut(img+r'vol3\20020224\dscf%04d.jpg')
mar9 =      ImgShortcut(img+r'vol3\20020309\dscf%04d.jpg')
jun8 =      ImgShortcut(img+r'vol3\20020608\dscf%04d.jpg')
jul7_2 =    ImgShortcut(img+r'vol3\20020707\dscf%04d.jpg')
jul7b =     ImgShortcut(img+r'vol3\20020707b\dscf%04d.jpg')
aug12 =     ImgShortcut(img+r'vol5\20030812\dscf%04d.jpg')
aug13 =     ImgShortcut(img+r'vol5\20030813\dscf%04d.jpg')
aug14 =     ImgShortcut(img+r'vol5\20030814\dscf%04d.jpg')

sci =       ImgShortcut(img+r'vol6\20040306\dscf%04d.jpg')

feb26 =     ImgShortcut(img+r'vol7\2005_02_26\IMG_%04d.jpg')
mar05 =     ImgShortcut(img+r'vol7\2005_03_05\IMG_%04d.jpg')

mar11 =     ImgShortcut(img+r'vol12\2006_03_11\IMG_%04d.jpg')

# Nodes for Nat's world

#
# Inside the house: first floor
#

nesw('hall',
    ni = jul12(28),     n = 'front43:n',
    ei = nov12(501),    e = 'livingroom:e',
    si = dec8(95),      s = 'playroom:s',
    wi = jul12(30),     w = 'diningroom:w',
)

nesw('playroom',
    ni = dec8(93),      n = 'hall:n',
    ei = dec8(97),
    si = dec8(91),
    wi = dec8(92)
)

findNode('playroom:e').actions += [((.31, .46, .235, .235), 'playroom_white_natworld')]
findNode('playroom:e').actions += [((.69, .56, .165, .165), 'playroom_black_natworld')]
NatWorldNode('playroom_white_natworld', (.31, .46, .235, .235))
NatWorldNode('playroom_black_natworld', (.69, .56, .165, .165))

nesw('livingroom',
    ni = nov12(497),
    ei = nov12(494),
    si = nov12(495),    s = 'stereo_s',
    wi = nov12(496),    w = 'hall:w'
)

lr('stereo_s', nov12(498),  'stereo_e',                     'livingroom:w')
lfr('stereo_e', nov12(500), 'livingroom:n', 'porch:e',      'stereo_s')

findNode('stereo_s').actions += [((.25, .1, .5, .9), 'menu_stereo')]

SongMenu('menu_stereo', [
    ('Play: Stand',             'Stand'),
    ('Play: Eat For Two',       'Eat For Two'),
    ('Play: Sunny Came Home',   'Sunny Came Home'),
    ('Play: Head Over Feet',    'Head Over Feet'),
    ('Stop',                    '')
    ])

nesw('porch',
     ei = jul12(37),
     wi = jul12(41),    w = 'livingroom:n'
)

nesw('diningroom',
     wi = img+r'vol1\20010405\dscf0015.jpg',
     ei = img+r'vol1\20010508a\dscf0016.jpg',    e = 'hall:e'
)

#
# Outside the house
#

nesw('front43',
    ni = nov4(17),
    ei = nov4(18),      e = 'allerton_hawthorne:e',
    si = nov10(381),    s = 'hall:s',
    wi = nov4(16),      w = 'markliesl:w'
)

nesw('allerton_hawthorne',
    ni = nov10(375),
    ei = nov4(267),     e = 'pond_allerton:e',
    si = nov4(268),     s = 'hawthorne_driveway:s',
    wi = nov4(266),     w = 'front43:w',
)

nesw('hawthorne_driveway',
    ni = nov10(370),    n = 'allerton_hawthorne:n',
    ei = nov10(368),
    si = nov10(369),
    wi = nov10(371),    w = 'driveway:w'
)

nesw('driveway',
    ni = nov10(350),    # into the basement
    ei = nov10(349),    e = 'hawthorne_driveway:e',
    si = nov10(346),    # into the yard
    wi = apr16a(2),     w = 'menu_drive'
)

MenuNode('menu_drive', [
    ('Passover',        'passover:0'),
    ('Home Depot',      'homedepot:0'),
    ('Connecticut',     'connecticut_drive:0'),
    ('Little Compton',  'littlecompton:0'),
    ('Airport',         'airport:0'),
    ('Cape Cod',        'capecod:0'),
    ('Candlewood Drive', 'candlewooddrive_driveend:n'),
    ('Newton Library',  'newtonlibrary_start:e')
    ])

MenuNode('menu_home', [
    ('Home',        'driveway:w')
    ])

photoalbum('passover',
    apr7a(range(1, 101)) +
    apr7b(range(1, 33)) +
    apr7c(range(1, 85)),
    'driveway:w'
)

photoalbum('homedepot',
    aug5((1, 2, 3, 5)),
    'driveway:w'
)

photoalbum('littlecompton',
    aug5(range(6, 131)),
    'driveway:w'
)

photoalbum('airport',
    mar17c(range(1,53)),
    'driveway:w'
)

photoalbum('capecod',
    jul03(range(1,22)) +
    jul04(range(1,37)) +
    jul06(range(1,51)),
    'driveway:w'
)

#
# Outside on Pill Hill
#

nesw('markliesl',
    ni = nov4(20),
    ei = nov4(21),  e = 'front43:e',
    si = nov4(22),
    wi = nov4(19),  w = 'high_allerton:w'
)

nesw('high_allerton',
    ni = nov23(16), n = 'high0:n',
    ei = nov4(24),  e = 'markliesl:e',
    si = nov23(18),
    wi = nov4(23),  w = 'allerton:0f',
)

# Down High Street.

nesw('high0',
    ni = nov23(20), n = 'high_acron:n',
    si = nov23(21), s = 'high_allerton:s'
)

nesw('high_acron',
    ni = nov23(22), n = 'high1:n',
    ei = nov23(23),
    si = nov23(25), s = 'high0:s',
    wi = nov23(24)
)

nesw('high1',
    ni = nov23(26), n = 'high_walnut:n',
    si = nov23(27), s = 'high_acron:s'
)

nesw('high_walnut',
    ni = nov23(29), n = 'rt9_high:n',
    ei = nov23(36),
    si = nov23(34), s = 'high1:s',
    wi = nov23(33), w = 'walnut_irving:w'
)

nesw('rt9_high',
    ni = nov23(37), n = 'rt9_high_wait:0',
    ei = nov23(41),
    si = nov23(42), s = 'high_walnut:s',
    wi = nov23(43), w = 'rt9_cypress:w'
)

lfffr('rt9_high_wait',
    nov23([38,39]+range(37, 41)*2), 'rt9_high:w', 'rt9_high_green', 'rt9_high:e'
)

lfr('rt9_high_green',
    nov23(44), 'rt9_high:w', 'rt9_high_2:n', 'rt9_high:e'
)

# Brookline Village

nesw('rt9_high_2',
    ni = nov23(46), n = 'wash_station:n',
    si = nov23(45), s = 'rt9_high:s'
)

nesw('wash_station',
    ni = jun8(939), n = 'wash0:n',
    ei = feb26(230), e = 'station_wash:e',
    si = jun8(941), s = 'rt9_high_2:s',
    wi = feb26(316),
)

nesw('wash0',
    ni = jun8(945), n = 'wash_davis:0',
    ei = jun8(942),
    si = jun8(943), s = 'wash_station:s',
    wi = jun8(944)
)

clump('wash_davis', [
    (jun8(947),),
    (jun8(948), 'oldcvs:n'),
    (jun8(949),),
    (jun8(951), 'wash0:s'),
    (jun8(946),)    # down Davis.
])

nesw('oldcvs',
    ni = jun8(954), n = 'wash_holden:n',
    ei = jun8(955), e = 'oldcvs_door:e',
    si = jun8(952), s = 'wash_davis:3',
    wi = jun8(953)
)

nesw('oldcvs_door',
    ei = jun8(956),
    ni = jun8(957),
    si = jun8(958),
    wi = jun8(959), w = 'oldcvs:w'
)

nesw('wash_holden',
    ni = jun8(960), n = 'wash_townhall:n',
    wi = jun8(961),
    si = jun8(962), s = 'oldcvs:s',
    ei = jun8(963)
)

nesw('wash_townhall',
    ni = jun8(964), n = 'wash_thayer:n',
    ei = jun8(965),
    si = jun8(966), s = 'wash_holden:s',
    wi = jun8(967)
)

nesw('wash_thayer',
    wi = jun8(968),
    ni = jun8(969), n = 'libdrive:0',
    ei = jun8(970),
    si = jun8(971), s = 'wash_townhall:s'
)

clump('libdrive', [
    (jun8(972), 'mainlib:n'),
    (jun8(973),),
    (jun8(974), 'libgarage1:e'),
    (jun8(975), 'wash_thayer:s'),
    (jun8(976),),
])

nesw('libgarage1',
    ei = jun8(978), e = 'libgarage2:e',
    ni = jun8(979),
    wi = jun8(980), w = 'libdrive:4',
    si = jun8(981)
)

nesw('libgarage2',
    ni = jun8(982), n = 'libraryrenovation:10',
    ei = jun8(984),
    wi = jun8(985), w = 'libgarage1:w'
)

nesw('mainlib',
    ei = jun8(986),
    si = jun8(987), s = 'libdrive:3',
    wi = jun8(988),
    ni = jun8(989), n = 'wash_school:n'
)

nesw('wash_school',
    ni = jun8(990), n = 'wash_cypress:n',
    ei = jun8(991), e = 'school1:e',
    si = jun8(992), s = 'mainlib:s',
    wi = jun8(993)
)

nesw('school1',
    wi = jun8(996), w = 'wash_school:w',
    ni = jun8(997),
    si = jun8(995),
    ei = jun8(994), e = 'schoolbridgeup:0'
)

tunneloneway('schoolbridgeup',
    jun8((998, 999)), 'school1:e', 'schoolbridgenorth:s'
)

nesw('schoolbridgenorth',
    si = jun8(1000), s = 'schoolbridgemiddle:s',
    ni = jun8(1001)
)

nesw('schoolbridgemiddle',
    si = jun8(1002), s = 'schoolbridgesouth:s',
    wi = jun8(1003),
    ni = jun8(1004), n = 'schoolbridgenorth:n',
    ei = jun8(1005)
)

nesw('schoolbridgesouth',
    si = jun8(1006), s = 'schoolbridgedown:0',
    ni = jun8(1007), n = 'schoolbridgemiddle:n'
)

tunneloneway('schoolbridgedown',
    jun8((1008, 1009)), 'schoolbridgesouth:n', 'school1:e'
)

# Walnut to Cypress

tunnel('allerton', [
    nov4((25, 26)),
    nov4((27, 28))
    ], 'high_allerton:e', 'walnut_irving:n'
)

nesw('walnut_irving',
    ni = nov4(29),
    ei = nov4(30),  e = 'high_walnut:e',
    si = nov4(31),  s = 'allerton:1b',
    wi = nov4(32),  w = 'walnut:0f'
)

tunnel('walnut', [
    (nov4(33), nov4(35)),
    (nov4(37), nov4(38)),
    (nov4(39), nov4(40))
    ], 'walnut_irving:e', 'walnut_cypress:w'
)

nesw('walnut_cypress',
    ni = nov4(42),  n = 'cypress_walmilt:n',
    ei = nov4(43),  e = 'walnut:2b',
    si = nov4(44),
    wi = nov4(41),  w = 'walnut_cypress_green'
)

lfr('walnut_cypress_green', nov4(47), 'walnut_cypress:s', 'walnut_cushing:w', 'walnut_cypress:n')

nesw('cypress_walmilt',
    ni = nov16(567),    n = 'cypress_milton:n',
    si = nov16(568),    s = 'walnut_cypress:s',
)

nesw('walnut_cushing',
    ni = nov4(52),      n = 'cushing:n',
    ei = nov16(559),    e = 'walnut_cypress:e',
    si = nov4(49),
    wi = nov16(560),    w = 'walnut_kennard:w',
)

nesw('cushing',
    ni = nov4(53),  n = 'milton_cushing:n',
    si = nov4(54),  s = 'walnut_cushing:s'
)

nesw('milton_cushing',
    ni = nov16(561),
    ei = nov16(562),    e = 'milton:e',
    si = nov16(563),    s = 'cushing:s',
    wi = nov16(564),
)

nesw('milton',
    ni = nov4(58),
    ei = nov4(59),  e = 'cypress_milton:e',
    si = nov4(60),  s = 'yellowhousephotos:0',
    wi = nov4(57),  w = 'milton_cushing:w'
)

nesw('cypress_milton',
    ni = nov4(63),  n = 'rt9_cypress:n',
    ei = nov16(566),
    si = nov4(61),  s = 'cypress_walmilt:s',
    wi = nov4(62),  w = 'milton:w'
)

photoalbum('yellowhousephotos',
    jan19(range(400, 404)),
    'milton:s'
)

#
# Brookline Village - Cypress to Washington
#

nesw('rt9_cypress',
    ni = nov4(64),  n = 'cypress_brington:n',
    ei = nov4(65),  e = 'rt9_high:e',
    si = nov4(66),  s = 'cypress_milton:s',
    wi = nov4(67)
)

nesw('cypress_brington',
    ni = nov4(69),  n = 'cypress_bridge:n',
    si = nov4(68),  s = 'rt9_cypress:s'
)

nesw('cypress_bridge',
    ni = nov4(73),  n = 'cypress_tappan:n',
    ei = nov4(72),
    si = nov4(71),  s = 'cypress_brington:s',
    wi = nov4(70)
)

nesw('cypress_tappan',
    ni = nov4(74),  n = 'cypress_davis:n',
    si = nov4(75),  s = 'cypress_bridge:s',
    wi = nov4(76)
)

nesw('cypress_davis',
    ni = nov4(77),  n = 'cypress_stanton:n',
    ei = nov4(78),
    si = nov4(79),  s = 'cypress_tappan:s',
    wi = nov4(80),
)

nesw('cypress_stanton',
    ni = nov4(81),  n = 'cypress_cvs:n',
    si = nov4(82),  s = 'cypress_davis:s',
)

nesw('cypress_cvs',
    ni = nov4(84),  n = 'wash_cypress:s',
    si = nov4(85),  s = 'cypress_stanton:s',
    wi = nov4(83),  w = 'inside_cypress_cvs',
)

lr('inside_cypress_cvs', nov4(86), 'cypress_cvs:s', 'cypress_cvs:s')

#
# Washington Street
# North and south take a little turn at this point...
#

nesw('wash_cypress',
    ni = nov4(89),  n = 'wash_to_beacon:0f',
    si = nov4(87),  s = 'wash_school:s',
    wi = nov4(88),  w = 'cypress_cvs:s',
)

photoalbum('libraryrenovation',
    libimg(range(1, 9)) +
    nov30(range(48, 82)),
    'wash_cypress:s'
)


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
)

nesw('beacon_wash',
    ni = nov4(111),     n = 'wash_t:n',
    ei = nov4(112),
    si = nov4(113),     s = 'wash_to_beacon:8b',
    wi = nov4(114),
)

nesw('wash_t',
    ni = nov4(122),
    ei = nov4(123),
    si = nov4(124),     s = 'beacon_wash:s',
    wi = nov4(125),     w = 'wash_wait_for_t:0',
)

lfffr('wash_wait_for_t',
    nov4(range(118, 122) + range(126, 137)),
    'wash_t:s', 'wash_t_arrive_0', 'wash_t:n'
)

lfr('wash_t_arrive_0', nov4(137), 'wash_t:s', 'wash_t_arrive_1', 'wash_t:n')
lfr('wash_t_arrive_1', nov4(138), 'wash_t:s', 'wash_t_arrive_2', 'wash_t:n')
lfr('wash_t_arrive_2', nov4(139), 'wash_t:w', 't_on_beacon_inbound:0', 'wash_t:e')

#
# T: C inbound
#

tunneloneway('t_on_beacon_inbound', nov4(range(140, 173)), 'wash_t:s', 'arlington_t:0')

#
# Underground
#

tunneloneway('arlington_t', nov4((173, 175, 176, 177)), 'arlington_t:0', 'arlington_wait_for_t')

bf('arlington_wait_for_t', nov4(179), 'arlington_wait_for_t', 'arlington_wait_for_t:0')

lfffr('arlington_wait_for_t',
    nov4(range(178, 182)) +
        nov11((477, 478, 481, 482, 483, 484)),
    'arlington_wait_for_t', 'arlington_d_arrive', 'arlington_wait_for_t'
)

lfr('arlington_d_arrive', nov4(182), 'arlington_wait_for_t', 't_on_beacon_outbound:0', 'arlington_wait_for_t')

#
# T: D outbound
#

tunneloneway('t_on_beacon_outbound', nov4(range(183, 212)), 't_on_beacon_outbound:0', 'broovill_t:n')

#
# Brookline Village: T to Pond
#

nesw('broovill_t',
    ni = nov4(214),
    ei = nov4(215),     e = 'broovill_t2:e',
    si = nov4(212),
    wi = nov4(213),
)

nesw('broovill_t2',
    ni = nov11(487),     n = 'station_b:n',
    ei = nov4(219),
    si = nov4(216),     s = 'brooklineplace:0f',
    wi = nov4(220),     w = 'broovill_t:w',
)

tunnel('brooklineplace', [
    nov4((221, 222)),
    nov4((224, 223)),
    nov4((225, 226))
    ], 'broovill_t2:n', 'videoplus:s'
)

nesw('videoplus',
    ni = nov4(228),     n = 'brooklineplace:2b',
    ei = nov4(229),     e = 'rt9_brookline:0',
    si = nov4(230),     s = 'rt9_brooklineplace:s',
    wi = nov4(227),
)

nesw('rt9_brooklineplace',
    ni = nov4(233),     n = 'videoplus:n',
    ei = nov4(234),     e = 'rt9_brookline:0',
    si = nov4(231),
    wi = nov4(232),
)

lfffr('rt9_brookline',
    nov4(range(235, 240)), 'rt9_brookline:0', 'rt9_brookline_green', 'rt9_brooklineplace:w'
)

bf('rt9_brookline_green', nov4(240), 'rt9_brooklineplace:w', 'rt9_brookline2:s')

nesw('rt9_brookline2',
    ni = nov4(245),     n = 'rt9_brooklineplace:w',
    ei = nov4(246),
    si = nov4(242),     s = 'rt9_brookline2_wait:0',
    wi = nov4(244),
)

lfffr('rt9_brookline2_wait',
    nov4((241, 242, 243) * 2), 'rt9_brookline2:e', 'rt9_brookline2_green', 'rt9_brookline2:w'
)

lfr('rt9_brookline2_green', nov4(247), 'rt9_brookline2:e', 'rt9_brookline3:s', 'rt9_brookline2:w')

nesw('rt9_brookline3',
    ni = nov4(248),     n = 'rt9_brookline2:n',
    ei = nov4(249),     e = 'rt9_pond:e',
    si = nov4(251),     s = 'brookhouse:0f',
    wi = nov4(250),
)

#
# Brook House and Pond
#

tunnel('brookhouse', [
    nov4((253, 252)),
    nov4((254, 255)),
    nov4((256, 257))
    ], 'rt9_brookline3:n', 'pond_brookhouse:e'
)

nesw('pond_brookhouse',
    ni = nov11(409),    n = 'pondtort9:0f',
    ei = nov11(410),
    si = nov4(258),     s = 'pondtoallerton:0f',
    wi = nov4(259),     w = 'brookhouse:2b',
)

tunnel('pondtoallerton', [nov4((260, 261))], 'pond_brookhouse:n', 'pond_allerton:s')

nesw('pond_allerton',
    ni = nov4(264),     n = 'pondtoallerton:0b',
    ei = nov4(265),
    si = nov4(262),
    wi = nov4(263),     w = 'allerton_hawthorne:w',
)

#
# Walk to route 9 E trolley.
#

tunnel('pondtort9', [nov11((412, 413))], 'pond_brookhouse:s', 'rt9_pond:n')

nesw('rt9_pond',
    ni = nov11(414),
    ei = nov11(417),    e = 'rt9underbridge:0f',
    si = nov11(415),    s = 'pondtort9:0b',
    wi = nov11(416),    w = 'rt9_brookline3:w',
)

tunnel('rt9underbridge', [nov11((418, 419))], 'rt9_pond:w', 'rt9_shuntington:e')

nesw('rt9_shuntington',
    ni = nov11(423),
    ei = nov11(420),    e = 'rt9_shuntington2:s',
    si = nov11(425),
    wi = nov11(421),    w = 'rt9underbridge:0b',
)

nesw('rt9_shuntington2',
    ni = nov11(428),
    si = nov11(426),    s = 'shuntington_wait:0',
    wi = nov11(427),    w = 'rt9_shuntington:w',
)

lfffr('shuntington_wait',
    nov11((426, 429, 430) * 2), 'rt9_shuntington:n', 'shuntington_arrive1', 'rt9_shuntington:s'
)

lfr('shuntington_arrive1', nov11(431), 'rt9_shuntington2:n', 'shuntington_arrive2', 'rt9_shuntington2:w')
lfr('shuntington_arrive2', nov11(432), 'rt9_shuntington2:s', 't_on_rt9_inbound:0', 'rt9_shuntington2:n')

tunneloneway('t_on_rt9_inbound',
    nov11(range(433, 476)), 'shuntington_wait:0', 'arlington_t:0'
)

#
# Lincoln School
#

nesw('walnut_kennard',
    ni = nov16(556),    n = 'kennard:n',
    ei = nov16(557),    e = 'walnut_cushing:e',
    si = nov16(558),
    wi = nov16(555),    w = 'walnut_kennard2:w',
)

nesw('walnut_arch',
    ni = nov16(504),    n = 'archpath:n',
    ei = nov16(505),    e = 'walnut_kennard2:e',
    si = nov16(506),
    wi = nov16(503),	w = 'drivetobaker:0',
)

nesw('archpath',
    ni = nov16(507),    n = 'lincoln_south:n',
    si = nov16(508),    s = 'walnut_arch:s',
)

nesw('lincoln_south',
    ni = nov16(509),    n = 'lincoln_east:n',
    ei = nov16(510),
    si = nov16(511),    s = 'archpath:s',
    wi = nov16(512),    w = 'lincoln_lobby_south:n',
)

nesw('lincoln_east',
    ni = nov16(513),
    ei = nov16(544),    e = 'kennard_steps:e',
    si = nov16(515),    s = 'lincoln_south:s',
    wi = nov16(516),    w = 'lincoln_entrance:n',
)

nesw('lincoln_entrance',
    ni = nov16(518),
    ei = nov16(519),
    si = nov16(520),    s = 'lincoln_east:e',
    wi = nov16(517),    w = 'lincoln_lobby_center:w'
)

nesw('lincoln_lobby_south',
    ni = nov16(521),    n = 'lincoln_lobby_center:n',
    ei = nov16(522),
    si = nov16(523),    s = 'lincoln_south:e',
    #wi = nov16(524),    # to cafeteria
    wi = sci(3452),     w = 'scifair:w',
)

nesw('scifair',
    wi = sci(3457),     w = 'scifair2:w',
    ni = sci(3458),
    ei = sci(3459),     e = 'lincoln_lobby_south:e',
    si = sci(3460),
)

nesw('scifair2',
    wi = sci(3461),
    ni = sci(3462),
    ei = sci(3463),     e = 'scifair:e',
    si = sci(3464),
)

nesw('lincoln_lobby_center',
    ni = nov16(525),    n = 'lincoln_lobby_north:n',
    ei = nov16(528),    e = 'lincoln_entrance:e',
    si = nov16(526),    s = 'lincoln_lobby_south:s',
    wi = nov16(527),
)

# this could really be a five-way clump.
nesw('lincoln_lobby_north',
    ni = nov16(540),    n = 'lincoln_lobby_open',
    ei = nov16(529),    #music & theater
    si = nov16(531),    s = 'lincoln_lobby_center:s',
    wi = nov16(533),    w = 'preschool_hall:w',
)

lfr('lincoln_lobby_open', nov16(541), 'lincoln_lobby_north:w', 'lincoln_elevator:0', 'lincoln_lobby_north:e')

tunneloneway('lincoln_elevator',
    nov16([542, 543, 542]), 'lincoln_lobby_north:s', 'lincoln_lobby_north:s'
)

nesw('preschool_hall',
    ei = nov16(535),    e = 'lincoln_lobby_north:e',
    wi = nov16(534),    w = 'preschool_end:w',
)

nesw('preschool_end',
    ni = nov16(537),    # Ben's classroom!
    ei = nov16(538),    e = 'preschool_hall:e',
    si = nov16(539),
    wi = nov16(536),
)

nesw('kennard_steps',
    ni = nov16(545),
    ei = nov16(546),
    si = nov16(547),    s = 'kennard:s',
    wi = nov16(548),    w = 'lincoln_east:w',
)

nesw('kennard',
    ni = nov16(550),    n = 'kennard_steps:n',
    si = nov16(549),    s = 'walnut_kennard2:s',
)

nesw('walnut_kennard2',
    ni = nov16(553),    n = 'kennard:n',
    ei = nov16(554),    e = 'walnut_kennard:e',
    si = nov16(551),
    wi = nov16(552),    w = 'walnut_arch:w',
)

#
# Trip to Connecticut
#

_ = 'connecticut_'

tunnelonewayskip(_+'drive', 5,
    nov17(
        range(569, 635) +
        range(637, 652) +
        range(653, 658) +
        range(660, 690) +
        range(691, 770)
    ), 'driveway:n', _+'driveway:e'
)

nesw(_+'driveway',
    ni = nov17(771),    n = 'menu_home',
    ei = nov17(770),    e = _+'garage:e',
    si = nov17(773),    s = _+'driveway_mid:s',
    wi = nov17(772),
)

nesw(_+'driveway_mid',
    ni = nov17(776),    n = _+'driveway:n',
    ei = nov17(777),
    si = nov17(774),    s = _+'driveway_end:s',
    wi = nov17(775),
)

nesw(_+'driveway_end',
    ni = nov17(780),    n = _+'driveway_mid:n',
    ei = nov17(781),    e = _+'aroundblock:0',
    si = nov17(778),
    wi = nov17(779),
)

tunnelonewayskip(_+'aroundblock', 3,
    may27a(range(125, 202)),
    _+'driveway_end:n', _+'driveway_end:e'
)

nesw(_+'garage',
    ni = nov17(785),
    ei = nov17(782),    e = _+'playroom:0',
    si = nov17(784),
    wi = nov17(783),    w = _+'driveway:w',
)

clump(_+'playroom', [
    (nov17(799), _+'hall:e'),
    (nov17(790),),
    (nov17(800), _+'entry:2'),
    (nov17(787),),
    (nov17(788),),
    (nov17(801), _+'garage:w'),
    (nov17(789),)
    ]
)

tableau(_+'playroom_pix',
    map(lambda x: (x,), nov17(range(791, 799))),
    _+'playroom:0', _+'playroom:2',
    b = _+'playroom:1'
)

findNode(_+'playroom:1').actions += [((.1, .5, .1, .1), _+'playroom_pix:0')]
findNode(_+'playroom:1').actions += [((.2, .5, .1, .1), _+'playroom_pix:1')]
findNode(_+'playroom:1').actions += [((.3, .5, .1, .1), _+'playroom_pix:2')]
findNode(_+'playroom:1').actions += [((.4, .5, .1, .1), _+'playroom_pix:3')]
findNode(_+'playroom:1').actions += [((.5, .4, .15, .2), _+'playroom_pix:4')]
findNode(_+'playroom:1').actions += [((.65, .5, .1, .1), _+'playroom_pix:5')]
findNode(_+'playroom:1').actions += [((.75, .5, .1, .1), _+'playroom_pix:6')]
findNode(_+'playroom:1').actions += [((.85, .5, .1, .1), _+'playroom_pix:7')]

nesw(_+'hall',
    ni = nov17(809),    n = _+'laundry:n',
    ei = nov17(825),    e = _+'kitchen:e',
    si = nov17(804),    s = _+'entry:3',
    wi = nov17(824),    w = _+'playroom:5',
)

nesw(_+'laundry',
    ni = nov17(810),
    ei = nov17(811),
    si = nov17(813),    s = _+'hall:s',
    wi = nov17(812),
)

clump(_+'entry', [
    (nov17(826), _+'stairs_up'),
    (nov17(827), _+'hall:n'),
    (nov17(828), _+'living:e'),
    (nov17(829),),
    (nov17(830), _+'playroom:5')
    ]
)

nesw(_+'living',
    ni = nov17(834),    n = _+'dining:n',
    ei = nov17(831),
    si = nov17(832),
    wi = nov17(833),    w = _+'entry:4',
)

nesw(_+'dining',
    ni = nov17(835),
    ei = nov17(836),
    si = nov17(837),    s = _+'living:s',
    wi = nov17(838),    w = _+'kitchen:w',
)

nesw(_+'kitchen',
    ni = nov17(878),
    ei = nov17(880),    e = _+'dining:e',
    si = nov17(877),
    wi = nov17(879),    w = _+'hall:w',
)

findNode(_+'kitchen:s').actions += [((.4, .4, .3, .3), _+'kitchen_pix')]

deadend(_+'kitchen_pix', nov17(882))

bf(_+'stairs_up', nov17(839), _+'stairs_down', _+'stairs_top:n')
bf(_+'stairs_down', nov17(840), _+'stairs_up', _+'entry:3')

nesw(_+'stairs_top',
    ni = nov17(841),
    ei = nov17(842),    e = _+'hall2:1',
    si = nov17(843),    s = _+'stairs_down',
    wi = edited(94),    w = _+'brms:w',
)

findNode(_+'stairs_top:s').d = _+'stairs_down'
findNode(_+'stairs_down').d = _+'entry:3'
findNode(_+'stairs_up').u = _+'stairs_top:n'
findNode(_+'entry:0').u = _+'stairs_up'
findNode(_+'entry:1').u = _+'stairs_up'

nesw(_+'brms',
    ni = nov17(844),
    ei = nov17(845),    e = _+'stairs_top:e',
    si = nov17(846),    s = _+'brms_closet',
    wi = nov17(847),
)

deadend(_+'brms_closet', nov17(848))

clump(_+'hall2', [
    (nov17(849), _+'bath2:n'),
    (nov17(856), _+'den:e'),
    (nov17(851), _+'brlaura:e'),
    (nov17(852), _+'brsue:s'),
    (nov17(853), _+'stairs_top:w')
    ]
)

nesw(_+'bath2',
    ni = nov17(854),
    si = nov17(855),    s = _+'hall2:3',
)

nesw(_+'den',
    ni = nov17(857),    n = _+'den_npix',
    ei = nov17(859),
    si = nov17(860),
    wi = nov17(861),    w = _+'hall2:4',
)

findNode(_+'den:n').actions += [((.73, .32, .09, .14), _+'den_npix')]

deadend(_+'den_npix', nov17(858))

nesw(_+'brlaura',
    ni = nov17(866),
    ei = nov17(863),
    si = nov17(864),
    wi = nov17(865),    w = _+'hall2:4',
)

findNode(_+'brlaura:e').actions += [((.5, .6, .2, .15), _+'brlaura_epix')]
findNode(_+'brlaura:n').actions += [((.33, .37, .2, .21), _+'brlaura_npix')]
findNode(_+'brlaura:s').actions += [((.1, .5, .1, .1), _+'brlaura_spix')]
findNode(_+'brlaura:s').actions += [((.475, .57, .11, .11), _+'brlaura_natworld')]

deadend(_+'brlaura_npix', nov17(867))
deadend(_+'brlaura_epix', nov17(876))
deadend(_+'brlaura_spix', mar9(637))
NatWorldNode(_+'brlaura_natworld', (.475, .57, .11, .11))

tableau(_+'brlaura_window_top_pix',
    map(lambda x: (x,), mar9(range(639, 643))),
    _+'brlaura:s', _+'brlaura:s',
    b = _+'brlaura:s'
)

tableau(_+'brlaura_window_bot_pix',
    map(lambda x: (x,), mar9(range(643, 646))),
    _+'brlaura:s', _+'brlaura:s',
    b = _+'brlaura:s'
)

findNode(_+'brlaura:s').actions += [((.5, .2, .15, .15), _+'brlaura_window_top_pix:0')]
findNode(_+'brlaura:s').actions += [((.65, .2, .15, .15), _+'brlaura_window_top_pix:1')]
findNode(_+'brlaura:s').actions += [((.8, .2, .15, .15), _+'brlaura_window_top_pix:2')]
findNode(_+'brlaura:s').actions += [((.9, .2, .15, .15), _+'brlaura_window_top_pix:3')]

findNode(_+'brlaura:s').actions += [((.65, .45, .15, .15), _+'brlaura_window_bot_pix:0')]
findNode(_+'brlaura:s').actions += [((.8, .45, .15, .15), _+'brlaura_window_bot_pix:1')]
findNode(_+'brlaura:s').actions += [((.85, .45, .15, .15), _+'brlaura_window_bot_pix:2')]

nesw(_+'brsue',
    ni = nov17(870),    n = _+'hall2:0',
    ei = nov17(871),
    si = nov17(868),
    wi = nov17(869),
)

findNode(_+'brsue:s').actions += [((.55, .61, .05, .1), _+'brsue_spix')]
findNode(_+'brsue:e').actions += [((.48, .54, .18, .12), _+'brsue_epix')]

deadend(_+'brsue_spix', nov17(872))
deadend(_+'brsue_epix', nov17(873))

#
# Newton library
#

_ = 'newtonlibrary_'

nesw(_+'start',
     ei = feb23(501),   e = _+'bridge:e'
)

nesw(_+'bridge',
     ei = feb23(502),   e = _+'entrance:e',
     si = feb23(503),
     wi = feb23(504),
     ni = feb23(505)
)

nesw(_+'entrance',
     ei = feb23(506),   e = _+'entry:e',
     wi = feb23(507),   w = _+'bridge:w'
)

nesw(_+'entry',
     ei = feb23(508),   e = _+'lobby:0',
     si = feb23(509),
     wi = feb23(510),   w = _+'entrance:w',
     ni = feb23(511)
)

clump(_+'lobby', [
    (feb23(512), _+'kidhall:e'),
    (feb23(513), _+'3n_atrium:s'),
    (feb23(514),),
    (feb23(515),),
    (feb23(516), _+'entry:w')
    ]
)

nesw(_+'kidhall',
     ei = feb24(593),   e = _+'kidmain:e',
     wi = feb24(595),   w = _+'lobby:4'
)

nesw(_+'kidmain',
     ei = feb24(596),
     si = feb24(597),   s = _+'kidvid:s',
     wi = feb24(599),   w = _+'kidhall:w',
     ni = feb24(600)
)

nesw(_+'kidvid',
     si = feb24(601),   s = _+'kidfact:s',
     wi = feb24(603),
     ni = feb24(604),   n = _+'kidmain:n',
     ei = feb24(605)
)

nesw(_+'kidfact',
     si = feb24(606),
     wi = feb24(607),
     ni = feb24(608),   n = _+'kidvid:n',
     ei = feb24(609)
)

# Newton library, third floor

nesw(_+'3n_atrium',
     si = feb23(518),
     wi = feb23(525),   w = _+'3nw:s',
     ei = feb24(573),   e = _+'3e:s'
)

x0 = StdNode(_+'3n_atrium_v:0', feb23(517))
x1 = findNode(_+'3n_atrium:s')
x2 = StdNode(_+'3n_atrium_v:2', feb23(519))
x3 = StdNode(_+'3n_atrium_v:3', feb23(520))
x4 = StdNode(_+'3n_atrium_v:4', feb23(521))
x5 = StdNode(_+'3n_atrium_v:5', feb23(522))

x0.d, x1.u = x1, x0
x1.d, x2.u = x2, x1
x2.d, x3.u = x3, x2
x3.d, x4.u = x4, x3
x4.d, x5.u = x5, x4

nesw(_+'3nw',
     si = feb23(523),   s = _+'3w:s',
     ei = feb23(524),   e = _+'3n_atrium:s'
)

nesw(_+'3w',
     si = feb23(526),   s = _+'3sw:s',
     wi = feb23(527),
     ni = feb23(528),   n = _+'3nw:e',
     ei = feb23(529),   e = _+'3w_atrium:e'
)

nesw(_+'3w_atrium',
     ei = feb23(534),
     ni = feb23(537),
     si = feb23(538)
)

x0 = findNode(_+'3w_atrium:e')
x1 = StdNode(_+'3w_atrium:1', feb23(535))
x2 = StdNode(_+'3w_atrium:2', feb23(536))

x0.d, x1.u = x1, x0
x1.d, x2.u = x2, x1

findNode(_+'3w_atrium:s').d = x1
findNode(_+'3w_atrium:n').d = x1
findNode(_+'3w_atrium:s').r = findNode(_+'3w:s')
findNode(_+'3w_atrium:n').l = findNode(_+'3w:n')

nesw(_+'3sw',
     si = feb23(533),   s = _+'3ssw:e',
     wi = feb23(530),   w = _+'3sw_elevator:w',
     ni = feb23(531),   n = _+'3w:n',
     ei = feb23(532),   e = _+'3se:e'
)

nesw(_+'3sw_elevator',
     wi = feb23(539),
     ni = feb23(540),
     ei = feb23(541),   e = _+'3sw:e',
     si = feb23(542),   s = _+'3_elevator'
)

nesw(_+'3e',
     si = feb24(574),   s = _+'3se:s',
     wi = feb24(575),   w = _+'3e_atrium:0',
     ni = feb24(576),   n = _+'3n_atrium:s',
     ei = feb24(577)
)

x0 = StdNode(_+'3e_atrium:0', feb24(578))
x1 = StdNode(_+'3e_atrium:1', feb24(579))
x2 = StdNode(_+'3e_atrium:2', feb24(580))

x0.d, x1.u = x1, x0
x1.d, x2.u = x2, x1
x0.l = findNode(_+'3e:s')
x0.r = findNode(_+'3e:n')

nesw(_+'3se',
     si = feb24(581),   s = _+'3sse:w',
     wi = feb24(582),   w = _+'3sw:w',
     ni = feb24(583),   n = _+'3e:n',
     ei = feb24(584)
)

nesw(_+'3sse',
     wi = feb24(585),   w = _+'3ssw:w',
     ni = feb24(586),   n = _+'3se:n',
     ei = feb24(587)
)

nesw(_+'3ssw',
     ei = feb24(588),   e = _+'3sse:e',
     wi = feb24(589),
     ni = feb24(590),   n = _+'3sw:n'
)

#
# Candlewood Drive
#

_ = 'candlewooddrive_'
j7 = jul7_2

nesw(_+'driveend',
    ni = j7(1219),  n = _+'drivetop:n',
    ei = j7(1220),
    si = j7(1217),
    wi = j7(1218)
)

MenuNode(_+'carmenu', [
    ('Home',                'driveway:w'),
    ('Ocean View Drive',    'oceanviewdrive_walkw:e')
    ])

findNode(_+'driveend:n').actions += [((.25, .45, .3, .35), _+'carmenu')]

nesw(_+'drivetop',
    si = j7(1213),  s = _+'driveend:s',
    wi = j7(1214),
    ni = j7(1215),
    ei = j7(1216),  e = _+'front:e'
)

nesw(_+'front',
    si = j7(1209),
    wi = j7(1210),  w = _+'drivetop:w',
    ni = j7(1211),  n = _+'entry:3',
    ei = j7(1212),  e = _+'fronte:e'
)

nesw(_+'fronte',
    ei = j7(1221),
    si = j7(1222),
    wi = j7(1223),  w = _+'front:w',
    ni = j7(1224),  n = _+'backe:3'
)

clump(_+'backe', [
    (j7(1225), _+'fronte:s'),
    (j7(1226),),
    (j7(1227), _+'back:1'),
    (j7(1228),),
    (j7(1229),)
])

clump(_+'back', [
    (j7(1230), _+'deck:s'),
    (j7(1231),),
    (j7(1232),),
    (j7(1233), _+'backe:4'),
    (j7(1234),)
])

nesw(_+'deck',
    si = j7(1235),  s = _+'center:2',
    wi = j7(1236),
    ni = j7(1237),  n = _+'back:2',
    ei = j7(1238),  e = _+'decke:e'
)

nesw(_+'decke',
    si = j7(1239),  s = _+'outdoorshoweropen',
    wi = j7(1241),  w = _+'deck:w',
    ni = j7(1242),
    ei = j7(1243)
)

lfr(_+'outdoorshoweropen', j7(1240), _+'decke:e', _+'outdoorshoweroff', _+'decke:w')

lfr(_+'outdoorshoweroff', j7(1247), _+'decke:e', _+'outdoorshoweron', _+'decke:n')
lfr(_+'outdoorshoweron', j7(1246), _+'decke:e', _+'outdoorshoweroff', _+'decke:n')

clump(_+'entry', [
    (j7(1202), _+'front:s'),
    (j7(1203),),
    (j7(1204), _+'center:4'),
    (j7(1205),),
    (j7(1206),)
])

clump(_+'center', [
    (j7(1251), _+'hall:1'),
    (j7(1252), _+'entry:0'),
    (j7(1253),),
    (j7(1254), _+'kitchen:w'),
    (j7(1255), _+'kitchen:w'),
    (j7(1256), _+'deck:n'),
    (j7(1257),)
])

nesw(_+'kitchen',
    si = j7(1258),
    wi = j7(1260),
    ni = j7(1261),
    ei = j7(1281),  e = _+'center:0'
)

clump(_+'hall', [
    (j7(1262),),
    (j7(1263), _+'kidroom'),
    (j7(1264), _+'adultroom'),
    (j7(1265), _+'basementdooropen'),
    (j7(1266), _+'center:4')
])

lr(_+'kidroom', j7(1267), _+'hall:4', _+'hall:4')
lr(_+'adultroom', j7(1268), _+'hall:4', _+'hall:4')

lfr(_+'basementdooropen', j7(1269), _+'hall:2', _+'basement:0', _+'hall:4')

clump(_+'basement', [
    (j7(1283),),
    (j7(1270),),
    (j7(1271),),
    (j7(1272), _+'basementup'),
    (j7(1274),),
    (j7(1275),)
])

lfr(_+'basementup', j7(1273), _+'basement:2', _+'hall:0', _+'basement:4')

#
# Ocean View Drive in Wellfleet
#

_ = 'oceanviewdrive_'

nesw(_+'walkw',
    ei = aug14(2774),   e = _+'walk:e',
    si = aug14(2775),
    wi = aug14(2776),
    ni = aug14(2777)
)

MenuNode(_+'carmenu', [
    ('Home',                'driveway:w'),
    ('Candlewood Drive',    'candlewooddrive_driveend:n')
    ])

findNode(_+'walkw:w').actions += [((.2, .4, .4, .4), _+'carmenu')]

nesw(_+'walk',
    ei = aug14(2778),   e = _+'walke:e',
    si = aug14(2779),
    wi = aug14(2780),   w = _+'walkw:w',
    ni = aug14(2781),   n = _+'screenporch:n'
)

nesw(_+'walke',
    ei = aug14(2782),
    si = aug14(2783),
    wi = aug14(2784),   w = _+'walk:w',
    ni = aug14(2785),   n = _+'backs:n'
)

nesw(_+'backs',
    ni = aug14(2786),   n = _+'back:n',
    ei = aug14(2787),
    si = aug14(2788),   s = _+'walke:s',
    wi = aug14(2789),   w = _+'porch:w'
)

nesw(_+'porch',
    ni = aug14(2790),   n = _+'dining:n',
    ei = aug14(2791),   e = _+'backs:e',
    si = aug14(2792),
    wi = aug14(2793),   w = _+'screenporch:w'
)

nesw(_+'screenporch',
    wi = aug14(2794),
    ni = aug14(2795),   n = _+'living:n',
    ei = aug14(2796),   e = _+'porch:e',
    si = aug14(2797),   s = _+'walk:s'
)

nesw(_+'living',
    ni = aug14(2848),
    ei = aug14(2849),   e = _+'dining:e',
    si = aug14(2850),   s = _+'screenporch:s',
    wi = aug14(2851)
)

nesw(_+'dining',
    ei = aug14(2852),
    si = aug14(2853),   s = _+'porch:s',
    wi = aug14(2854),   w = _+'living:w',
    ni = aug14(2855),   n = _+'kitchen:n'
)

nesw(_+'kitchen',
    ni = aug14(2856),
    ei = aug14(2857),
    si = aug14(2858),   s = _+'dining:s',
    wi = aug14(2859)
)

nesw(_+'back',
    ni = aug14(2810),   n = _+'backn:n',
    ei = aug14(2811),
    si = aug14(2812),   s = _+'backs:s',
    wi = aug14(2846)
)

nesw(_+'backn',
    ni = aug14(2813),   n = _+'prisrd1:n',
    ei = aug14(2814),
    si = aug14(2815),   s = _+'back:s',
    wi = aug14(2816)
)

nesw(_+'prisrd1',
    ni = aug14(2817),
    ei = aug14(2818),   e = _+'prisrd2:e',
    si = aug14(2819),   s = _+'backn:s',
    wi = aug14(2820)
)

nesw(_+'prisrd2',
    ei = aug14(2821),   e = _+'prisrd3:e',
    si = aug14(2822),
    wi = aug14(2823),   w = _+'prisrd1:w',
    ni = aug14(2824)
)

nesw(_+'prisrd3',
    ei = aug14(2825),   e = _+'prisrd4:e',
    si = aug14(2826),
    wi = aug14(2827),   w = _+'prisrd2:w',
    ni = aug14(2828)
)

nesw(_+'prisrd4',
    ei = aug14(2829),   e = _+'prisrd5:e',
    si = aug14(2830),
    wi = aug14(2831),   w = _+'prisrd3:w',
    ni = aug14(2832)
)

nesw(_+'prisrd5',
    ei = aug14(2833),
    si = aug14(2834),   s = _+'prisrd6:s',
    wi = aug14(2835),   w = _+'prisrd4:w',
    ni = aug14(2836)
)

nesw(_+'prisrd6',
    si = aug14(2837),   s = _+'prisrd7:s',
    wi = aug14(2838),
    ni = aug14(2839),   n = _+'prisrd5:n',
    ei = aug14(2840)
)

nesw(_+'prisrd7',
    si = aug14(2841),
    wi = aug14(2842),
    ni = aug14(2843),   n = _+'prisrd6:n',
    ei = aug14(2844),   e = _+'path1:e'
)

nesw(_+'path1',
    ei = aug14(2860),   e = _+'path2:e',
    si = aug14(2861),
    wi = aug14(2862),   w = _+'prisrd7:w',
    ni = aug14(2863)
)

nesw(_+'path2',
    ei = aug14(2864),   e = _+'path3:e',
    si = aug14(2865),
    wi = aug14(2866),   w = _+'path1:w',
    ni = aug14(2867)
)

nesw(_+'path3',
    ei = aug14(2868),   e = _+'path4:e',
    si = aug14(2870),
    wi = aug14(2871),   w = _+'path2:w',
    ni = aug14(2872)
)

nesw(_+'path4',
    ei = aug14(2873),   e = _+'beach1:e',
    si = aug14(2874),
    wi = aug14(2875),   w = _+'path3:w',
    ni = aug14(2876)
)

nesw(_+'beach1',
    ei = aug14(2877),
    si = aug14(2878),
    wi = aug14(2879),   w = _+'path4:w',
    ni = aug14(2880),   n = _+'beach2:n'
)

nesw(_+'beach2',
    ni = aug14(2881),   n = _+'beach3:n',
    ei = aug14(2882),
    si = aug14(2883),   s = _+'beach1:s',
    wi = aug14(2884)
)

nesw(_+'beach3',
    ni = aug14(2885),   n = _+'beach4:n',
    ei = aug14(2886),   e = _+'beachphotos:0',
    si = aug14(2887),   s = _+'beach2:s',
    wi = aug14(2888)
)

nesw(_+'beach4',
    ni = aug14(2889),
    ei = aug14(2890),
    si = aug14(2891),   s = _+'beach3:s',
    wi = aug14(2892)
)

photoalbum(_+'beachphotos',
    aug14((
        2893, 2894, 2896, 2899, 2900, 2906, 2908,
        2913, 2922, 2923, 2924)) +
    aug13((2765,)) +
    aug12((2753, 2751)),
    _+'beach3:e'
)

#
# Coast Guard Beach in Eastham.
#

_ = 'coastguard_'
back = 'candlewooddrive_driveend:n'

tunnelonewayskip(_+'start', 3,
    jul7b(range(1284, 1304)), back, _+'ranger:0'
)

tunneloneway(_+'ranger',
    jul7b((1305,)), back, _+'tram:0'
)

tunnelonewayskip(_+'tram', 3,
    jul7b(range(1314, 1342)), _+'ranger:0', _+'stop:0'
)

clump(_+'stop', (
    (jul7b(1344), _+'house1:e'),
    (jul7b(1345),),
    (jul7b(1343), _+'wait2:n'),
))

nesw(_+'house1',
    ei = jul7b(1348),
    si = jul7b(1349),
    wi = jul7b(1346), w = _+'stop:1',
    ni = jul7b(1347), n = _+'house2:n',
)

nesw(_+'house2',
    ni = jul7b(1350),
    wi = jul7b(1351),
    si = jul7b(1352), s = _+'house1:s',
    ei = jul7b(1353), e = _+'walk1:e',
)

nesw(_+'walk1',
    ni = jul7b(1354),
    ei = jul7b(1355), e = _+'walk2:e',
    si = jul7b(1356),
    wi = jul7b(1351), w = _+'house2:w',
)

nesw(_+'walk2',
    ei = jul7b(1357), e = _+'beach1:4',
    si = jul7b(1358),
    wi = jul7b(1361), w = _+'walk1:w',
    ni = jul7b(1354),
)

clump(_+'beach1', (
    (jul7b(1359),),
    (jul7b(1360),),
    (jul7b(1361), _+'walk2:w'),
    (jul7b(1362), ),
    (jul7b(1363),),
))

#
# Station street
#

_ = 'station_'

nesw(_+'wash',
    si = feb26(231),
    ei = feb26(232), e = _+'a:0',
    ni = feb26(233),
    wi = feb26(315), w = 'wash_station:w',
)

clump(_+'a', (
    (feb26(235), _+'b:e'),
    (feb26(236), _+'wash:w'),
))

nesw(_+'b',
    ni = feb26(239),
    ei = feb26(240), e = _+'c:e',
    si = feb26(237), s = 'broovill_t2:s',
    wi = feb26(238), w = _+'a:1',
)

nesw(_+'c',
    ni = feb26(244),
    ei = feb26(241), e = _+'kent:e',
    si = feb26(242),
    wi = feb26(243), w = _+'b:w',
)

nesw(_+'kent',
    ni = feb26(248),
    ei = feb26(245), e = 'kent_a:n',
    si = feb26(246),
    wi = feb26(247), w = _+'c:w',
)

# Kent street (there's a bend here)

_  = 'kent_'

nesw(_+'a',
    ni = feb26(249), n = _+'b:n',
    ei = feb26(250),
    si = feb26(251), s = 'station_kent:w',
    wi = feb26(252),
)

nesw(_+'b',
    ni = feb26(253), n = _+'bowker:n',
    ei = feb26(254),
    si = feb26(255), s = _+'a:s',
    wi = feb26(256),
)

nesw(_+'bowker',
    ni = feb26(257), n = _+'brook:n',
    ei = feb26(258),
    si = feb26(259), s = _+'b:s',
    wi = feb26(260),
)

nesw(_+'brook',
    ni = feb26(261), n = _+'aspinwall:n',
    ei = feb26(262),
    si = feb26(263), s = _+'bowker:s',
    wi = feb26(313),
)

nesw(_+'brook_waving',
    ni = feb26(261), n = _+'aspinwall:n',
    ei = feb26(262),
    si = feb26(263), s = _+'bowker:s',
    wi = feb26(314),
)

findNode(_+'brook:w').actions += [((.63, .6, .13, .25), _+'brook_waving:w')]
findNode(_+'brook_waving:w').actions += [((.63, .6, .13, .25), _+'brook:w')]

nesw(_+'aspinwall',
    ni = feb26(265), n = _+'football:n',
    ei = feb26(266),
    si = feb26(267), s = _+'brook:s',
    wi = feb26(268), w = 'aspinwall_a:0b',
)

nesw(_+'football',
    ni = feb26(270), n = _+'c:0',
    ei = feb26(271),
    si = feb26(272), s = _+'aspinwall:s',
    wi = feb26(273),
)

clump(_+'c', (
    (feb26(274), _+'kentsq:n'),
    (feb26(275), _+'football:s'),
))

nesw(_+'kentsq',
    ni = feb26(276), n = _+'francis:n',
    ei = feb26(277),
    si = feb26(278), s = _+'c:1',
    wi = feb26(279),
)

nesw(_+'francis',
    ni = feb26(280),
    ei = feb26(281),
    si = feb26(282), s = _+'kentsq:s',
    wi = feb26(283), w = 'francis_a:0',
)

# Francis street

_ = 'francis_'

clump(_+'a', (
    (feb26(284), _+'school:w'),
    (feb26(285), 'kent_francis:e'),
))

nesw(_+'school',
    ni = feb26(287), n = 'lawrence_scifest:n',
    ei = feb26(288), e = _+'a:1',
    si = feb26(289),
    wi = feb26(286), w = _+'park1:w',
)

nesw(_+'park1',
    ni = feb26(291),
    ei = feb26(292), e = _+'school:e',
    si = feb26(293),
    wi = feb26(290), w = _+'park2:w',
)

nesw(_+'park2',
    ni = feb26(296),
    ei = feb26(297), e = _+'park1:e',
    si = feb26(298), s = 'toxteth:0f',
    wi = feb26(294),                    # 295 is Max waving
)

nesw(_+'park2_waving',
    ni = feb26(296),
    ei = feb26(297), e = _+'park1:e',
    si = feb26(298), s = 'toxteth:0f',
    wi = feb26(295),
)

findNode(_+'park2:w').actions += [((.67, .45, .1, .25), _+'park2_waving:w')]
findNode(_+'park2_waving:w').actions += [((.67, .45, .1, .25), _+'park2:w')]

# Toxteth street

tunnel('toxteth', [
    feb26((299, 300)),
    feb26((301, 302)),
    ], 'francis_park2:n', 'aspinwall_toxteth:s'
)

# Aspinwall street

_ = 'aspinwall_'

nesw(_+'toxteth',
    ni = feb26(305), n = 'toxteth:1b',
    ei = feb26(306), e = _+'harrison:e',
    si = feb26(303),
    wi = feb26(304),
)

nesw(_+'harrison',
    ni = feb26(310),
    ei = feb26(307), e = _+'a:0f',
    si = feb26(308),
    wi = feb26(309), w = _+'toxteth:w',
)

tunnel(_+'a', [
    feb26((311, 312)),
    ], _+'harrison:w', 'kent_aspinwall:e'
)

# Lawrence Science Fair

nesw('lawrence_scifest',
    si = mar05(317), s = 'francis_school:s',
    wi = mar05(318),
    ni = mar05(319),
    ei = mar05(321),
)

"""
nesw(_+'',
    ni = feb26(),
    ei = feb26(),
    si = feb26(),
    wi = feb26(),
)
"""

# Baker School Science Fest

tunnelonewayskip('drivetobaker', 5,
    mar11(
        range(2108, 2113) + range(2114,2168)
    ), 'baker_fest:n', 'baker_fest:n'
)

nesw('baker_fest',
    ni = mar11(2168), n = 'baker_screen',
    ei = mar11(2169),
    si = mar11(2170),
    wi = mar11(2171),
)

bf('baker_screen', mar11(2173), 'baker_fest:n', 'baker_fest:n')

findNode('baker_screen').actions += [((.335, .29, .39, .39), 'baker_natworld')]
NatWorldNode('baker_natworld', (.335, .29, .39, .39))

# Main flow for Nat's world

def main():
    import getopt
    import sys

    def usage():
        print "Options:"
        print "\t-b\tBig"
        print "\t-d\tDebug mode"
        print "\t-f\tFull screen"
        print "\t-nc\tNo credits"
        print "\t-nt\tNo title"
        print "\t-v\tValidate all the nodes"
        print "\t-l\tList all the nodes"

    try:
        opts, args = getopt.getopt(sys.argv[1:], "bcdfn:vl")
    except getopt.GetoptError:
        # print help information and exit:
        usage()
        return

    big = 0
    debug = 0
    caption = 0
    validateNodes = 0
    fullscreen = 0
    credits = 1
    title = 1
    transitions = 1
    listNodes = 0

    for o, a in opts:
        if o == "-b":
            big = 1
        elif o == "-c":
            caption = 1
        elif o == "-d":
            debug = 1
        elif o == "-f":
            fullscreen = 1
        elif o == "-n":
            for c in a:
                if c == "c":
                    credits = 0
                elif c == "t":
                    title = 0
                elif c == 'x':
                    transitions = 0
                else:
                    usage()
                    return
        elif o == "-v":
            validateNodes = 1
        elif o == "-l":
            listNodes = 1
        else:
            usage()
            return

    if debug:
        print '%d nodes' % (Node.countNodes())

    if debug:
        MenuNode('menu_jump', [
            ('Home',                    'hall:w',           'h'),
            ('10 Milton',               'milton:s',         'm'),
            ('Lincoln',                 'lincoln_east:n',   'l'),
            ('Beacon T',                'wash_t:n',         't'),
            ('Brookline Village T',     'broovill_t:n',     'v'),
            ('Connecticut',             'connecticut_driveway:n',    'c'),
            ('Ct Computer',             'connecticut_brlaura:s',     'x'),
            ('Newton Library',          'newtonlibrary_start:e',    'n'),
            ('Candlewood Drive',        'candlewooddrive_outdoorshoweropen',   'a'),
            ('Ocean View Drive',        'oceanviewdrive_walkw:e',        'o'),
            ('Coast Guard Beach',       'coastguard_start:0',       'b'),
			('Baker Science Fest',		'baker_fest:n'),
            ])

        Node.setJumpNode('z', 'menu_jump')

    nw = WorldApp.WorldApp()

    if title:
        nw.setTitle("Nat's World")

    if big:
        nw.setScreenSize((1200, 900))
    else:
        nw.setScreenSize((800, 600))
    nw.setFullScreen(fullscreen)
    nw.setDebug(debug)
    nw.setCaption(caption)
    nw.setValidateNodes(validateNodes)
    nw.setTransitions(transitions)

    #nw.setHomeNode('hall:w')
    #nw.setHomeNode('walnut_kennard:n')
    nw.setHomeNode('station_wash:e')

    nw.setCursors('cursors.bmp', (
        'arrow',    'hand',
        'left',     'right',
        'up',       'down',
        'left180',  'right180',
        'forward',  'back',
        'x'
        ))

    if credits:
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

    if listNodes:
        fout = open("nodes.xml", "w")
        Node.dumpAllNodes(fout)

    nw.run()

if __name__ == '__main__':
    main()
