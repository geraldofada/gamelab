from actors import Bullet, SpaceShip, Aliens
from PPlay.keyboard import Keyboard
import globals

keyboard = Keyboard()

class Play(object):
    def __init__(self, window):
        self.window = window
        self.alien = Aliens(self.window, (5, 2))
        self.bullet = Bullet(self.window, self.alien.aliens)
        self.spaceship = SpaceShip(self.window, self.bullet, self.alien)

    def run(self):
        if keyboard.key_pressed("esc"):
            globals.PLAY_INIT = True
            globals.GAME_STATE = 0
            self.window.delay(150)

        if len(self.alien.aliens) <= 0 and globals.PLAY_LEVEL <= 7:
            globals.PLAY_LEVEL += 1

        self.spaceship.update()
        self.bullet.update()
        self.alien.update()
    
