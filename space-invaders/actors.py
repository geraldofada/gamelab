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
    def __init__(self, window):
        self.window = window
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
            self.bullets[i].y -= self.speed * self.window.delta_time()
            self.bullets[i].draw()


class Alien(object):
    def __init__(self, window):
        self.window = window
        self.aliens = [[Animation("./assets/actors/alien_1.png", 2) for _ in range(10)] for _ in range(5)]
        self.__setup()
        self.update()
    
    #TODO: fix the movement and create a function to set the position
    def update(self):
        for i in range(len(self.aliens)):
            if (self.aliens[i][-1].x >= self.window.width - globals.SCREEN_BORDER - 1 or
                self.aliens[i][0].x <= globals.SCREEN_BORDER):
                globals.ALIEN_VEL *= -1
                print("foi")
                break

        for i in range(len(self.aliens)):
            for j in range(len(self.aliens[0])):
                if (self.aliens[i][j].x >= globals.SCREEN_BORDER and
                    self.aliens[i][j].x <= self.window.width - globals.SCREEN_BORDER):
                    self.aliens[i][j].x += globals.ALIEN_VEL * self.window.delta_time()

                self.aliens[i][j].update()
                self.aliens[i][j].draw()
    
    def __setup(self):
        for i in range(len(self.aliens)):
            for j in range(len(self.aliens[0])):
                self.aliens[i][j].set_position(globals.SCREEN_BORDER + 1 + (self.aliens[i][j].width + 25) * j,
                                               globals.SCREEN_BORDER + 1 + (self.aliens[i][j].height + 25) * i)
                self.aliens[i][j].set_total_duration(800)
                self.aliens[i][j].play()