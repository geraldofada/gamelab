from actors import Bullet, SpaceShip, Alien
from PPlay.keyboard import Keyboard
import globals


class Play(object):
    def __init__(self, window):
        self.window = window
        self.alien = Alien(self.window, 10, 5)
        self.bullet = Bullet(self.window, self.alien.aliens)
        self.spaceship = SpaceShip(self.window, self.bullet, self.alien)

    def run(self):
        if Keyboard().key_pressed("esc"):
            globals.GAME_OVER = True
            globals.GAME_STATE = 0
            self.window.delay(100)

        self.spaceship.update()
        self.bullet.update()
        self.alien.update()