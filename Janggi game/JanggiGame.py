# Author: Richard Frank
# Date: 03/07/2021
# Description: This program contains all functionality to play a basic game of Janggi in python.
# All standard pieces and rules have been implemented.


class JanggiGame:
    """This class contains the primary functionality in which the game is play. Methods include an initialization
    of the game board and placement of pieces at their standard locations. The ability to move pieces and return the
    games current state."""

    def __init__(self):
        """Initializes the Janggi board, places the pieces on the board, sets the game state,
        sets the check status of both players, and sets the current turn."""
        game_state = ['UNFINISHED', 'RED_WON', 'BLUE_WON']
        players = ['RED', 'BLUE']
        self._game_state = game_state[0]
        self._player_turn = players[1]
        self._blue_check = False
        self._red_check = False
        self._red_general_location = 'e2'
        self._blue_general_location = 'e9'
        self._player_board = {
            'A': {1: {'piece': Chariot("RED"), 'type': None}, 2: {'piece': None, 'type': None}, 3: {'piece': None, 'type': None},
                  4: {'piece': Soldier("RED"), 'type': None}, 5: {'piece': None, 'type': None}, 6: {'piece': None, 'type': None},
                  7: {'piece': Soldier("BLUE"), 'type': None}, 8: {'piece': None, 'type': None}, 9: {'piece': None, 'type': None},
                  10: {'piece': Chariot("BLUE"), 'type': None}},
            'B': {1: {'piece': Elephant("RED"), 'type': None}, 2: {'piece': None, 'type': None}, 3: {'piece': Cannon("RED"), 'type': None},
                  4: {'piece': None, 'type': None}, 5: {'piece': None, 'type': None}, 6: {'piece': None, 'type': None},
                  7: {'piece': None, 'type': None}, 8: {'piece': Cannon("BLUE"), 'type': None}, 9: {'piece': None, 'type': None},
                  10: {'piece': Elephant("BLUE"), 'type': None}},
            'C': {1: {'piece': Horse("RED"), 'type': None}, 2: {'piece': None, 'type': None},
                  3: {'piece': None, 'type': None}, 4: {'piece': Soldier("RED"), 'type': None},
                  5: {'piece': None, 'type': None}, 6: {'piece': None, 'type': None},
                  7: {'piece': Soldier("BLUE"), 'type': None}, 8: {'piece': None, 'type': None},
                  9: {'piece': None, 'type': None}, 10: {'piece': Horse("BLUE"), 'type': None}},
            'D': {1: {'piece': Guard("RED"), 'type': "PALACE", 'Status': None}, 2: {'piece': None, 'type': "PALACE", 'Status': None},
                  3: {'piece': None, 'type': "PALACE", 'Status': None}, 4: {'piece': None, 'type': None},
                  5: {'piece': None, 'type': None}, 6: {'piece': None, 'type': None},
                  7: {'piece': None, 'type': None}, 8: {'piece': None, 'type': "PALACE", 'Status': None},
                  9: {'piece': None, 'type': "PALACE", 'Status': None}, 10: {'piece': Guard("BLUE"), 'type': "PALACE", 'Status': None}},
            'E': {1: {'piece': None, 'type': "PALACE", 'Status': None},
                  2: {'piece': General("RED"), 'type': "PALACE", 'Status': None},
                  3: {'piece': None, 'type': "PALACE", 'Status': None}, 4: {'piece': Soldier("RED"), 'type': None},
                  5: {'piece': None, 'type': None}, 6: {'piece': None, 'type': None},
                  7: {'piece': Soldier("BLUE"), 'type': None}, 8: {'piece': None, 'type': "PALACE", 'Status': None},
                  9: {'piece': General("BLUE"), 'type': "PALACE", 'Status': None}, 10: {'piece': None, 'type': "PALACE", 'Status': None}},
            'F': {1: {'piece': Guard("RED"), 'type': "PALACE", 'Status': None},
                  2: {'piece': None, 'type': "PALACE", 'Status': None},
                  3: {'piece': None, 'type': "PALACE", 'Status': None}, 4: {'piece': None, 'type': None},
                  5: {'piece': None, 'type': None}, 6: {'piece': None, 'type': None},
                  7: {'piece': None, 'type': None}, 8: {'piece': None, 'type': "PALACE", 'Status': None},
                  9: {'piece': None, 'type': "PALACE", 'Status': None}, 10: {'piece': Guard("BLUE"), 'type': "PALACE", 'Status': None}},
            'G': {1: {'piece': Elephant("RED"), 'type': None}, 2: {'piece': None, 'type': None}, 3: {'piece': None, 'type': None},
                  4: {'piece': Soldier("RED"), 'type': None}, 5: {'piece': None, 'type': None}, 6: {'piece': None, 'type': None},
                  7: {'piece': Soldier("BLUE"), 'type': None}, 8: {'piece': None, 'type': None}, 9: {'piece': None, 'type': None},
                  10: {'piece': Elephant("BLUE"), 'type': None}},
            'H': {1: {'piece': Horse("RED"), 'type': None}, 2: {'piece': None, 'type': None},
                  3: {'piece': Cannon("RED"), 'type': None}, 4: {'piece': None, 'type': None},
                  5: {'piece': None, 'type': None}, 6: {'piece': None, 'type': None},
                  7: {'piece': None, 'type': None}, 8: {'piece': Cannon("BLUE"), 'type': None},
                  9: {'piece': None, 'type': None}, 10: {'piece': Horse("BLUE"), 'type': None}},
            'I': {1: {'piece': Chariot("RED"), 'type': None}, 2: {'piece': None, 'type': None},
                  3: {'piece': None, 'type': None}, 4: {'piece': Soldier("RED"), 'type': None},
                  5: {'piece': None, 'type': None}, 6: {'piece': None, 'type': None},
                  7: {'piece': Soldier("BLUE"), 'type': None}, 8: {'piece': None, 'type': None},
                  9: {'piece': None, 'type': None}, 10: {'piece': Chariot("BLUE"), 'type': None}},
        }

    def get_board(self):
        """Returns the player board, for use in move validity in the individual classes"""
        return self._player_board

    def show_board(self):
        """Prints the current state of the player board."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

        for val in alpha_list:
            row = []
            for num in range(1, 11):
                row += val, [num, self._player_board.get(val).get(num)]
            print(row)

    def get_turn(self):
        """Returns the value of the player_turn data member. Keeps track of the player who
        can move at the point it is called."""
        return self._player_turn

    def swap_turns(self):
        """Changes the _player_turn datamamber for the Janggi game to the opposing player.
        This method is called after a successful move is completed."""
        if self.get_turn() == "BLUE":
            self._player_turn = "RED"
        else:
            self._player_turn = "BLUE"

    def get_game_state(self):
        """Returns the current state of the game, possibilities are 'UNFINISHED' or 'RED_WON' or 'BLUE_WON'"""
        return self._game_state

    def set_game_state(self, winner):
        """Changes the game state to the winner of the game. The game is set to UNFINISHED by default."""
        if winner.upper() == "RED":
            self._game_state = "RED_WON"
        if winner.upper() == "BLUE":
            self._game_state = "BLUE_WON"

    def get_check_status(self, position):
        """returns the check status of a piece. Only called on Palace pieces."""
        col = position[0].upper()
        row = int(position[1:])
        if self._player_board[col][row]['type'] == "PALACE":
            return self._player_board[col][row]['Status']

    def is_in_check(self, player):
        """Returns True if the player is in check and returns false if the player is not in check."""
        if player.upper() == "RED":
            return self._red_check
        elif player.upper() == "BLUE":
            return self._blue_check
        else:
            return

    def get_general_location(self, color):
        """Returns the current location of the general who is being passed."""
        if color.upper() == "RED":
            return self._red_general_location
        elif color.upper() == "BLUE":
            return self._blue_general_location
        else:
            return

    def set_general_location(self, color, location):
        """Sets the current location of the general who is being passed."""
        if color.upper() == "RED":
            self._red_general_location = location
        elif color.upper() == "BLUE":
            self._blue_general_location = location
        else:
            return

    def set_red_check(self):
        """Sets the value of the red_check datamember to True."""
        self._red_check = True

    def set_blue_check(self):
        """Sets the value of the blue_check datamember to True."""
        self._blue_check = True

    def remove_red_check(self):
        """Sets the value of the red_check datamember to False."""
        self._red_check = False

    def remove_blue_check(self):
        """Sets the value of the blue_check datamember to False."""
        self._blue_check = False

    def set_check(self, position):
        """Sets the status of a provided board piece to 'IN_CHECK'"""
        col = position[0].upper()
        row = int(position[1:])
        self._player_board[col][row]['Status'] = "IN_CHECK"

    def remove_check(self, position):
        """Sets the status of a provided board piece to None"""
        col = position[0].upper()
        row = int(position[1:])
        self._player_board[col][row]['Status'] = None

    def clear_board(self):
        """Clears the check status of all pieces within the palace."""
        red_palace = ["d1", "d2", "d3", "e1", "e2", "e3", "f1", "f2", "f3"]
        blue_palace = ["d8", "d9", "d10", "e8", "e9", "e10", "f8", "f9", "f10"]

        for value in red_palace:
            self.remove_check(value)

        for value in blue_palace:
            self.remove_check(value)

    def set_board_check(self):
        """Set's the check state of all pieces in the palace depending on the current state of the board."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        piece_list = []
        for value in alpha_list:
            for item in range(1, 11):
                if self._player_board[value][item]["piece"] is not None and type(self._player_board[value][item]["piece"]) is not General:
                    piece_list.append(str(value) + str(item))

        for piece in piece_list:
            self.determine_spaces_in_check(piece)


    def determine_spaces_in_check(self, end_pos):
        """This method is called after at the end of a players turn, once the move has been validated and the piece has been moved.
        This leverages the valid_move function, using the end_position of the current move as the start position of the next move.
        Then it cycles through the palace coordinates to determine if the piece could reach that space on the next turn. If True, the
        space "status" is set to "IN_CHECK"."""

        red_palace = ["d1", "d2", "d3", "e1", "e2", "e3", "f1", "f2", "f3"]
        blue_palace = ["d8", "d9", "d10", "e8", "e9", "e10", "f8", "f9", "f10"]

        current_piece = self.get_piece(end_pos)

        if current_piece.get_player() == "RED":
            for val in blue_palace:
                if current_piece.valid_move(end_pos, val, self.get_space_type(end_pos), self.get_board()):
                    self.set_check(val)
                    if type(self.get_piece(val)) is General:
                        if self.get_piece(val).set_general_check():
                            self.set_blue_check()
        elif current_piece.get_player() == "BLUE":
            for val in red_palace:
                if current_piece.valid_move(end_pos, val, self.get_space_type(end_pos), self.get_board()):
                    self.set_check(val)
                    if type(self.get_piece(val)) is General:
                        if self.get_piece(val).set_general_check():
                            self.set_red_check()
        else:
            return

    def is_occupied(self, position):
        """Determines if a space on the board is currently occupied."""
        col = position[0].upper()
        row = int(position[1:])
        if self._player_board[col][row]['piece'] is not None:
            return False
        return True

    def get_piece(self, position):
        """Returns the piece at a given position."""
        col = position[0].upper()
        row = int(position[1:])
        return self._player_board[col][row]['piece']

    def get_space_type(self, position):
        """Returns the space type on the board, none for regular space, 'Palace' for
        palace spaces."""
        start_col = position[0].upper()
        start_row = int(position[1:])
        return self._player_board[start_col][int(start_row)]['type']

    def move_piece(self, start_pos, end_pos):
        """Move the piece at the start position to the end position.
        If a piece is at the end position, it is overwritten (captured)"""
        start_col = start_pos[0].upper()
        start_row = start_pos[1:]
        piece = self._player_board[start_col][int(start_row)]['piece']
        self._player_board[start_col][int(start_row)]['piece'] = None
        end_col = end_pos[0].upper()
        end_row = end_pos[1:]
        self._player_board[end_col][int(end_row)]['piece'] = piece
        if type(self.get_piece(end_pos)) is General:
            self.set_general_location(self.get_piece(end_pos).get_player(), end_pos)

    def evaluate_checkmate(self, general_location):
        """This method tests all possible moves for a general and if no moves are valid, declares a checkmate."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        # current_player = self.get_turn()
        moving_piece = self.get_piece(general_location)
        start_col_helper = general_location[0].upper()
        start_column = alpha_list.index(start_col_helper)
        start_row = int(general_location[1:])
        possible_moves = []

        # creates the list of possible moves
        for val in range(-1, 2):
            if 9 > start_column + val > -1:
                string_potential = alpha_list[start_column + val]
                for row in range(-1, 2):
                    if 11 > start_row + row > 0:
                        string_potential += str(start_row + row)
                        possible_moves.append(string_potential)
                        string_potential = string_potential[:1]

        # tests if each move is valid
        move_count = 0
        for possible_move in possible_moves:
            if moving_piece is not None:
                if moving_piece.valid_move(general_location, possible_move, self.get_space_type(possible_move), self.get_board()):
                    move_count += 1

        #if no move is valid, changes the game state.
        if move_count == 0:
            if self.get_turn() == "RED":
                self.set_game_state("blue")
            elif self.get_turn() == "BLUE":
                self.set_game_state("red")
            else:
                return

    def get_general_location(self, color):
        """Returns the current location of the general who is being passed."""
        if color.upper() == "RED":
            return self._red_general_location
        elif color.upper() == "BLUE":
            return self._blue_general_location
        else:
            return

    def make_move(self, start_pos, end_pos):
        """Moves a piece from the starting position to the end position. This function will complete the following:
        1. Determine if the correct player is making the move.
        2. Determine if there is a piece at the starting position.
        3. Determine if the piece being moved belongs to the current player.
        4. Determine if the move is valid (right place, no player is blocking the movement).
        5. Move the piece to the end_pos and mark the start_pos as empty.
        6. Update palace check states as needed based on the board state after the move has been made."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        start_row = int(start_pos[1:])
        end_row = int(end_pos[1:])
        current_player = self.get_turn()
        moving_piece = self.get_piece(start_pos)
        piece_to_capture = self.get_piece(end_pos)
        # pass turn
        if start_pos == end_pos:
            self.swap_turns()
            return True
        # validate that rows are on the board.
        if start_row < 1 or start_row > 10 or end_row < 1 or end_row > 10:
            return False
        start_col_helper = start_pos[0].upper()
        end_col_helper = end_pos[0].upper()
        # validate that columns are on the board.
        if (start_col_helper not in alpha_list) or (end_col_helper not in alpha_list):
            return False
        # make sure there is a piece at the start location
        if moving_piece is not None:
            # makes sure the piece being moved belongs to the current player
            if current_player == moving_piece.get_player():
                # check if there is a piece at the end position.
                if piece_to_capture is None:
                    self.clear_board()
                    self.set_board_check()
                    if moving_piece.valid_move(start_pos, end_pos, self.get_space_type(end_pos), self.get_board()):
                        self.move_piece(start_pos, end_pos)
                        if type(moving_piece) is General:
                            self.set_general_location(current_player, end_pos)
                        self.clear_board()
                        self.set_board_check()
                        self.evaluate_checkmate(self.get_general_location("RED"))
                        self.evaluate_checkmate(self.get_general_location("BLUE"))
                        if type(moving_piece) is General:
                            if current_player == "RED":
                                self.remove_red_check()
                                self.swap_turns()
                                return True
                            elif current_player == "BLUE":
                                self.remove_blue_check()
                                self.swap_turns()
                                return True
                        self.swap_turns()
                        return True
                    else:
                        return False
                elif piece_to_capture is not None and piece_to_capture.get_player() != current_player:
                    if moving_piece.valid_move(start_pos, end_pos, self.get_space_type(end_pos), self.get_board()):
                        self.move_piece(start_pos, end_pos)
                        self.clear_board()
                        self.set_board_check()
                        self.evaluate_checkmate(self.get_general_location(current_player))
                        self.swap_turns()
                        if type(moving_piece) is General:
                            if current_player == "RED":
                                self.remove_red_check()
                                return True
                            elif current_player == "BLUE":
                                self.remove_blue_check()
                                return True
                        return True
                    else:
                        return False
                else:
                    return False
            return False
        return False


