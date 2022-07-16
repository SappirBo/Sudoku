from src.GameBoard import *
import random

class game:
    def __init__(self, game_difficulty: int):
        self.difficulty = int(game_difficulty)
        self.board_full = GameBoard()
        self.board_partial = GameBoard()

    def initiolize_game(self):
        self.board_full.fill_board()
        filled_slots = int(30/self.difficulty)
        for times in range(filled_slots):
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            self.board_partial[i][j] = self.board_full[i][j]

    def move(self,row: int, column: int ,number: int ):
        if number >= 10 or number <= 0:
            raise Exception("Invalid Number")
        if row >=10 or row <= 0:
            raise Exception("Invalid Row")
        if column >=10 or column <= 0:
            raise Exception("Invalid Column")
        row -= 1
        column -= 1
        if self.board_full[row][column] == number and self.board_partial[row][column] == 0:
            self.board_partial[row][column] == number
        if self.game_stats() == True:
            print("Game Over")

    def game_stats(self):
        for i in range(9):
            for j in range(9):
                if self.board_partial[i][j] == 0:
                    return False
        return True

    def print_game(self):
        self.board_partial.print_board()

