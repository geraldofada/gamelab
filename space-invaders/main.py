from PPlay.window import Window
from menu import Menu
import globals

def main():
    window = Window(globals.WIDTH, globals.HEIGHT)
    window.set_background_color((0,0,0))

    menu = Menu(window)

    window.update()
    while globals.GAME_STARTED:
        menu.draw()
        window.set_background_color((0,0,0))
        window.update()

if __name__ == "__main__":
    main()