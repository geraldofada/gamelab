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

        self.score = 0
        self.time = 0
        self.level = 1

        if globals.DIFFICULTY["easy"][0]:
            self.difficulty = "Peaceful"
        elif globals.DIFFICULTY["medium"][0]:
            self.difficulty = "Easy (x2 Multiplier)"
        elif globals.DIFFICULTY["hard"][0]:
            self.difficulty = "Hard (x3 Multiplier)"
        else:
            self.difficulty = "?"

    def run(self):
        if keyboard.key_pressed("esc"):
            globals.PLAY_INIT = True
            globals.GAME_STATE = 0
            self.window.delay(150)

        if len(self.alien.aliens) <= 0:
            self.level += 1
            if self.level == 2:
                self.alien.__init__(self.window, (5, 3))
            elif self.level == 3:
                self.alien.__init__(self.window, (6, 4))
            elif self.level == 4:
                self.alien.__init__(self.window, (8, 5))
            elif self.level == 5:
                self.alien.__init__(self.window, (9, 5))
            elif self.level == 6:
                self.alien.__init__(self.window, (11, 5))
            elif self.level == 7:
                self.alien.__init__(self.window, (13, 6))
            else:
                self.alien.__init__(self.window, (15, 6))

            self.bullet.__init__(self.window, self.alien.aliens)

        self.window.draw_text_font(
            "SCORE: {}".format(self.score),
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
            "LEVEL: {}".format(self.level),
            "./assets/fonts/pixelmix.ttf",
            globals.SCREEN_BORDER + 900,
            self.window.height - globals.SCREEN_BORDER,
        )

        self.spaceship.update()
        self.bullet.update()
        self.alien.update()

    def get_score(self, time):
        return 10 * (0.95 ** time)
