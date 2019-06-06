from PPlay.sprite import Sprite
from PPlay.animation import Animation
from PPlay.keyboard import Keyboard
import globals

keyboard = Keyboard()


class SpaceShip(object):
    def __init__(self, window, bullet, alien):
        self.window = window
        self.bullet = bullet
        self.alien = alien

        self.sprite = Sprite("./assets/actors/spaceship.png")

        self.speed = globals.SPACESHIP_VEL
        self.reload_cron = 0

        self.__set_pos()

    def update(self):
        if keyboard.key_pressed("left") and self.sprite.x > globals.SCREEN_BORDER:
            self.sprite.x -= self.speed * self.window.delta_time()

        if (
            keyboard.key_pressed("right")
            and self.sprite.x + self.sprite.width
            < self.window.width - globals.SCREEN_BORDER
        ):
            self.sprite.x += self.speed * self.window.delta_time()

        if keyboard.key_pressed("space"):
            if self.reload_cron <= 0:
                self.bullet.spawn(
                    self.sprite.x + self.sprite.width / 2, self.sprite.y + 5
                )
                self.reload_cron = globals.RELOAD_TIME

        for ali in self.alien.aliens:
            if self.sprite.collided(ali):
                globals.GAME_STATE = 0
                globals.GAME_OVER = True
                break

        self.reload_cron -= 1
        self.sprite.draw()

    def __set_pos(self):
        self.sprite.set_position(
            self.window.width / 2 - self.sprite.width / 2,
            self.window.height - self.sprite.height - 15,
        )


class Bullet(object):
    def __init__(self, window, aliens):
        self.window = window
        self.aliens = aliens

        self.bullets = []
        self.speed = globals.BULLET_VEL

    def spawn(self, initial_x, initial_y):
        bullet = Sprite("./assets/actors/bullet.png")
        bullet.set_position(initial_x - bullet.width / 2, initial_y - bullet.height)
        self.bullets.append(bullet)

    def update(self):
        for bullet in self.bullets:
            for alien in self.aliens:
                if bullet.collided(alien):
                    self.bullets.remove(bullet)
                    self.aliens.remove(alien)

        if len(self.bullets) > 0:
            for bullet in self.bullets:
                if bullet.y + bullet.height < 0:
                    self.bullets.remove(bullet)

        for i in range(len(self.bullets)):
            self.bullets[i].y -= self.speed * self.window.delta_time()
            self.bullets[i].draw()


class Aliens(object):
    def __init__(self, window, mtx_x, mtx_y):
        self.window = window
        self.mtx_x = mtx_x
        self.mtx_y = mtx_y

        self.speed = globals.ALIEN_VEL
        self.aliens = []
        self.__setup()

    def update(self):
        for alien in self.aliens:
            alien.x += self.speed * self.window.delta_time()
            alien.update()
            alien.draw()

        for alien in self.aliens:
            if alien.x < globals.SCREEN_BORDER:
                for alien in self.aliens:
                    alien.set_position(alien.x + 1, alien.y + 20)
                self.speed *= -1
                break
            elif alien.x + alien.width > self.window.width - globals.SCREEN_BORDER:
                for alien in self.aliens:
                    alien.set_position(alien.x - 1, alien.y + 20)
                self.speed *= -1
                break

    def __setup(self):
        for i in range(self.mtx_y):
            for j in range(self.mtx_x):
                alien = Animation("./assets/actors/alien_1.png", 2)
                alien.set_total_duration(800)
                alien.play()
                alien.set_position(
                    globals.SCREEN_BORDER + 1 + (alien.width + 10) * j,
                    globals.SCREEN_BORDER + 1 + (alien.height + 10) * i,
                )
                self.aliens.append(alien)
