from PPlay.window import Window
from PPlay.sprite import Sprite
from PPlay.keyboard import Keyboard


def main():
    HEIGHT = 600
    WIDTH = 800
    VEL_X = 200
    VEL_Y = 200

    window = Window(WIDTH, HEIGHT)
    keyboard = Keyboard()

    ball = Sprite("./assets/ball.png")
    ball.set_position((window.width/2 - ball.width/2), (window.height/2 - ball.height/2))

    bat_player = Sprite("./assets/bat.png")
    bat_player.set_position(15, (window.height/2 - bat_player.height/2))

    bat_npc = Sprite("./assets/bat.png")
    bat_npc.set_position((window.width - 15) - bat_npc.width,
                         (window.height/2 - bat_npc.height/2))

    game_started = False
    player_score = 0
    npc_score = 0

    window.set_background_color((0,0,0))
    window.draw_text("{} {}".format(player_score, npc_score),
                        window.width / 2, 15, 25, (255,255,255))
    ball.draw()
    bat_player.draw()
    bat_npc.draw()

    while True:
        # to start the game
        if keyboard.key_pressed("space") or game_started:
            ball.x += (VEL_X * window.delta_time())
            ball.y += (VEL_Y * window.delta_time())
            game_started = True

        # scoring and reset after left and right window collision
        if (ball.x < 0) or (ball.x + ball.width > window.width):
            if ball.x < 0:
                npc_score += 1
            elif ball.x + ball.width > window.width:
                player_score += 1

            ball.set_position((window.width/2 - ball.width/2), (window.height/2 - ball.height/2))
            bat_player.set_position(15, (window.height/2 - bat_player.height/2))
            bat_npc.set_position((window.width - 15) - bat_npc.width,
                                (window.height/2 - bat_npc.height/2))

            game_started = False

            window.set_background_color((0,0,0))
            window.draw_text("{} {}".format(player_score, npc_score),
                                window.width / 2, 15, 25, (255,255,255))
            ball.draw()
            bat_player.draw()
            bat_npc.draw()
            window.update()
            continue
        
        # bottom and top window collision
        if ball.y < 0:
            VEL_Y *= -1
            ball.set_position(ball.x, ball.y + 1)
        elif ball.y + ball.height > window.height:
            VEL_Y *= -1
            ball.set_position(ball.x, ball.y - 1)

        # bat collision
        if bat_player.collided(ball):
            VEL_X *= -1
            ball.set_position(ball.x + 1, ball.y)
        elif bat_npc.collided(ball):
            VEL_X *= -1
            ball.set_position(ball.x - 1, ball.y)
        
        # controls
        if keyboard.key_pressed("up") and bat_player.y > 15:
                bat_player.y -= 0.5
        if (keyboard.key_pressed("down") and 
           (bat_player.y + bat_player.height < window.height - 15)):
                bat_player.y += 0.5
        
        # AI
        if (ball.y < window.height/2 and 
            bat_npc.y > 15 and 
            game_started):
            bat_npc.y -= 0.5
        elif (ball.y > window.height/2 and 
              bat_npc.y + bat_npc.height < window.height - 15 and 
              game_started):
            bat_npc.y += 0.5

        # reset
        window.set_background_color((0,0,0))
        window.draw_text("{} {}".format(player_score, npc_score),
                            window.width / 2, 15, 25, (255,255,255))
        ball.draw()
        bat_player.draw()
        bat_npc.draw()
        window.update()

if __name__ == "__main__":
    main()