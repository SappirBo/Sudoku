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


class myLayout(Widget):
    this_game = game(1)

    def start_game(self):

        this_game = game(3)


    def clear(self):
        self.ids.calc_input.text = ''

    # button pressing function
    def button_press(self, button):
        prev = self.ids.calc_input.text
        if prev == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text += f'{button}'



class clacApp(App):
    def build(self):
        return myLayout()


if __name__ == '__main__':
    clacApp().run()