class Piece:
    """This class creates the various types of pieces and the functionality required to move those pieces."""

    def __init__(self, player):
        """This initializes the piece class with all required data members (starting location, color, type)"""
        self._player = player.upper()

    def valid_move(self):
        """This function determines if the move being made is valid based on the criteria of the
        individual piece."""
        pass

    def get_player(self):
        """Returns the player that the piece belongs to"""
        return self._player


class Soldier(Piece):
    """This contains the functionality required for the soldier class including the initializer,
     movement checks, getters, and setters."""

    def __init__(self, player):
        """Initializes the soldier class as if it were a piece."""
        super().__init__(player)

    def valid_move(self, start_pos, end_pos, space_type, board):
        """This function determines if the move being attempted is valid based on the rules of Soldier movement in Janggi."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        start_col_helper = start_pos[0].upper()
        start_column = alpha_list.index(start_col_helper)
        start_row = int(start_pos[1:])
        end_col_helper = end_pos[0].upper()
        end_column = alpha_list.index(end_col_helper)
        end_row = int(end_pos[1:])
        current_player = self.get_player()

        # this is this required base logic outside of the palace.
        if current_player == "RED":
            if space_type is None:
                if (start_column == end_column - 1 or start_column == end_column + 1) and start_row == end_row:
                    return True
                elif start_column == end_column and start_row == end_row - 1:
                    return True
            elif space_type == "PALACE":
                if start_column == 3:
                    if (start_column == end_column - 1 or start_column == end_column + 1) and start_row == end_row:
                        return True
                    elif start_column == end_column and start_row == end_row - 1:
                        return True
                    elif start_column == end_column - 1 and start_row == end_row - 1:
                        return True
                    else:
                        return False
                if start_column == 4:
                    # column + 1, -1, or = and end row - 1
                    if (start_column == end_column or start_column == end_column - 1 or start_column == end_column + 1) \
                            and (start_row == end_row or start_row == end_row - 1):
                        return True
                    else:
                        return False
                if start_column == 5:
                    # column + 1,
                    if (start_column == end_column - 1 or start_column == end_column + 1) and start_row == end_row:
                        return True
                    elif start_column == end_column and start_row == end_row - 1:
                        return True
                    elif start_column == end_column + 1 and start_row == end_row - 1:
                        return True
                    else:
                        return False

        elif current_player == "BLUE":
            if space_type is None:
                if (start_column == end_column - 1 or start_column == end_column + 1) and start_row == end_row:
                    return True
                elif start_column == end_column and start_row == end_row + 1:
                    return True
            elif space_type == "PALACE":
                if start_column == 3:
                    if (start_column == end_column - 1 or start_column == end_column + 1) and start_row == end_row:
                        return True
                    elif start_column == end_column and start_row == end_row + 1:
                        return True
                    elif start_column == end_column - 1 and start_row == end_row + 1:
                        return True
                    else:
                        return False
                if start_column == 4:
                    if (start_column == end_column or start_column == end_column - 1 or start_column == end_column + 1) \
                            and (start_row == end_row or start_row == end_row + 1):
                        return True
                    else:
                        return False
                if start_column == 5:
                    # column + 1,
                    if (start_column == end_column - 1 or start_column == end_column + 1) and start_row == end_row:
                        return True
                    elif start_column == end_column and start_row == end_row + 1:
                        return True
                    elif start_column == end_column + 1 and start_row == end_row + 1:
                        return True
                    else:
                        return False
        else:
            return False


class Cannon(Piece):
    """This contains the functionality required for the cannon class including the initializer and movement checks"""

    def __init__(self, player):
        """Initializes the cannon class as a subclass of the pieces class."""
        super().__init__(player)

    def valid_move(self, start_pos, end_pos, space_type, board):
        """Determines if the move being attempted is legal based on all logic related to moving to a cannon piece. Returns: Boolean.
	    True if the move is valid, false if not."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        start_col_helper = start_pos[0].upper()
        start_column = alpha_list.index(start_col_helper)
        start_row = int(start_pos[1:])
        end_col_helper = end_pos[0].upper()
        end_column = alpha_list.index(end_col_helper)
        end_row = int(end_pos[1:])
        current_player = self.get_player()

        # cannon cannot capture another cannon
        if type(board[end_col_helper][end_row]['piece']) is Cannon:
            return False

        # pass turn
        if start_row == end_row and start_column == end_column:
            return True

        # test validity.
        elif space_type is None:
            if (start_column > end_column or start_column < end_column) and start_row == end_row:
                if self.validate_horizontal_move(start_pos, end_pos, board):
                    return True
                else:
                    return False
            elif (start_row > end_row or start_row < end_row) and start_column == end_column:
                if self.validate_vertical_move(start_pos, end_pos, board):
                    return True
                else:
                    return False
        elif space_type == "PALACE":
            if (start_column > end_column or start_column < end_column) and start_row == end_row:
                if self.validate_horizontal_move(start_pos, end_pos, board):
                    return True
                else:
                    return False
            elif (start_row > end_row or start_row < end_row) and start_column == end_column:
                if self.validate_vertical_move(start_pos, end_pos, board):
                    return True
                else:
                    return False
            elif current_player == "RED" and board["E"][2]['piece'] is not None and \
                    (end_pos == "f1" or end_pos == "f3" or end_pos == "d1" or end_pos == "d3"):
                return True
            elif current_player == "BLUE" and board["E"][9]['piece'] is not None and \
                    (end_pos == "d8" or end_pos == "d10" or end_pos == "f8" or end_pos == "f10"):
                return True
        else:
            return False

    def validate_horizontal_move(self, start_pos, end_pos, board):
        """Determines if the cannon is making a valid horizontal move, if the move is valid the function
        returns True. """
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        start_col_helper = start_pos[0].upper()
        start_column = alpha_list.index(start_col_helper)
        start_row = int(start_pos[1:])
        end_col_helper = end_pos[0].upper()
        end_column = alpha_list.index(end_col_helper)
        end_row = int(end_pos[1:])
        end_counter = end_column
        if start_column < end_column:
            start_counter = start_column + 1
            piece_counter = 0
            while start_counter < end_counter:
                column = alpha_list[start_counter]
                row = start_row
                if board[column][row]['piece'] is not None:
                    piece_counter += 1
                    start_counter += 1
                else:
                    start_counter += 1
        if start_column > end_column:
            start_counter = start_column - 1
            piece_counter = 0
            while start_counter > end_counter:
                column = alpha_list[start_counter]
                row = start_row
                if board[column][row]['piece'] is not None:
                    piece_counter += 1
                    start_counter -= 1
                else:
                    start_counter -= 1

        if piece_counter == 1:
            return True
        elif piece_counter == 0 or piece_counter > 1:
            return False
        return False

    def validate_vertical_move(self, start_pos, end_pos, board):
        """Determines if the cannon is making a valid horizontal move, if the move is valid the function returns True."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        start_col_helper = start_pos[0].upper()
        start_column = alpha_list.index(start_col_helper)
        start_row = int(start_pos[1:])
        end_col_helper = end_pos[0].upper()
        end_column = alpha_list.index(end_col_helper)
        end_row = int(end_pos[1:])
        end_counter = end_row
        if start_row < end_row:
            start_counter = start_row + 1
            piece_counter = 0
            while start_counter < end_counter:
                column = start_col_helper
                row = start_counter
                if board[column][row]['piece'] is not None:
                    piece_counter += 1
                    start_counter += 1
                else:
                    start_counter += 1
        if start_row > end_row:
            start_counter = start_row - 1
            piece_counter = 0
            while start_counter > end_counter:
                column = start_col_helper
                row = start_counter
                if board[column][row]['piece'] is not None:
                    piece_counter += 1
                    start_counter -= 1
                else:
                    start_counter -= 1

        if piece_counter == 1:
            return True
        elif piece_counter == 0 or piece_counter > 1:
            return False
        return False


class Chariot(Piece):
    """This contains the functionality required for the chariot class including the initializer and movement checks"""

    def __init__(self, player):
        """Initializes the chariot class as a subclass of the pieces class."""
        super().__init__(player)

    def valid_move(self, start_pos, end_pos, space_type, board):
        """Determines if the move being attempted is legal based on all logic related to moving to a chariot piece.
        Returns: Boolean. True if the move is valid, false if not."""

        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        start_col_helper = start_pos[0].upper()
        start_column = alpha_list.index(start_col_helper)
        start_row = int(start_pos[1:])
        end_col_helper = end_pos[0].upper()
        end_column = alpha_list.index(end_col_helper)
        end_row = int(end_pos[1:])
        current_player = self.get_player()
        # cannon cannot capture another cannon
        if type(board[end_col_helper][end_row]['piece']) is Cannon:
            return False

        # test validity.
        elif space_type is None:
            if (start_column > end_column or start_column < end_column) and start_row == end_row:
                if self.validate_horizontal_move(start_pos, end_pos, board):
                    return True
                else:
                    return False
            elif (start_row > end_row or start_row < end_row) and start_column == end_column:
                if self.validate_vertical_move(start_pos, end_pos, board):
                    return True
                else:
                    return False
        elif space_type == "PALACE":
            if (start_column > end_column or start_column < end_column) and start_row == end_row:
                if self.validate_horizontal_move(start_pos, end_pos, board):
                    return True
                else:
                    return False
            elif (start_row > end_row or start_row < end_row) and start_column == end_column:
                if self.validate_vertical_move(start_pos, end_pos, board):
                    return True
                else:
                    return False
            elif current_player == "RED" and board["E"][2]['piece'] is None and \
                    (end_pos == "f1" or end_pos == "f3" or end_pos == "d1" or end_pos == "d3"):
                return True
            elif current_player == "BLUE" and board["E"][9]['piece'] is None and \
                    (end_pos == "d8" or end_pos == "d10" or end_pos == "f8" or end_pos == "f10"):
                return True
        else:
            return False

    def validate_horizontal_move(self, start_pos, end_pos, board):
        """Determines if the cannon is making a valid horizontal move, if the move is valid the function
        returns True. """
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        start_col_helper = start_pos[0].upper()
        start_column = alpha_list.index(start_col_helper)
        start_row = int(start_pos[1:])
        end_col_helper = end_pos[0].upper()
        end_column = alpha_list.index(end_col_helper)
        end_row = int(end_pos[1:])
        end_counter = end_column
        if start_column < end_column:
            start_counter = start_column + 1
            piece_counter = 0
            while start_counter < end_counter:
                column = alpha_list[start_counter]
                row = start_row
                if board[column][row]['piece'] is not None:
                    piece_counter += 1
                    start_counter += 1
                else:
                    start_counter += 1
        if start_column > end_column:
            start_counter = start_column - 1
            piece_counter = 0
            while start_counter > end_counter:
                column = alpha_list[start_counter]
                row = start_row
                if board[column][row]['piece'] is not None:
                    piece_counter += 1
                    start_counter -= 1
                else:
                    start_counter -= 1

        if piece_counter == 0:
            return True
        else:
            return False
        return False

    def validate_vertical_move(self, start_pos, end_pos, board):
        """Determines if the cannon is making a valid horizontal move, if valid the function returns True."""

        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        start_col_helper = start_pos[0].upper()
        start_column = alpha_list.index(start_col_helper)
        start_row = int(start_pos[1:])
        end_col_helper = end_pos[0].upper()
        end_column = alpha_list.index(end_col_helper)
        end_row = int(end_pos[1:])
        end_counter = end_row
        if start_row < end_row:
            start_counter = start_row + 1
            piece_counter = 0
            while start_counter < end_counter:
                column = start_col_helper
                row = start_counter
                if board[column][row]['piece'] is not None:
                    piece_counter += 1
                    start_counter += 1
                else:
                    start_counter += 1
        if start_row > end_row:
            start_counter = start_row - 1
            piece_counter = 0
            while start_counter > end_counter:
                column = start_col_helper
                row = start_counter
                if board[column][row]['piece'] is not None:
                    piece_counter += 1
                    start_counter -= 1
                else:
                    start_counter -= 1

        if piece_counter == 0:
            return True
        else:
            return False
        return False


class Elephant(Piece):
    """This class contains the functionality required for the Elephant piece in the Janggi game."""

    def __init__(self, player):
        """Initializes the elephant class as a subclass of the pieces class."""
        super().__init__(player)

    def valid_move(self, start_pos, end_pos, space_type, board):
        """Determines if the move being attempted is legal based on all logic related to moving to an elephant piece.
        Returns: Boolean. True if the move is valid, false if not."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        start_col_helper = start_pos[0].upper()
        start_column = alpha_list.index(start_col_helper)
        start_row = int(start_pos[1:])
        end_col_helper = end_pos[0].upper()
        end_column = alpha_list.index(end_col_helper)
        end_row = int(end_pos[1:])

        # test validity.
        if end_column > start_column:
            if self.validate_right_move(start_row, end_row, start_column, end_column, board):
                return True
        elif end_column < start_column:
            if self.validate_left_move(start_row, end_row, start_column, end_column, board):
                return True
        else:
            return False

    def validate_right_move(self, start_row, end_row, start_column, end_column, board):
        """Checks all possible moves for of the elephant class from the left side of the board to the right."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        # test right 2, up 3
        if end_row == start_row + 3 and end_column == start_column + 2:
            if board[alpha_list[start_column]][start_row + 1]['piece'] is None:
                if board[alpha_list[start_column + 1]][start_row + 2]['piece'] is None:
                    return True
        # test right 3, up 2
        elif end_row == start_row + 2 and end_column == start_column + 3:
            if board[alpha_list[start_column + 1]][start_row]['piece'] is None:
                if board[alpha_list[start_column + 2]][start_row + 1]['piece'] is None:
                    return True
        # test right 2, down 3
        elif end_row == start_row - 3 and end_column == start_column + 2:
            if board[alpha_list[start_column]][start_row - 1]['piece'] is None:
                if board[alpha_list[start_column + 1]][start_row - 2]['piece'] is None:
                    return True
        # test right 3, down 2
        elif end_row == start_row - 2 and end_column == start_column + 3:
            if board[alpha_list[start_column + 1]][start_row]['piece'] is None:
                if board[alpha_list[start_column + 2]][start_row - 1]['piece'] is None:
                    return True
                else:
                    return False

    def validate_left_move(self, start_row, end_row, start_column, end_column, board):
        """Checks all possible moves for of the elephant class from the right side of the board to the left."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        # test left 2, up 3
        if end_row == start_row + 3 and end_column == start_column - 2:
            if board[alpha_list[start_column]][start_row + 1]['piece'] is None:
                if board[alpha_list[start_column - 1]][start_row + 2]['piece'] is None:
                    return True
        # test left 3, up 2
        elif end_row == start_row + 2 and end_column == start_column - 3:
            if board[alpha_list[start_column - 1]][start_row]['piece'] is None:
                if board[alpha_list[start_column - 2]][start_row + 1]['piece'] is None:
                    return True
        # test left 2, down 3
        elif end_row == start_row - 3 and end_column == start_column - 2:
            if board[alpha_list[start_column]][start_row - 1]['piece'] is None:
                if board[alpha_list[start_column - 1]][start_row - 2]['piece'] is None:
                    return True
        # test left 3, down 2
        elif end_row == start_row - 2 and end_column == start_column - 3:
            if board[alpha_list[start_column - 1]][start_row]['piece'] is None:
                if board[alpha_list[start_column - 2]][start_row - 1]['piece'] is None:
                    return True
        else:
            return False

