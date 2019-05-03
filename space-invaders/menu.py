from PPlay.sprite import Sprite


class Menu(object):
    def __init__(self, window):
        self.window = window
        self.play = Sprite("./assets/menu/play.png")
        self.difficulty = Sprite("./assets/menu/play.png")
        self.rank = Sprite("./assets/menu/play.png")
        self.quit = Sprite("./assets/menu/play.png")
        self.__set_pos()
    
    def draw(self):
        self.play.draw()
        self.difficulty.draw()
        self.rank.draw()
        self.quit.draw()
    
    def __set_pos(self):
        self.play.set_position(400, 15)