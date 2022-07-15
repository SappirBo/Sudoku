
BOARD_SIZE = 9


class GameBoard:
    def __init__(self):
        self.board = [[0 for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE) ]
        self.create_board()

    def create_board(self):
        for i in range(0, 9):
            for j in range(0,9):
                self.board[i][j] = 0

    def at(self,row: int, column: int) -> int:
        return self.board[row][column]



    def print_board(self):
        for line in self.board:
            print(line)
        print("__________________________________________________________________")