class Horse(Piece):
    """This class contains the functionality required for the horse piece in the Janggi game."""

    def __init__(self, player):
        """Initializes the horse class as a subclass of the pieces class."""
        super().__init__(player)

    def valid_move(self, start_pos, end_pos, space_type, board):
        """Determines if the move being attempted is legal based on all logic related to moving to a horse piece.
        Returns: Boolean. True if the move is valid, false if not."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        start_col_helper = start_pos[0].upper()
        start_column = alpha_list.index(start_col_helper)
        start_row = int(start_pos[1:])
        end_col_helper = end_pos[0].upper()
        end_column = alpha_list.index(end_col_helper)
        end_row = int(end_pos[1:])

        # test validity.
        if end_column > start_column:
            if self.validate_right_move(start_row, end_row, start_column, end_column, board):
                return True
        elif end_column < start_column:
            if self.validate_left_move(start_row, end_row, start_column, end_column, board):
                return True
        else:
            return False

    def validate_right_move(self, start_row, end_row, start_column, end_column, board):
        """Checks all possible moves for of the elephant class from the left side of the board to the right."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        # test up 2, right 1
        if end_row == start_row + 2 and end_column == start_column + 1:
            if board[alpha_list[start_column]][start_row + 1]['piece'] is None:
                return True
        # test right 2, up 1
        elif end_row == start_row + 1 and end_column == start_column + 2:
            if board[alpha_list[start_column + 1]][start_row]['piece'] is None:
                return True
        # test right 2, down 1
        elif end_row == start_row - 1 and end_column == start_column + 2:
            if board[alpha_list[start_column + 1]][start_row]['piece'] is None:
                return True
        # test right 1, up 2
        elif end_row == start_row - 2 and end_column == start_column + 1:
            if board[alpha_list[start_column]][start_row - 1]['piece'] is None:
                return True
            else:
                return False
        else:
            return False

    def validate_left_move(self, start_row, end_row, start_column, end_column, board):
        """Checks all possible moves for of the elephant class from the right side of the board to the left."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        # test up 2, left 1
        if end_row == start_row + 2 and end_column == start_column - 1:
            if board[alpha_list[start_column]][start_row + 1]['piece'] is None:
                return True
        # test left 2, up 1
        elif end_row == start_row + 1 and end_column == start_column - 2:
            if board[alpha_list[start_column - 1]][start_row]['piece'] is None:
                return True
        # test left 2, down 1
        elif end_row == start_row - 1 and end_column == start_column - 2:
            if board[alpha_list[start_column - 1]][start_row]['piece'] is None:
                return True
        # test left 1, down 2
        elif end_row == start_row - 2 and end_column == start_column - 1:
            if board[alpha_list[start_column]][start_row - 1]['piece'] is None:
                return True
            else:
                return False

class Guard(Piece):
    """This contains the functionality required for the Guard class including the initializer and movement checks."""

    def __init__(self, player):
        """Initializes the Guard class as a subclass of the pieces class."""
        super().__init__(player)

    def valid_move(self, start_pos, end_pos, space_type, board):
        """Determines if the move being attempted is legal based on all logic related to moving to a Guard piece.
            Returns: Boolean. True if the move is valid, false if not."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        start_col_helper = start_pos[0].upper()
        start_column = alpha_list.index(start_col_helper)
        start_row = int(start_pos[1:])
        end_col_helper = end_pos[0].upper()
        end_column = alpha_list.index(end_col_helper)
        end_row = int(end_pos[1:])

        if board[end_col_helper][end_row]['type'] == "PALACE":
            if (end_row == start_row + 1 or end_row == start_row - 1 or end_row == start_row) and (end_column == start_column
            + 1 or end_column == start_column - 1 or end_column == start_column):
                return True
        else:
            return False


