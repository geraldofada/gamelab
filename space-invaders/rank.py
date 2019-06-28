from db import Database
from PPlay.keyboard import Keyboard
import globals

keyboard = Keyboard()

class Rank(object):
    def __init__(self, window):
        self.window = window
        self.data = Database().get_scores()
    
    def run(self):
        if keyboard.key_pressed("esc"):
            globals.PLAY_INIT = True
            globals.GAME_STATE = 0
            self.window.delay(150)

        self.window.draw_text_font(
            "TOP 10 Players",
            "./assets/fonts/pixelmix.ttf",
            300,
            50,
            font_size=36
        )
        
        self.window.draw_text_font(
            "NAME   SCORE",
            "./assets/fonts/pixelmix.ttf",
            300,
            140,
            font_size=26
        )

        i = 0
        for d in self.data:
            self.draw_score(d[0], d[1], 300, 200 + i)
            i += 50
    
    def draw_score(self, name, score, x, y):
        if globals.RANK_BETTER_PRECISION == True:
            text = "{}   {}".format(name, score)
        else:
            text = "{}   {:.3f}".format(name, score)

        self.window.draw_text_font(
            text,
            "./assets/fonts/pixelmix.ttf",
            x,
            y,
            font_size=26
        )