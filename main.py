from function import *

print(start_logo)
if input("Do you want to play Black Jack? Type 'y' or 'n': ") == 'y':
    stop_game = False
    while not stop_game:
        play_game()
        print(gameover_logo)
        if input("Do you want to play again? Type 'y' or 'n': ") == 'y':
            cls()
        else:
            stop_game = True
else:
    print(game_exit)