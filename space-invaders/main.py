from PPlay.keyboard import Keyboard
from PPlay.window import Window
from menu import Menu
from play import Play

import globals

def main():
    window = Window(globals.WIDTH, globals.HEIGHT)
    window.set_title("Space Invaders")
    window.set_background_color((0,0,0))

    keyboard = Keyboard()

    menu = Menu(window)
    play = Play(window)

    window.update()
    while globals.GAME_STARTED:
        window.set_background_color((0,0,0))

        if keyboard.key_pressed("esc")  and globals.GAME_STATE == 1:
            globals.GAME_STATE = 0
            play.__init__(window)
            window.delay(100)
        elif keyboard.key_pressed("esc") and globals.GAME_STATE == 0:
            globals.GAME_STARTED = False

        if globals.GAME_STATE == 0:
            menu.run()
        elif globals.GAME_STATE == 1:
            play.run()

        window.update()

if __name__ == "__main__":
    main()