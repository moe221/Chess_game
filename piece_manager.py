# import turtle package
from turtle import Turtle
from gameboard import *

BOARD_POSITIONS = {'a1': (-361.50, -354.50), 'b1': (-259.00, -354.50), 'c1': (-156.50, -354.50),
                   'd1': (-54.00, -354.50),
                   'e1': (48.50, -354.50), 'f1': (151.00, -354.50), 'g1': (253.50, -354.50), 'h1': (356.00, -354.50),
                   'a2': (-361.50, -252.00), 'b2': (-259.00, -252.00), 'c2': (-156.50, -252.00),
                   'd2': (-54.00, -252.00),
                   'e2': (48.50, -252.00), 'f2': (151.00, -252.00), 'g2': (253.50, -252.00), 'h2': (356.00, -252.00),
                   'a3': (-361.50, -149.50), 'b3': (-259.00, -149.50), 'c3': (-156.50, -149.50),
                   'd3': (-54.00, -149.50),
                   'e3': (48.50, -149.50), 'f3': (151.00, -149.50), 'g3': (253.50, -149.50), 'h3': (356.00, -149.50),
                   'a4': (-361.50, -47.00), 'b4': (-259.00, -47.00), 'c4': (-156.50, -47.00), 'd4': (-54.00, -47.00),
                   'e4': (48.50, -47.00), 'f4': (151.00, -47.00), 'g4': (253.50, -47.00), 'h4': (356.00, -47.00),
                   'a5': (-361.50, 55.50), 'b5': (-259.00, 55.50), 'c5': (-156.50, 55.50), 'd5': (-54.00, 55.50),
                   'e5': (48.50, 55.50), 'f5': (151.00, 55.50), 'g5': (253.50, 55.50), 'h5': (356.00, 55.50),
                   'a6': (-361.50, 158.00), 'b6': (-259.00, 158.00), 'c6': (-156.50, 158.00), 'd6': (-54.00, 158.00),
                   'e6': (48.50, 158.00), 'f6': (151.00, 158.00), 'g6': (253.50, 158.00), 'h6': (356.00, 158.00),
                   'a7': (-361.50, 260.50), 'b7': (-259.00, 260.50), 'c7': (-156.50, 260.50), 'd7': (-54.00, 260.50),
                   'e7': (48.50, 260.50), 'f7': (151.00, 260.50), 'g7': (253.50, 260.50), 'h7': (356.00, 260.50),
                   'a8': (-361.50, 363.00), 'b8': (-259.00, 363.00), 'c8': (-156.50, 363.00), 'd8': (-54.00, 363.00),
                   'e8': (48.50, 363.00), 'f8': (151.00, 363.00), 'g8': (253.50, 363.00), 'h8': (356.00, 363.00)}

UP = 102.5
DOWN = -102.5
RIGHT = 102.5
LEFT = -102.5


def click_board_position(x, y):
    for key in BOARD_POSITIONS:
        x_board = BOARD_POSITIONS[key][0]
        y_board = BOARD_POSITIONS[key][1]
        if x in range(int(x_board - 51.5),
                      int(x_board + 51.5)) and y in range(int(y_board - 51.5),
                                                          int(y_board + 51.5)):
            return x_board, y_board, key


