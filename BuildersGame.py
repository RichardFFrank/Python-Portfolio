# Author: Richard Frank
# Date: 12/1/2020
# Description: This program creates the builders game allowing players to move plays around a 5x5 board and build tiers.
# The first player on a space with 3 tiers is the winner.


class BuildersGame:
    """This class allows the user to play the builders game."""

    def __init__(self):
        """This function initializes the Builders Game ("E" = empty space)"""
        game_board = []
        player_board = []
        for column in range(5):
            player_board.append(["E"] * 5)
        for column in range(5):
            game_board.append([0] * 5)
        self._game_board = game_board
        self._player_board = player_board
        self._current_state = "UNFINISHED"
        self._current_player = "x"
        self._turn_count = 0
        self._builder_x_1 = {"row": "empty", "column": "empty"}
        self._builder_x_2 = {"row": "empty", "column": "empty"}
        self._builder_o_1 = {"row": "empty", "column": "empty"}
        self._builder_o_2 = {"row": "empty", "column": "empty"}

    def get_current_state(self):
        """This function returns the current state of the Builders Game"""
        return self._current_state

    def swap_turns(self):
        """This function changes turns after a player make their move"""
        if self._current_player == "x":
            self._current_player = "o"
        elif self._current_player == "o":
            self._current_player = "x"
        else:
            return False

    def check_rows_and_columns(self, row_1, column_1, row_2, column_2):
        """This function check to see if the rows and columns selected are in the bounds of the game."""
        if -1 < row_1 < 5 and -1 < column_1 < 5 and -1 < row_2 < 5 and -1 < column_2 < 5:
            return True
        else:
            return False

    def check_occupation(self, row, column):
        """This function checks if the space is occupied by another player"""
        if row > 4 and column > 4:
            if self._player_board[4][4] == "E":
                return True
            else:
                return False
        elif row < 0 and column < 0:
            if self._player_board[0][0] == "E":
                return True
            else:
                return False
        elif row > 4:
            if self._player_board[4][column] == "E":
                return True
            else:
                return False
        elif column > 4:
            if self._player_board[row][4] == "E":
                return True
            else:
                return False
        elif row < 0:
            if self._player_board[0][column] == "E":
                return True
            else:
                return False
        elif column < 0:
            if self._player_board[row][0] == "E":
                return True
            else:
                return False
        else:
            if self._player_board[row][column] == "E":
                return True

    def check_if_space_in_range(self, current_row, current_column, new_row, new_column):
        """This function determines if the move that will be made is in the appropriate range"""
        if -1 <= new_row - current_row <= 1 and -1 <= new_column - current_column <= 1:
            if self.check_occupation(new_row, new_column):
                return True
            else:
                return False
        else:
            return False

    def test_winner(self, new_row, new_column):
        """This function determines if the turn that was made causes a change in game state."""
        if self._game_board[new_row][new_column] == 3 and self._player_board[new_row][new_column] == self._current_player:
            if self._current_player == "x":
                self._current_state = "X_WON"
            elif self._current_player == "o":
                self._current_state = "O_WON"
        else:
            return

    def turn_is_correct(self, row, column):
        """This function checks if the builder being moved is correct and if it is their turn."""
        if self.get_current_state() == "UNFINISHED":
            if self._current_player == self._player_board[row][column]:
                return True
            else:
                return False
        else:
            return False

    def initial_placement(self, row_1, column_1, row_2, column_2, player):
        """This function allows players to be added to the board in unique positions."""
        if not(row_1 == row_2 and column_1 == column_2):
            if self.check_rows_and_columns(row_1, column_1, row_2, column_2):
                if self.check_occupation(row_1, column_1) and self.check_occupation(row_2, column_2):
                    if self._turn_count == 0:
                        if self._current_player == "x" and player == "x":
                            self._player_board[row_1][column_1] = player
                            self._builder_x_1["row"] = row_1
                            self._builder_x_1["column"] = column_1
                            self._player_board[row_2][column_2] = player
                            self._builder_x_2["row"] = row_2
                            self._builder_x_2["column"] = column_2
                            self.swap_turns()
                            self._turn_count += 1
                            return True
                        else:
                            return False
                    elif self._turn_count == 1:
                        if self._current_player == "o" and player == "o":
                            self._player_board[row_1][column_1] = player
                            self._builder_o_1["row"] = row_1
                            self._builder_o_1["column"] = column_1
                            self._player_board[row_2][column_2] = player
                            self._builder_o_2["row"] = row_2
                            self._builder_o_2["column"] = column_2
                            self.swap_turns()
                            self._turn_count += 1
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def _move_player(self, current_row, current_column, new_row, new_column):
        """This function moves the builder piece."""
        if self._game_board[new_row][new_column] - self._game_board[current_row][current_column] <= 1:
            self._player_board[current_row][current_column] = "E"
            self._player_board[new_row][new_column] = self._current_player
            if self._current_player == "x":
                if self._builder_x_1["row"] == current_row and self._builder_x_1["column"] == current_column:
                    self._builder_x_1["row"] = new_row
                    self._builder_x_1["column"] = new_column
                    return True
                elif self._builder_x_2["row"] == current_row and self._builder_x_2["column"] == current_column:
                    self._builder_x_2["row"] = new_row
                    self._builder_x_2["column"] = new_column
                    return True
            elif self._current_player == "o":
                if self._builder_o_1["row"] == current_row and self._builder_o_1["column"] == current_column:
                    self._builder_o_1["row"] = new_row
                    self._builder_o_1["column"] = new_column
                    return True
                elif self._builder_o_2["row"] == current_row and self._builder_o_2["column"] == current_column:
                    self._builder_o_2["row"] = new_row
                    self._builder_o_2["column"] = new_column
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def move_is_available(self):
        """This function determines if there is a move available for the the selected player to move."""
        available_spaces = 0
        if self._current_player == "x":
            for row in range(-1, 2):
                for column in range(-1, 2):
                    if self.check_occupation(self._builder_x_1["row"] + row, self._builder_x_1["column"] + column):
                        available_spaces += 1
                    if self.check_occupation(self._builder_x_2["row"] + row, self._builder_x_2["column"] + column):
                        available_spaces += 1
        if self._current_player == "o":
            for row in range(-1, 2):
                for column in range(-1, 2):
                    if self.check_occupation(self._builder_o_1["row"] + row, self._builder_o_1["column"] + column):
                        available_spaces += 1
                    if self.check_occupation(self._builder_o_2["row"] + row, self._builder_o_2["column"] + column):
                        available_spaces += 1
        if available_spaces == 0:
            if self._current_player == "x":
                self._current_state = "O_WON"
                return True
            elif self._current_player == "o":
                self._current_state = "X_WON"
                return True
        else:
            return True

    def build(self, current_row, current_column, build_row, build_column):
        """This function builds one level of a tower."""
        if abs(current_row - build_row) < 2 and abs(current_column - build_column) < 2 and 0 <= build_row <= 4 and 0 <= build_column <= 4:
            if self._player_board[build_row][build_column] == "E":
                if self._game_board[build_row][build_column] < 5:
                    self._game_board[build_row][build_column] += 1
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def make_move(self, current_row, current_column, new_row, new_column, build_row, build_column):
        """This function executes the move if all required conditions are met."""
        if self.turn_is_correct(current_row, current_column):
            if self.move_is_available():
                if self.check_occupation(new_row, new_column):
                    if self.check_if_space_in_range(current_row, current_column, new_row, new_column):
                        if self._move_player(current_row, current_column, new_row, new_column):
                            if self.build(new_row, new_column, build_row, build_column):
                                self.test_winner(new_row, new_column)
                                self.swap_turns()
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

