"""
Configurations, may be changed
"""
BULLET_VEL = 200
ALIEN_VEL = 80

SPACESHIP_VEL = 400
RELOAD_TIME = 350

ALIEN_RELOAD_TIME = 400

SHOW_FPS = False
RANK_BETTER_PRECISION = False


"""
INTERNAL VARIABLES. DON'T CHANGE
"""
SCREEN_BORDER = 25
HEIGHT = 800
WIDTH = 1020

# 0: menu, 1: play, 2: rank
GAME_STATE = 0

GAME_RUNNING = True
PLAY_INIT = False

DIFFICULTY = {"easy": [True, 1], "medium": [False, 1.5], "hard": [False, 2]}