class Chesspiece(Turtle):
    def __init__(self):
        super().__init__()
        self.moves = 0
        self.moved = False
        self.selected = False
        self.board_position = ''
        self.player = ''
        self.board_pieces = []
        self.taken_pieces = []
        self.taken = False
        self.name = ''

    def to_graveyard(self):
        if self.player == 'white':
            self.goto(-500, 350)
        else:
            self.goto(500, 350)

    def check_space(self, key):
        list_of_occupied_positions = [pos.board_position for pos in self.board_pieces]
        if key in list_of_occupied_positions:
            for pieces in self.board_pieces:
                if pieces.board_position == key and (pieces.player != self.player):
                    pieces.board_position = ''
                    pieces.taken = True

            self.selected = False

    def friendly_piece(self, key):
        list_of_occupied_positions = [pos.board_position for pos in self.board_pieces]
        if key in list_of_occupied_positions:
            for pieces in self.board_pieces:
                if pieces.board_position == key and (pieces.player == self.player):
                    self.selected = False
                    return True

    def clear_way_vertical(self, x_board, y_board, key, current_x, current_y):
        if (y_board - current_y) > 0:
            step = UP
        else:
            step = DOWN
        i = current_y
        while i != (y_board - step):
            i += step
            for key in BOARD_POSITIONS:
                if BOARD_POSITIONS[key] == (current_x, i):
                    list_of_occupied_positions = [pos.board_position for pos in self.board_pieces]
                    if key in list_of_occupied_positions:
                        print('way is blocked_v')
                        return False
        return True

    def clear_way_horizontal(self, x_board, y_board, key, current_x, current_y):
        if (x_board - current_x) > 0:
            step = RIGHT
        else:
            step = LEFT
        i = current_x
        while i != (x_board - step):
            i += step
            for key in BOARD_POSITIONS:
                if BOARD_POSITIONS[key] == (i, current_y):
                    list_of_occupied_positions = [pos.board_position for pos in self.board_pieces]
                    if key in list_of_occupied_positions:
                        print('way is blocked_h')
                        return False
        print('all clear_h')
        return True

    def clear_way_diagonal(self, x_board, y_board, key, current_x, current_y):
        if (x_board - current_x) > 0:
            step_side = RIGHT
        else:
            step_side = LEFT

        if (y_board - current_y) > 0:
            step_forward = UP
        else:
            step_forward = DOWN
        i = current_x
        j = current_y
        while i != (x_board - step_side) or j != (y_board - step_forward):
            i += step_side
            j += step_forward
            for key in BOARD_POSITIONS:
                if BOARD_POSITIONS[key] == (i, j):
                    list_of_occupied_positions = [pos.board_position for pos in self.board_pieces]
                    if key in list_of_occupied_positions:
                        print('way is blocked_d')
                        return False
        print('all clear_d')
        return True


class Pawn(Chesspiece):
    def __init__(self, color):
        super().__init__()
        self.icon = f'Images/P{color}.gif'
        self.shape(self.icon)

    def move(self, x, y):
        self.moved = False
        move_allowed = False
        x_board, y_board, key = click_board_position(x, y)
        current_x = self.position()[0]
        current_y = self.position()[1]
        list_of_occupied_positions = [pos.board_position for pos in self.board_pieces]

        if self.player == 'white':
            if self.moves == 0:
                distance = [UP, 2 * UP]
            else:
                distance = [UP]
        else:
            if self.moves == 0:
                distance = [DOWN, 2 * DOWN]
            else:
                distance = [DOWN]

        distance_x = [LEFT, RIGHT]

        if (x_board == current_x) and ((y_board - current_y) in distance):
            if key in list_of_occupied_positions:
                move_allowed = False
            else:
                if self.clear_way_vertical(x_board, y_board, key, current_x, current_y):
                    move_allowed = True

        elif (x_board in [current_x + distance_x[0], current_x + distance_x[1]]) and (
                y_board == (current_y + distance[0])):
            if key in list_of_occupied_positions and not self.friendly_piece(key):
                move_allowed = True
                self.check_space(key)

        if move_allowed:
            self.goto(x=x_board, y=y_board)
            self.board_position = key
            self.moves += 1
            self.moved = True
            self.selected = False
        else:
            self.selected = False


class Knight(Chesspiece):
    def __init__(self, color):
        super().__init__()
        self.icon = f'Images/Kn{color}.gif'
        self.shape(self.icon)

    def move(self, x, y):

        move_allowed = False
        x_board, y_board, key = click_board_position(x, y)
        current_x = self.position()[0]
        current_y = self.position()[1]

        # stop pieces of same color from going to same position
        if self.friendly_piece(key):
            return None

        valid_move1 = (current_x + LEFT, current_y + 2 * UP)
        valid_move2 = (current_x + RIGHT, current_y + 2 * UP)
        valid_move3 = (current_x + LEFT, current_y + 2 * DOWN)
        valid_move4 = (current_x + RIGHT, current_y + 2 * DOWN)
        valid_move5 = (current_x + 2 * LEFT, current_y + DOWN)
        valid_move6 = (current_x + 2 * RIGHT, current_y + DOWN)
        valid_move7 = (current_x + 2 * LEFT, current_y + UP)
        valid_move8 = (current_x + 2 * RIGHT, current_y + UP)

        valid_moves = [valid_move1, valid_move2, valid_move3, valid_move4, valid_move5,
                       valid_move6, valid_move7, valid_move8, ]

        for moves in valid_moves:
            if (x_board, y_board) == moves:
                move_allowed = True

            if move_allowed:
                self.goto(x=x_board, y=y_board)
                self.board_position = key
                self.moves += 1
                self.selected = False
                self.moved = True
                self.check_space(key)

            else:
                self.selected = False


