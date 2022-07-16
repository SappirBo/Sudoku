import random
from random import shuffle
BOARD_SIZE = 9
table = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(table)

class GameBoard:
    def __init__(self):
        self.board = [[0 for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]
        self.create_board()

    def create_board(self):
        for i in range(0, 9):
            for j in range(0, 9):
                self.board[i][j] = 0

    def check_board(self) -> bool:
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        return True

    def at(self, row: int, column: int) -> int:
        return self.board[row][column]

    def possible(self, x, y, n) -> bool:
        # check row and column.
        for i in range(9):
            if self.board[x][i] == n:
                return False
            if self.board[i][y] == n:
                return False
        # checking the 3X3 table of this position.
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[x0 + i][y0 + j] == n:
                    return False
        return True

    def ad_numbers(self):
        for i in range(30):
            i = random.randint(0,8)
            j = random.randint(0,8)
            for number in table:
                if self.possible(i, j, number):
                    self.board[i][j] = number

    def fill_board(self)->bool:
        if self.check_board() is True:
            return True
        else:
            for i in range(9):
                for j in range(9):
                    if self.board[i][j] == 0:
                        for number in table:
                            if self.possible(i, j, number):
                                self.board[i][j] = number
                                if self.fill_board() is True:
                                    return True
                                else:
                                    self.board[i][j] = 0
                        return
            return True

    def print_board(self):
        for line in self.board:
            print(line)
        print("__________________________________________________________________")
