from PPlay.sprite import Sprite
from actors import Bullet, SpaceShip, Alien
import globals


class Play(object):
    def __init__(self, window):
        self.window = window
        self.alien = Alien(self.window, 10, 5)
        self.bullet = Bullet(self.window, self.alien.aliens)
        self.spaceship = SpaceShip(self.window, self.bullet)
    
    def run(self):
        self.spaceship.update()
        self.bullet.update()
        self.alien.update()