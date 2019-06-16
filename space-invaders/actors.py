from random import randint
from PPlay.sprite import Sprite
from PPlay.animation import Animation
from PPlay.keyboard import Keyboard
import globals

keyboard = Keyboard()


class SpaceShip(object):
    def __init__(self, window, bullet, alien, multiplier=1):
        self.window = window
        self.bullet = bullet
        self.alien = alien

        self.sprite = Sprite("./assets/actors/spaceship.png")
        self.player_was_shot = False

        self.speed = globals.SPACESHIP_VEL
        self.reload_cron = 0
        self.reload_time = globals.RELOAD_TIME * multiplier

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
                self.reload_cron = self.reload_time

        for bullet in self.bullet.bullets_alien:
            if self.sprite.collided(bullet):
                self.bullet.bullets_alien.remove(bullet)
                self.player_was_shot = True

        for ali in self.alien.aliens:
            if self.sprite.collided(ali):
                globals.GAME_STATE = 0
                globals.PLAY_INIT = True
                break

        self.reload_cron -= 1
        self.sprite.draw()

    def __set_pos(self):
        self.sprite.set_position(
            self.window.width / 2 - self.sprite.width / 2,
            self.window.height - self.sprite.height - 55,
        )


class Bullet(object):
    def __init__(self, window):
        self.window = window

        self.bullets = []
        self.bullets_alien = []
        self.speed = globals.BULLET_VEL

    def spawn(self, initial_x, initial_y, was_alien=False):
        bullet = Sprite("./assets/actors/bullet.png")
        bullet.set_position(initial_x - bullet.width / 2, initial_y - bullet.height)
        if was_alien == False:
            self.bullets.append(bullet)
        else:
            self.bullets_alien.append(bullet)

    def update(self):
        if len(self.bullets) > 0:
            for bullet in self.bullets:
                if bullet.y + bullet.height < 0:
                    self.bullets.remove(bullet)

        for bullet in self.bullets:
            bullet.y -= self.speed * self.window.delta_time()
            bullet.draw()

        if len(self.bullets_alien) > 0:
            for bullet in self.bullets_alien:
                if bullet.y + bullet.height < 0:
                    self.bullets_alien.remove(bullet)

        for bullet in self.bullets_alien:
            bullet.y += self.speed * self.window.delta_time()
            bullet.draw()


class Aliens(object):
    def __init__(self, window, tuple_x_y, bullet, multiplier=1):
        self.window = window
        self.tuple_x_y = tuple_x_y
        self.bullet = bullet

        self.speed = globals.ALIEN_VEL * multiplier
        self.reload_time = globals.ALIEN_RELOAD_TIME
        self.reload_cron = 0

        self.alien_killed = False
        self.alien_shooting = False

        self.aliens = []
        self.__setup()

    def update(self):
        if self.reload_cron <= 0 and self.alien_shooting == False:
            index_alien_shooting = randint(0, len(self.aliens) - 1)
            alien_shooting_x = self.aliens[index_alien_shooting].x + self.aliens[index_alien_shooting].width/2
            alien_shooting_y = self.aliens[index_alien_shooting].y + self.aliens[index_alien_shooting].height

            self.bullet.spawn(alien_shooting_x, alien_shooting_y, True)
            self.reload_cron = self.reload_time

        for alien in self.aliens:
            for bullet in self.bullet.bullets:
                if bullet.collided(alien):
                        self.bullet.bullets.remove(bullet)
                        self.aliens.remove(alien)
                        self.alien_killed = True

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

        self.reload_cron -= 1

    def __setup(self):
        for i in range(self.tuple_x_y[1]):
            for j in range(self.tuple_x_y[0]):
                alien = Animation("./assets/actors/alien_1.png", 2)
                alien.set_total_duration(800)
                alien.play()
                alien.set_position(
                    globals.SCREEN_BORDER + 1 + (alien.width + 10) * j,
                    globals.SCREEN_BORDER + 1 + (alien.height + 10) * i,
                )
                self.aliens.append(alien)