class Rook(Chesspiece):
    def __init__(self, color):
        super().__init__()
        self.icon = f'Images/R{color}.gif'
        self.shape(self.icon)

    def move(self, x, y):
        move_allowed = False
        x_board, y_board, key = click_board_position(x, y)
        current_x = self.position()[0]
        current_y = self.position()[1]

        if self.friendly_piece(key):
            return None

        if (x_board == current_x) and (y_board != current_y):
            if self.clear_way_vertical(x_board, y_board, key, current_x, current_y):
                move_allowed = True

        elif (x_board != current_x) and (y_board == current_y):
            if self.clear_way_horizontal(x_board, y_board, key, current_x, current_y):
                move_allowed = True

        if move_allowed:
            self.goto(x=x_board, y=y_board)
            self.board_position = key
            self.moves += 1
            self.selected = False
            self.moved = True
            self.check_space(key)

        else:
            self.selected = False


class Bishop(Chesspiece):
    def __init__(self, color):
        super().__init__()
        self.icon = f'Images/B{color}.gif'
        self.shape(self.icon)

    def move(self, x, y):
        move_allowed = False
        x_board, y_board, key = click_board_position(x, y)
        current_x = self.position()[0]
        current_y = self.position()[1]

        if self.friendly_piece(key):
            return None

        if abs(x_board - current_x) == abs(y_board - current_y):
            if self.clear_way_diagonal(x_board, y_board, key, current_x, current_y):
                move_allowed = True

        if move_allowed:
            self.goto(x=x_board, y=y_board)
            self.board_position = key
            self.moves += 1
            self.selected = False
            self.moved = True
            self.check_space(key)

        else:
            self.selected = False


class Queen(Chesspiece):
    def __init__(self, color):
        super().__init__()
        self.icon = f'Images/Q{color}.gif'
        self.shape(self.icon)

    def move(self, x, y):
        move_allowed = False
        x_board, y_board, key = click_board_position(x, y)
        current_x = self.position()[0]
        current_y = self.position()[1]

        if self.friendly_piece(key):
            return None

        if (x_board == current_x) and (y_board != current_y):
            if self.clear_way_vertical(x_board, y_board, key, current_x, current_y):
                move_allowed = True

        elif (x_board != current_x) and (y_board == current_y):
            if self.clear_way_horizontal(x_board, y_board, key, current_x, current_y):
                move_allowed = True

        elif abs(x_board - current_x) == abs(y_board - current_y):
            if self.clear_way_diagonal(x_board, y_board, key, current_x, current_y):
                move_allowed = True

        if move_allowed:
            self.goto(x=x_board, y=y_board)
            self.board_position = key
            self.moves += 1
            self.selected = False
            self.moved = True
            self.check_space(key)

        else:
            self.selected = False


class King(Chesspiece):
    def __init__(self, color):
        super().__init__()
        self.icon = f'Images/K{color}.gif'
        self.shape(self.icon)
        self.name = 'king'

    def move(self, x, y):
        move_allowed = False
        x_board, y_board, key = click_board_position(x, y)

        if self.friendly_piece(key):
            return None

        if (abs(x_board - self.position()[0]) < 200) and (abs(y_board - self.position()[1]) < 200):
            move_allowed = True

        if move_allowed:
            self.goto(x=x_board, y=y_board)
            self.board_position = key
            self.moves += 1
            self.selected = False
            self.moved = True
            self.check_space(key)

        else:
            self.selected = False
