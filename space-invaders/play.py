from PPlay.keyboard import Keyboard
import globals


class Play(object):
    def __init__(self, window):
        self.window = window
        self.keyboard = Keyboard()
    
    def run(self):
        if self.keyboard.key_pressed("esc"):
            globals.GAME_STATE = 0