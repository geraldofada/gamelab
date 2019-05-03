from PPlay.sprite import Sprite


class Menu(object):
    def __init__(self, window):
        self.window = window
        self.play = Sprite("./assets/menu/play.png")
        self.difficulty = Sprite("./assets/menu/play.png")
        self.rank = Sprite("./assets/menu/play.png")
        self.quit = Sprite("./assets/menu/play.png")
        self.__set_pos()
    
    def run(self):
        self.__draw()

    def __draw(self):
        self.play.draw()
        self.difficulty.draw()
        self.rank.draw()
        self.quit.draw()
    
    def __set_pos(self):
        self.play.set_position(self.window.width/2 - self.play.width/2,
                               self.play.height*1 + 30*1)

        self.difficulty.set_position(self.window.width/2 - self.difficulty.width/2, 
                                     self.difficulty.height*2 + 30*2)

        self.rank.set_position(self.window.width/2 - self.rank.width/2,
                               self.rank.height*3 + 30*3)

        self.quit.set_position(self.window.width/2 - self.quit.width/2,
                               self.quit.height*4 + 30*4)