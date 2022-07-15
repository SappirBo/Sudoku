import unittest
from src.GameBoard import *


class MyTestCase(unittest.TestCase):
    # Test Create New Board and Using At function.
    def CreateBoard(self):
        g = GameBoard()
        for i in range(0, 9):
            for j in range(0, 9):
                self.assertEqual(g.at(i, j) == 0)

    # def test_something(self):
    #     self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
