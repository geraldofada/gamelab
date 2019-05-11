from PPlay.keyboard import Keyboard
from PPlay.sprite import Sprite
from actors import Bullet, SpaceShip, Alien
import globals


class Play(object):
    def __init__(self, window):
        self.window = window
        self.keyboard = Keyboard()
        self.bullet = Bullet(self.window)
        self.spaceship = SpaceShip(self.window, self.bullet)
        self.alien = Alien(self.window)
    
    def run(self):
        if self.keyboard.key_pressed("esc"):
            globals.GAME_STATE = 0
        
        self.spaceship.update()
        self.bullet.update()
        self.alien.update()