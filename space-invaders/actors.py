from PPlay.sprite import Sprite
from PPlay.animation import Animation
from PPlay.keyboard import Keyboard
import globals


class SpaceShip(object):
    def __init__(self, window, bullet):
        self.window = window
        self.bullet = bullet
        self.keyboard = Keyboard()
        self.sprite = Sprite("./assets/actors/spaceship.png")
        self.speed = 400
        self.reload_cron = 0
        self.__set_pos()
        self.__draw()

    def update(self):
        if self.keyboard.key_pressed("left") and self.sprite.x > globals.SCREEN_BORDER:
            self.sprite.x -= self.speed * self.window.delta_time()

        if (self.keyboard.key_pressed("right") and
            self.sprite.x + self.sprite.width < self.window.width - globals.SCREEN_BORDER):
            self.sprite.x += self.speed * self.window.delta_time()

        if self.keyboard.key_pressed("space"):
            if self.reload_cron <= 0:
                self.bullet.spawn(self.sprite.x + self.sprite.width/2,
                                  self.sprite.y + 5)
                self.reload_cron = globals.RELOAD_TIME

        self.reload_cron -= 1
        self.__draw()

    def __draw(self):
        self.sprite.draw()

    def __set_pos(self):
        self.sprite.set_position(self.window.width/2 - self.sprite.width/2,
                                    self.window.height - self.sprite.height - 15)

class Bullet(object):
    def __init__(self, window, aliens):
        self.window = window
        self.aliens = aliens
        self.bullets = []
        self.speed = 200

    def spawn(self, initial_x, initial_y):
        bullet = Sprite("./assets/actors/bullet.png")
        bullet.set_position(initial_x - bullet.width/2, initial_y - bullet.height)
        self.bullets.append(bullet)

    def update(self):
        if len(self.bullets) > 0:
            if self.bullets[-1].y + self.bullets[-1].height < 0:
                self.bullets = []

        for i in range(len(self.bullets)):
            for j in range(len(self.aliens)):
                if self.bullets[i].collided(self.aliens[j]):
                    self.bullets.pop(i)
                    self.aliens.pop(j)
                    break

        for i in range(len(self.bullets)):
            self.bullets[i].y -= self.speed * self.window.delta_time()
            self.bullets[i].draw()


class Alien(object):
    def __init__(self, window, mtx_x, mtx_y):
        self.window = window
        self.mtx_x = mtx_x
        self.mtx_y = mtx_y
        self.aliens = []
        self.__setup()
        self.update()

    def update(self):
        for alien in self.aliens:
            if (alien.x < globals.SCREEN_BORDER or
                alien.x + alien.width > self.window.width - globals.SCREEN_BORDER):
                for alien in self.aliens:
                    alien.set_position(alien.x, alien.y + 20)
                globals.ALIEN_VEL *= -1
                break

        for alien in self.aliens:
            alien.x += globals.ALIEN_VEL * self.window.delta_time()
            alien.update()
            alien.draw()

    def __setup(self):
        for i in range(self.mtx_y):
            for j in range(self.mtx_x):
                alien = Animation("./assets/actors/alien_1.png", 2)
                alien.set_total_duration(800)
                alien.play()
                alien.set_position(globals.SCREEN_BORDER + 1 + (alien.width + 10) * j,
                                   globals.SCREEN_BORDER + 1 + (alien.height + 10) * i)
                self.aliens.append(alien)