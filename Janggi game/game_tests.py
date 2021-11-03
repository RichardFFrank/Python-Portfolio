import unittest
from JanggiGame import *

class TestListLibrary(unittest.TestCase):

    def test_failed_horse(self):
        game = JanggiGame()
        self.assertTrue(game.make_move('c10', 'd8'))
        self.assertTrue(game.make_move('c1', 'd3'))
        self.assertTrue(game.make_move('e7', 'e6'))
        self.assertTrue(game.make_move('e4', 'e5'))
        self.assertTrue(game.make_move('c7', 'c6'))
        self.assertTrue(game.make_move('c4', 'c5'))
        self.assertTrue(game.make_move('c6', 'c5'))
        self.assertTrue(game.make_move('e5', 'e6'))
        self.assertTrue(game.make_move('d8', 'e5'))

    def test_horse_own_piece(self):
        game = JanggiGame()
        self.assertTrue(game.make_move('c10', 'd8'))
        self.assertTrue(game.make_move('c1', 'd3'))
        self.assertTrue(game.make_move('c7', 'd7'))
        self.assertTrue(game.make_move('c4', 'd4'))
        self.assertFalse(game.make_move('d8', 'c6'))
        # Test Failed: Blue horse from west should not be able to jump over a blue piece

    def test_horse_capture(self):
        game = JanggiGame()
        self.assertTrue(game.make_move('c10', 'd8'))
        self.assertTrue(game.make_move('c1', 'd3'))
        self.assertTrue(game.make_move('e7', 'e6'))
        self.assertTrue(game.make_move('e4', 'e5'))
        self.assertTrue(game.make_move('c7', 'c6'))
        self.assertTrue(game.make_move('c4', 'c5'))
        self.assertTrue(game.make_move('c6', 'c5'))
        self.assertTrue(game.make_move('e5', 'e6'))
        self.assertTrue(game.make_move('d8', 'e6'))
        self.assertTrue(game.make_move('d3', 'c5'))
        self.assertTrue(game.make_move('h10', 'g8'))
        self.assertTrue(game.make_move('h1', 'i3'))
        self.assertTrue(game.make_move('g7', 'h7'))
        self.assertTrue(game.make_move('g4', 'f4'))
        self.assertTrue(game.make_move('h7', 'h6'))
        self.assertTrue(game.make_move('i4', 'i5'))
        self.assertTrue(game.make_move('h6', 'h6'))
        self.assertTrue(game.make_move('i5', 'i6'))
        self.assertTrue(game.make_move('d8', 'e6'))
        self.assertTrue(game.make_move('g8', 'g8'))
        self.assertTrue(game.make_move('i3', 'h5'))
        #Test Failed: Red Horse from East should be able to capture a Blue Soldier

    def test_check_blue(self):
        game = JanggiGame()
        self.assertTrue(game.make_move('c7', 'c6'))
        self.assertTrue(game.make_move('c1', 'd3'))
        self.assertTrue(game.make_move('b10', 'd7'))
        self.assertTrue(game.make_move('b3', 'e3'))
        self.assertTrue(game.make_move('c10', 'd8'))
        self.assertTrue(game.make_move('h1', 'g3'))
        self.assertTrue(game.make_move('e7', 'e6'))
        self.assertTrue(game.make_move('e3', 'e6'))
        self.assertFalse(game.is_in_check("red"))
        self.assertTrue(game.make_move('h8', 'c8'))
        self.assertTrue(game.make_move('d3', 'e5'))
        self.assertTrue(game.make_move('c8', 'c4'))
        self.assertTrue(game.make_move('e5', 'c4'))
        self.assertTrue(game.make_move('i10', 'i8'))
        self.assertTrue(game.make_move('g4', 'f4'))
        self.assertTrue(game.make_move('i8', 'f8'))
        self.assertTrue(game.make_move('g3', 'h5'))
        self.assertTrue(game.make_move('h10', 'g8'))
        self.assertTrue(game.make_move('e6', 'e3'))
        print(game.get_game_state())
        self.assertTrue(game.make_move('e9', 'd9'))
        print(game.get_game_state())


    def test_general_1(self):
        game = JanggiGame()
        self.assertTrue(game.make_move('e9', 'f8'))
        self.assertTrue(game.make_move('e2', 'f3'))
        self.assertTrue(game.make_move('f8', 'e8'))
        self.assertTrue(game.make_move('f3', 'e3'))
        self.assertTrue(game.make_move('e8', 'd8'))
        self.assertTrue(game.make_move('e3', 'd3'))
        self.assertTrue(game.make_move('d8', 'd9'))
        self.assertTrue(game.make_move('d3', 'd2'))
        self.assertTrue(game.make_move('d9', 'e9'))
        self.assertTrue(game.make_move('d2', 'e2'))
        self.assertTrue(game.make_move('e9', 'e10'))
        self.assertTrue(game.make_move('e2', 'e1'))
# Attempting:  e9 -> f8
# Attempting:  e2 -> f3
# Attempting:  f8 -> g8
# Attempting:  f8 -> f8
# Attempting:  f3 -> f4
# Attempting:  f3 -> f3
# Attempting:  f10 -> e10

# Test Failed: Blue General is in check and is_in_check should return True for blue