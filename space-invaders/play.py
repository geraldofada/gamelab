from pygame.time import Clock

from actors import Bullet, SpaceShip, Aliens
from PPlay.keyboard import Keyboard
import globals

keyboard = Keyboard()


class Play(object):
    def __init__(self, window):
        self.window = window

        self.score = 0
        self.level = 1
        self.lives = 2
        self.time = 0
        self.multiplier = 0
        self.difficulty = ""

        if globals.DIFFICULTY["easy"][0]:
            self.multiplier = globals.DIFFICULTY["easy"][1]
        elif globals.DIFFICULTY["medium"][0]:
            self.multiplier = globals.DIFFICULTY["medium"][1]
        elif globals.DIFFICULTY["hard"][0]:
            self.multiplier = globals.DIFFICULTY["hard"][1]

        self.update_difficulty()

        self.bullet = Bullet(self.window)
        self.alien = Aliens(self.window, (5, 2), self.bullet, self.multiplier)
        self.spaceship = SpaceShip(
            self.window, self.bullet, self.alien, self.multiplier
        )

    def run(self):
        if keyboard.key_pressed("esc"):
            globals.PLAY_INIT = True
            globals.GAME_STATE = 0
            self.window.delay(150)

        if keyboard.key_pressed("d") and keyboard.key_pressed("b"):
            self.alien.aliens = []
            self.window.delay(150)

        if len(self.alien.aliens) <= 0:
            self.time = 0
            self.level += 1

            self.bullet.__init__(self.window)

            if self.level == 2:
                self.alien.__init__(self.window, (5, 3), self.bullet, self.multiplier)
            elif self.level == 3:
                self.alien.__init__(self.window, (6, 4), self.bullet, self.multiplier)
                self.multiplier += 0.5
            elif self.level == 4:
                self.alien.__init__(self.window, (8, 5), self.bullet, self.multiplier)
            elif self.level == 5:
                self.alien.__init__(self.window, (9, 5), self.bullet, self.multiplier)
                self.multiplier += 0.5
            elif self.level == 6:
                self.alien.__init__(self.window, (11, 5), self.bullet, self.multiplier)
            elif self.level == 7:
                self.alien.__init__(self.window, (13, 6), self.bullet, self.multiplier)
                self.multiplier += 0.5
            elif 15 > self.level > 7:
                self.alien.__init__(self.window, (15, 6), self.bullet, self.multiplier)
                self.multiplier += 0.1
            else:
                self.alien.__init__(self.window, (15, 6), self.bullet, self.multiplier)

            self.update_difficulty()
            self.spaceship.__init__(
                self.window, self.bullet, self.alien, self.multiplier
            )

        if self.alien.alien_killed == True:
            self.score += self.get_score(self.time) * self.multiplier
            self.alien.alien_killed = False
        
        if self.spaceship.player_was_shot == True:
            self.spaceship.__init__(
                self.window, self.bullet, self.alien, self.multiplier
            )
            self.lives -= 1
            if self.lives < 0:
                globals.GAME_STATE = 0
                globals.PLAY_INIT = True

        self.window.draw_text_font(
            "SCORE: {0:.2f}".format(self.score),
            "./assets/fonts/pixelmix.ttf",
            globals.SCREEN_BORDER,
            self.window.height - globals.SCREEN_BORDER,
        )

        self.window.draw_text_font(
            "DIFFICULTY: {}".format(self.difficulty),
            "./assets/fonts/pixelmix.ttf",
            globals.SCREEN_BORDER + 200,
            self.window.height - globals.SCREEN_BORDER,
        )

        self.window.draw_text_font(
            "LIVES: {}".format(self.lives),
            "./assets/fonts/pixelmix.ttf",
            globals.SCREEN_BORDER + 700,
            self.window.height - globals.SCREEN_BORDER,
        )

        self.window.draw_text_font(
            "LEVEL: {}".format(self.level),
            "./assets/fonts/pixelmix.ttf",
            globals.SCREEN_BORDER + 900,
            self.window.height - globals.SCREEN_BORDER,
        )

        self.spaceship.update()
        self.bullet.update()
        self.alien.update()
        self.time += self.window.delta_time()

    def get_score(self, time):
        return 11.29 * (0.94 ** time)

    def update_difficulty(self):
        if globals.DIFFICULTY["easy"][0]:
            self.difficulty = "Peaceful (x{0:.1f} Multiplier)".format(self.multiplier)
        elif globals.DIFFICULTY["medium"][0]:
            self.difficulty = "Easy (x{0:.1f} Multiplier)".format(self.multiplier)
        elif globals.DIFFICULTY["hard"][0]:
            self.difficulty = "Hard (x{0:.1f} Multiplier)".format(self.multiplier)
