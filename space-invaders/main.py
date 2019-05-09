from PPlay.window import Window
from menu import Menu
from play import Play

import globals

def main():
    window = Window(globals.WIDTH, globals.HEIGHT)
    window.set_title("Space Invaders")
    window.set_background_color((0,0,0))

    menu = Menu(window)
    play = Play(window)

    window.update()
    while globals.GAME_STARTED:
        window.set_background_color((0,0,0))

        if globals.GAME_STATE == 0:
            menu.run()
        elif globals.GAME_STATE == 1:
            play.run()

        window.update()

if __name__ == "__main__":
    main()