# import turtle package
from turtle import Turtle
from piece_manager import Pawn, Knight, Bishop, Rook, Queen, King


ROWS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
COLS = [x for x in range(1, 9)]


class Gameboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-413, -406)
        self.speed(10)
        self.pensize(4)
        self.pu()
        self.pencolor('white')
        self.draw_board()
        self.positions = {}
        self.notations()
        self.pieces_list = []
        self.graveyard_white = []
        self.graveyard_black = []
        self.winner = ''
        self.highlighted = False
        self.setup_board()


    def draw_box(self):
        for i in range(0, 4):
            self.pd()
            self.forward(102.5)
            self.left(90)

        self.forward(102.5)

    def draw_board(self):
        # rows
        for i in range(8):
            self.pu()
            if i == 0:
                pass
            else:
                self.sety(self.ycor() + 102.5)
                self.setx(-413)
            # columns
            for j in range(8):
                if (i + j) % 2 == 0:
                    col = '#024C3E' #'#094DC6'#

                else:
                    col = '#FFF5E3' #'#FFF8F0'#

                # fill with given color
                self.fillcolor(col)

                # start filling with colour
                self.begin_fill()

                # call method
                self.draw_box()
                # stop filling
                self.end_fill()

    def notations(self):
        start_y = -406 + 51.5
        for i in range(8):
            start_x = -413 + 51.5
            col = str(COLS[i])
            for j in range(8):
                row = ROWS[j]
                pos = Turtle('square')
                pos.fillcolor('#D9E9F4')
                pos.shapesize(stretch_wid=0.2, stretch_len=4.65)
                pos.hideturtle()
                pos.pu()
                pos.goto(x=start_x, y=start_y)
                self.positions[row + col] = pos
                start_x += 102.5
            start_y += 102.5

    def setup_board(self):
        # pawns
        for rows in ROWS:
            pw = Pawn(color='W')
            pw.player = 'white'
            pw.pu()
            col = '2'
            x_start = self.positions[rows + col].position()[0]
            y_start = self.positions[rows + col].position()[1]
            pw.goto(x=x_start, y=y_start)
            pw.board_position = rows + col
            self.pieces_list.append(pw)

        for rows in ROWS:
            pb = Pawn(color='B')
            pb.player = 'black'
            pb.pu()
            col = '7'
            x_start = self.positions[rows + col].position()[0]
            y_start = self.positions[rows + col].position()[1]
            pb.goto(x=x_start, y=y_start)
            pb.board_position = rows + col
            self.pieces_list.append(pb)

        # knights
        for i in ['b1', 'g1']:
            knw = Knight(color = 'W')
            knw.player = 'white'
            knw.pu()
            x_start = self.positions[i].position()[0]
            y_start = self.positions[i].position()[1]
            knw.goto(x=x_start, y=y_start)
            knw.board_position = i
            self.pieces_list.append(knw)

        for i in ['b8', 'g8']:
            knb = Knight(color = 'B')
            knb.player = 'black'
            knb.pu()
            x_start = self.positions[i].position()[0]
            y_start = self.positions[i].position()[1]
            knb.goto(x=x_start, y=y_start)
            knb.board_position = i
            self.pieces_list.append(knb)

        for i in ['a1', 'h1']:
            rw = Rook(color = 'W')
            rw.player = 'white'
            rw.pu()
            x_start = self.positions[i].position()[0]
            y_start = self.positions[i].position()[1]
            rw.goto(x=x_start, y=y_start)
            rw.board_position = i
            self.pieces_list.append(rw)

        for i in ['a8', 'h8']:
            rb = Rook(color = 'B')
            rb.player = 'black'
            rb.pu()
            x_start = self.positions[i].position()[0]
            y_start = self.positions[i].position()[1]
            rb.goto(x=x_start, y=y_start)
            rb.board_position = i
            self.pieces_list.append(rb)

        for i in ['c1', 'f1']:
            bw = Bishop(color = 'W')
            bw.player = 'white'
            bw.pu()
            x_start = self.positions[i].position()[0]
            y_start = self.positions[i].position()[1]
            bw.goto(x=x_start, y=y_start)
            bw.board_position = i
            self.pieces_list.append(bw)

        for i in ['c8', 'f8']:
            bb = Bishop(color = 'B')
            bb.player = 'black'
            bb.pu()
            x_start = self.positions[i].position()[0]
            y_start = self.positions[i].position()[1]
            bb.goto(x=x_start, y=y_start)
            bb.board_position = i
            self.pieces_list.append(bb)

        for i in ['d1']:
            qw = Queen(color = 'W')
            qw.player = 'white'
            qw.pu()
            x_start = self.positions[i].position()[0]
            y_start = self.positions[i].position()[1]
            qw.goto(x=x_start, y=y_start)
            qw.board_position = i
            self.pieces_list.append(qw)

        for i in ['d8']:
            qb = Queen(color = 'B')
            qb.player = 'black'
            qb.pu()
            x_start = self.positions[i].position()[0]
            y_start = self.positions[i].position()[1]
            qb.goto(x=x_start, y=y_start)
            qb.board_position = i
            self.pieces_list.append(qb)

        for i in ['e1']:
            kw = King(color = 'W')
            kw.player = 'white'
            kw.pu()
            x_start = self.positions[i].position()[0]
            y_start = self.positions[i].position()[1]
            kw.goto(x=x_start, y=y_start)
            kw.board_position = i
            self.pieces_list.append(kw)

        for i in ['e8']:
            kb = King(color='B')
            kb.player = 'black'
            kb.pu()
            x_start = self.positions[i].position()[0]
            y_start = self.positions[i].position()[1]
            kb.goto(x=x_start, y=y_start)
            kb.board_position = i
            self.pieces_list.append(kb)

        for pieces in self.pieces_list:
            pieces.board_pieces = self.pieces_list

    def to_graveyard(self, piece):
        if piece.player == 'white':
            if piece not in self.graveyard_white:
                self.graveyard_white.append(piece)
                if len(self.graveyard_white) <= 8:
                    x_cor = 500
                    y_cor = 400 - (80 *len(self.graveyard_white))
                else:
                    x_cor = 550
                    y_cor = 400 - (80 *(len(self.graveyard_white) - 8))
                piece.goto(x_cor, y_cor)

        else:
            if piece not in self.graveyard_black:
                self.graveyard_black.append(piece)
                if len(self.graveyard_black) <= 8:
                    x_cor = -500
                    y_cor = 400 - (80 *len(self.graveyard_black))
                else:
                    x_cor = -550
                    y_cor = 400 - (80 *(len(self.graveyard_black) - 8))
                piece.goto(x_cor, y_cor)



    def game_over(self):
        self.pu()
        self.goto(0, 30)
        self.color('black')
        self.write('GAME OVER', align='center', font=('arial', 25, 'bold'))
        self.goto(0, 60)
        self.write(f'{self.winner.upper()} WINS!', align='center', font=('arial', 25, 'bold'))




