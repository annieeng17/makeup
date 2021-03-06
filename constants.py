# States for the program state machine
STATE_MENU = 1
STATE_SKIN_TONE = 2 
STATE_FACE = 3
STATE_FACE_BOX = 4
STATE_FACE_BOX_RESULTS = 5 #skintone color most likely
STATE_EYES = 6
STATE_EYES_RESULTS = 7
STATE_BLUSH = 8
STATE_BLUSH_RESULTS = 9
STATE_HIGHLIGHTER = 10
STATE_HIGHLIGHTER_RESULTS = 11
STATE_CONTOUR = 12
STATE_CONTOUR_RESULTS = 13
STATE_LIP = 14
STATE_LIP_RESULTS = 15
STATE_RESULTS = 16

# Button action identifiers
ACTION_BUTTON_NEXT  = 1
ACTION_BUTTON_BACK  = 2
ACTION_UPDATE_TEXT  = 3

# Button time in seconds
BUTTON_TIME_REQUIRED = 0.5

# Skintone identifiers
SKINTONE_COOL = 'UT_COOL'
SKINTONE_WARM = 'UT_WARM'
SKINTONE_NEUTRAL = 'UT_NEUTRAL'