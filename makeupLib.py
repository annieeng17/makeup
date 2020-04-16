# how to find out whether you're cool,warm or neutral toned
'''
look at the vein on your wrists
if you mostly see blue/purple veins, then you're cool toned
if you mostly see green veins, then you're warm toned
if you mostly see a blend of both blue/purple and green veins, then you're \
neutral toned
'''

# if fair skin
# cheeks:
# cool: light pink, warm: light peach, neutral: peachy pink

# if light skin
# cheeks:
# cool: baby pink, warm: peach, neutral: sheer plum

# if medium skin
# cheeks:
# cool: mauve, warm: apricot, neutral: soft berry

# if tan skin
# cheeks:
# cool: rose, warm: orangey peach, neutral: bronze

# if deep skin
# cheeks:
# cool: raisin, warm: bright tangerine, neutral: rich cinnamon

'''
fair - (172,219,255)
light - (125,194,241)
medium - (105,172,224)
tan - (66,134,198)
deep - (36,85,141)
'''

# def STATE_SKINTONE:
# draw_rects(vis, rects, (0, 255, 0))
# call on average color function and find the color, 
# if color is closest to fair then fair, 
# if color is closest to lighthen light, 
# if color is closest to medium then medium, 
# if color is closest to tan then tan, 
# if color is closest to deep then deep, 

TONE_FAIR   = (226, 245, 253) 
TONE_LIGHT  = (203, 241, 253)
TONE_MEDIUM = (186, 229, 251)
TONE_TAN    = (180, 220, 253)
TONE_DEEP   = (255, 214, 164)

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
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    },
    TONE_LIGHT : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    }
}

COLOR_PALETTE = {
    TONE_FAIR : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    },
    TONE_LIGHT : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    }
}

COLOR_PALETTE = {
    TONE_FAIR : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    },
    TONE_LIGHT : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    }
}

COLOR_PALETTE = {
    TONE_FAIR : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    },
    TONE_LIGHT : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    }
}

COLOR_PALETTE = {
    TONE_FAIR : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    },
    TONE_LIGHT : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    }
}

COLOR_PALETTE = {
    TONE_FAIR : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    },
    TONE_LIGHT : {
        FEATURE_CHEEKS: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        },
        FEATURE_EYES: {
            UNDERTONE_COOL: (0, 0, 0),
            UNDERTONE_WARM: (0, 0, 0),
            UNDERTONE_NEUTRAL: (0, 0, 0)
        }
    }
}
# SKINTONES[TONE_FAIR][FEATURE_CHEEKS][UNDERTONE_COOL]