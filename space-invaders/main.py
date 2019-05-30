from PPlay.keyboard import Keyboard
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

        if globals.GAME_OVER:
            play.__init__(window)
            globals.GAME_OVER = False

        if globals.SHOW_FPS:
            window.draw_text(
                'FPS: {}'.format(1/window.delta_time()),
                globals.SCREEN_BORDER,
                globals.SCREEN_BORDER,
                color=(255,255,255)
            )

        if globals.GAME_STATE == 0:
            menu.run()
        elif globals.GAME_STATE == 1:
            play.run()

        window.update()

if __name__ == "__main__":
    main()