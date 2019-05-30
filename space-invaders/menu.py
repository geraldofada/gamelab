from PPlay.animation import Animation
from PPlay.mouse import Mouse
from PPlay.keyboard import Keyboard

import globals

class Menu(object):
    def __init__(self, window):
        self.window = window
        self.play = Animation("./assets/menu/play.png", 2)
        self.difficulty = Animation("./assets/menu/difc.png", 2)
        self.rank = Animation("./assets/menu/rank.png", 2)
        self.quit = Animation("./assets/menu/quit.png", 2)
        self.difficulty_ind = Animation("./assets/menu/difc_indicator.png", 3)
        self.mouse = Mouse()
        self.__set_pos()
        self.__draw()
    
    def run(self):
        if Keyboard().key_pressed("esc"):
            globals.GAME_STARTED = False

        if self.mouse.is_over_object(self.play):
            self.play.set_curr_frame(1)
            if self.mouse.is_button_pressed(1):
                globals.GAME_STATE = 1
        else:
            self.play.set_curr_frame(0)

        if self.mouse.is_over_object(self.difficulty):
            self.difficulty.set_curr_frame(1)
            if self.mouse.is_button_pressed(1):
                globals.DIFFICULTY = (globals.DIFFICULTY + 1) % 3
                self.window.delay(150)
                self.difficulty_ind.set_curr_frame(globals.DIFFICULTY)
        else:
            self.difficulty.set_curr_frame(0)

        if self.mouse.is_over_object(self.rank):
            self.rank.set_curr_frame(1)
            if self.mouse.is_button_pressed(1):
                globals.GAME_STATE = 2
        else:
            self.rank.set_curr_frame(0)

        if self.mouse.is_over_object(self.quit):
            self.quit.set_curr_frame(1)
            if self.mouse.is_button_pressed(1):
                globals.GAME_STARTED = False
        else:
            self.quit.set_curr_frame(0)

        self.__draw()

    def __draw(self):
        self.play.draw()
        self.difficulty.draw()
        self.rank.draw()
        self.quit.draw()
        self.difficulty_ind.draw()
    
    def __set_pos(self):
        self.play.set_position(self.window.width/2 - self.play.width/2,
                               self.play.height*1 + 30*1)

        self.difficulty.set_position(self.window.width/2 - self.difficulty.width/2, 
                                     self.difficulty.height*2 + 30*2)

        self.rank.set_position(self.window.width/2 - self.rank.width/2,
                               self.rank.height*3 + 30*3)

        self.quit.set_position(self.window.width/2 - self.quit.width/2,
                               self.quit.height*4 + 30*4)

        self.difficulty_ind.set_position(50, self.window.height - self.difficulty_ind.height - 50)