class General(Piece):
    """This contains the functionality required for the General class including the initializer and movement checks"""

    def __init__(self, player):
        """Initializes the General class as a subclass of the pieces class."""
        super().__init__(player)
        self._check_status = False

    def valid_move(self, start_pos, end_pos, space_type, board):
        """Determines if the move being attempted is legal based on all logic related to moving to a General piece.
        Returns: Boolean. True if the move is valid, false if not."""
        alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        start_col_helper = start_pos[0].upper()
        start_column = alpha_list.index(start_col_helper)
        start_row = int(start_pos[1:])
        end_col_helper = end_pos[0].upper()
        end_column = alpha_list.index(end_col_helper)
        end_row = int(end_pos[1:])
        # pass turn
        if start_row == end_row and start_column == end_column:
            return True

        if board[end_col_helper][end_row]['type'] == "PALACE":
            if board[end_col_helper][end_row]['Status'] is None:
                if (end_row == start_row + 1 or end_row == start_row - 1 or end_row == start_row) and \
                        (end_column == start_column + 1 or end_column == start_column - 1 or end_column == start_column):
                    return True
        else:
            return False

    def set_general_check(self):
        """Sets the check status of the general general that the function is called on."""
        if self._check_status == False:
            self._check_status = True
            return True
        if self._check_status:
            return

    def remove_general_check(self):
        """Sets the check status of the general to False (meaning not in check)."""
        self._check_status = False

