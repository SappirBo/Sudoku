from src.GameBoard import *
from src.game import game
import os


def run():
    print("Start Game")
    diff = input("Difficulty ?")
    print(" ")
    current_game = game(diff)
    current_game.initiolize_game()
    while current_game.game_stats() == False:
        os.system('cls')
        print(" ")
        current_game.print_game()
        see_ans = input("Do Yo Wish To See Solution? (yes = 1) ")
        if see_ans == "1":
            current_game.board_partial.board = current_game.board_full.board
            os.system('cls')
            print(" ")
            current_game.print_game()
        else:
            next_move_x = int(input("next x?"))
            next_move_y = int(input("next y?"))
            next_move_number = int(input("number?"))
            current_game.move(next_move_x,next_move_y,next_move_number)

if __name__ == "__main__":
    run()