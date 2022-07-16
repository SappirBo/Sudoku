import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from src.game import *
from src.GameBoard import *

# Setting up size of the up
Window.size = (800, 400)
# Setting Up the kv file
Builder.load_file('game_gui.kv')

curr_game = game(1)


class myLayout(Widget):

    def clear_board(self):
        for row in range(9):
            for col in range(9):
                    row_str = str(row)
                    col_str = str(col)
                    key = "n" + row_str + col_str
                    self.ids[key].text = ""

    def start_game_easy(self):
        curr_game = game(1)
        self.clear_board()
        for row in range(9):
            for col in range(9):
                if curr_game.board_partial.board[row][col] != 0:
                    row_str = str(row)
                    col_str = str(col)
                    key = "n" + row_str + col_str
                    self.ids[key].text = str(curr_game.board_partial.board[row][col])

    # button pressing function
    # def move(self, button):



class clacApp(App):
    def build(self):
        return myLayout()


if __name__ == '__main__':
    clacApp().run()
