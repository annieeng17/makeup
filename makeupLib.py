# def STATE_SKINTONE:
# draw_rects(vis, rects, (0, 255, 0))
# call on average color function and find the color, 
# if color is closest to fair then fair, 
# if color is closest to lighthen light, 
# if color is closest to medium then medium, 
# if color is closest to tan then tan, 
# if color is closest to deep then deep, 

TONE_FAIR   = (211, 231, 255) 
TONE_LIGHT  = (185, 224, 255)
TONE_MEDIUM = (142, 191, 239)
TONE_TAN    = (120, 174, 237)
TONE_DEEP   = ( 84, 134, 180)

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
            UNDERTONE_COOL: (203, 191, 221),   #Light Pink
            UNDERTONE_WARM: (168, 181, 249),   #Light Peach
            UNDERTONE_NEUTRAL: (169, 172, 247) #Peachy Pink
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),   #
            UNDERTONE_WARM: (0, 0, 0),   #
            UNDERTONE_NEUTRAL: (0, 0, 0) #
        }
    },
    TONE_LIGHT : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (178, 162, 246),  #Baby Pink
            UNDERTONE_WARM: (166, 181, 254),  #Peach
            UNDERTONE_NEUTRAL: (148, 155, 218)#Sheer Plum
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    },
    TONE_MEDIUM : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (175, 177, 211),#Mauve
            UNDERTONE_WARM: (126, 141, 227),#Apricot
            UNDERTONE_NEUTRAL: (96, 88, 195)#Soft Berry
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    },
    TONE_TAN : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (66, 42, 189),    #Rose
            UNDERTONE_WARM: (124, 155, 248),  #Orangey Peach
            UNDERTONE_NEUTRAL: (116, 151, 225)#Bronze
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    },
    TONE_DEEP : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (88, 94, 159),  #Raisin
            UNDERTONE_WARM: (49, 106, 245), #Bright Tangerine
            UNDERTONE_NEUTRAL: (62, 66, 154)#Rich Cinnamon
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    }
}

# SKINTONES[TONE_FAIR][FEATURE_CHEEKS][UNDERTONE_COOL]