'''
description for fair skin for highlighter. opt for light colored highlighters.
should opt for highlighters with a pearlescent, icy silver or champagne sheen.
 adds just enough radiance to your complexion.
'''
TONE_FAIR   = 'Fair'
TONE_LIGHT  = 'Light'
TONE_MEDIUM = 'Medium'
TONE_TAN    = 'Tan'
TONE_DEEP   = 'Deep'

FEATURE_CHEEKS = 'CHEEKS'
FEATURE_EYES   = 'EYES'
FEATURE_LIPS   = 'LIPS'
FEATURE_UPPER_CHEEKS = 'HIGHLIGHTER'
FEATURE_CHEEK_BONES = 'CONTOUR'

UNDERTONE_COOL    = 'UT_COOL'
UNDERTONE_WARM    = 'UT_WARM'
UNDERTONE_NEUTRAL = 'UT_NEUTRAL'

'''
A dictionary that tells the user what shade they are right away after inputting
their information
'''
COLOR_PALETTE = {
    TONE_FAIR : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: ((203, 191, 221), 'Light Pink'),
            UNDERTONE_WARM: ((168, 181, 249),  'Light Peach'),
            UNDERTONE_NEUTRAL: ((169, 172, 247), 'Peachy Pink')
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: ((154, 157, 209), 'Fairy'),
            UNDERTONE_WARM: ((147, 172, 243), 'Glistening'),
            UNDERTONE_NEUTRAL: ((111, 130, 192), 'Tempera')
        },
        FEATURE_UPPER_CHEEKS: {
            UNDERTONE_COOL: ((0, 0, 0),        'Pearl'),
            UNDERTONE_WARM: ((204, 255, 255),  'Cream'),
            UNDERTONE_NEUTRAL: ((251, 145, 245), 'Rose Quartz')
        },
        FEATURE_CHEEK_BONES: {
            UNDERTONE_COOL: ((148, 169, 207),  'Light Taupe'),
            UNDERTONE_WARM: ((131, 157, 192),  'Sombre'),
            UNDERTONE_NEUTRAL: ((140, 166, 196), 'Fawn')
        },
        FEATURE_LIPS: {
            UNDERTONE_COOL: ((142, 143, 246),   'Pink Sands'),
            UNDERTONE_WARM: ((139, 143, 219),   'Rum Punch'),
            UNDERTONE_NEUTRAL: ((135, 151, 237), 'Pink Lemonade')
        }
    },
    TONE_LIGHT : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: ((178, 162, 246),  'Baby Pink'),
            UNDERTONE_WARM: ((166, 181, 254),  'Peach'),
            UNDERTONE_NEUTRAL: ((148, 155, 218), 'Sheer Plum')
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: ((154, 156, 221), 'Bronze'),
            UNDERTONE_WARM: ((84, 103, 171), 'Orange Soda'),
            UNDERTONE_NEUTRAL: ((130, 160, 233), 'Noir')
        },
        FEATURE_UPPER_CHEEKS: {
            UNDERTONE_COOL: ((216, 220, 245),  'Vanilla Quartz'),
            UNDERTONE_WARM: ((202, 221, 234),  'Peacky Keen'),
            UNDERTONE_NEUTRAL: ((209, 214, 255), 'Peach Schnapps')
        },
        FEATURE_CHEEK_BONES: {
            UNDERTONE_COOL: ((121, 139, 180),  'Fire'), 
            UNDERTONE_WARM: ((87, 108, 135),   'Cappuccino'),
            UNDERTONE_NEUTRAL: ((109, 132, 164), 'Cocoa')
        },
        FEATURE_LIPS: {
            UNDERTONE_COOL: ((118, 137, 212),   'Sun Kissed'),
            UNDERTONE_WARM: ((101, 122, 201),   'Colada'),
            UNDERTONE_NEUTRAL: ((153, 141, 212), 'Salt Lyfe')
        }
    },
    TONE_MEDIUM : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: ((175, 177, 211), 'Mauve'),
            UNDERTONE_WARM: ((126, 141, 227), 'Apricot'),
            UNDERTONE_NEUTRAL: ((96, 88, 195),'Soft Berry')
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: ((113, 113, 174), 'Dandelion'),
            UNDERTONE_WARM: ((128, 124, 196), 'Dusty Rose'),
            UNDERTONE_NEUTRAL: ((53, 57, 96), 'Rose Pink')
        },
        FEATURE_UPPER_CHEEKS: {
            UNDERTONE_COOL: ((191, 214, 255),  'Moonstone'),
            UNDERTONE_WARM: ((206, 231, 247),  'Champagne Pop'),
            UNDERTONE_NEUTRAL: ((177, 195, 255), 'Prismatic Amethyst')
        },
        FEATURE_CHEEK_BONES: {
            UNDERTONE_COOL: ((105, 135, 198),  'Gienah'),
            UNDERTONE_WARM: ((112, 128, 174),  'Java'),
            UNDERTONE_NEUTRAL: ((106, 118, 246), 'Paloma')
        },
        FEATURE_LIPS: {
            UNDERTONE_COOL: ((113, 119, 188),   'Siesta'),
            UNDERTONE_WARM: ((109, 116, 198),   "5 0'Clock"),
            UNDERTONE_NEUTRAL: ((115, 115, 202), 'Set Sail')
        }
    },
    TONE_TAN : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: ((66, 42, 189),    'Rose'),
            UNDERTONE_WARM: ((124, 155, 248),  'Orangey Peach'),
            UNDERTONE_NEUTRAL: ((116, 151, 225), 'Bronze')
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: ((90, 106, 198), 'Sultry'),
            UNDERTONE_WARM: ((83, 96, 186), 'Sienna'),
            UNDERTONE_NEUTRAL: ((112, 102, 178), 'Burnt Orange')
        },
        FEATURE_UPPER_CHEEKS: {
            UNDERTONE_COOL: ((188, 206, 229),  'Shimmer'),
            UNDERTONE_WARM: ((162, 187, 216),  'Prosecco Pop'),
            UNDERTONE_NEUTRAL: ((167, 193, 230), 'Butterscotch')
        },
        FEATURE_CHEEK_BONES: {
            UNDERTONE_COOL: ((110, 143, 212),  'Vallarta'),
            UNDERTONE_WARM: ((92, 127, 177),   'Havana'),
            UNDERTONE_NEUTRAL: ((128, 161, 209), 'Laguna')
        },
        FEATURE_LIPS: {
            UNDERTONE_COOL: ((92, 96, 193),   'Weekender'),
            UNDERTONE_WARM: ((79, 79, 160),   "Surf's Up"),
            UNDERTONE_NEUTRAL: ((85, 76, 178), 'Escape')
        }
    },
    TONE_DEEP : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: ((88, 94, 159),  'Raisin'),
            UNDERTONE_WARM: ((49, 106, 245), 'Bright Tangerine'),
            UNDERTONE_NEUTRAL: ((62, 66, 154), 'Rich Cinnamon')
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: ((116, 130, 191), 'Rustic'),
            UNDERTONE_WARM: ((81, 105, 200), 'Cyprus Umber'),
            UNDERTONE_NEUTRAL: ((121, 128, 169), 'Mulberry')
        },
        FEATURE_UPPER_CHEEKS: {
            UNDERTONE_COOL: ((99, 104, 149), 'Tourmaline'),
            UNDERTONE_WARM: ((140, 174, 227), 'Summer'),
            UNDERTONE_NEUTRAL: ((52, 75, 113), 'Bronzed')
        },
        FEATURE_CHEEK_BONES: {
            UNDERTONE_COOL: ((67, 116, 178), 'Casino'),
            UNDERTONE_WARM: ((204, 255, 255), 'Natura'),
            UNDERTONE_NEUTRAL: ((39, 66, 46), 'Punta Cana')
        },
        FEATURE_LIPS: {
            UNDERTONE_COOL: ((100, 88, 169),   'Island Life'),
            UNDERTONE_WARM: ((80, 68, 153),    'Berry Mojito'),
            UNDERTONE_NEUTRAL: ((118, 100, 176), 'Cruisin')
        }
    }
}

