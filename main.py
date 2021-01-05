# TODO SETUP GAME BOARD

import turtle as t
from tkinter import Button
from gameboard import Gameboard
from player import Player

# create screen object
screen = t.Screen()
screen.title('Chess Game')
screen.setup(width=1300, height=835)  # og 835, 835
# add all icons to screen
for image in ['BB', 'KB', 'KnB', 'KnW', 'KW', 'PB', 'PW',
              'QB', 'RB', 'RW', 'BW', 'QW']:
    screen.addshape(f'Images/{image}.gif')

# turn animation off
screen.tracer(0)
screen.listen()

# setup Chess board
gameboard = Gameboard()
screen.update()

# setup players
player1 = Player(color='white')
player1.player_turn = True
player2 = Player(color='black')

for piece in gameboard.pieces_list:
    if piece.player == 'white':
        player1.player_pieces.append(piece)
    else:
        player2.player_pieces.append(piece)

# to highlight selected piece
for positions in gameboard.positions:
    turtle = gameboard.positions[positions]
    turtle.sety(turtle.ycor() - 45)


def check_winner():
    for piece in gameboard.pieces_list:
        if piece.name == 'king' and piece.taken:
            if piece.player == 'white':
                gameboard.winner = 'Black'
                return True
            else:
                gameboard.winner = 'White'
                return True
    return False


def turn_over(player1, player2):
    if player1.player_turn == True:
        player1.player_turn = False
        player2.player_turn = True
        print(f"{player2.color}'s move")
    else:
        player2.player_turn = False
        player1.player_turn = True
        print(f"{player1.color}'s move")


def get_mouse_click_coor(x, y):
    if player1.player_turn:
        available_pieces = player1.player_pieces
    else:
        available_pieces = player2.player_pieces

    for piece in available_pieces:
        if x in range(int(piece.xcor() - 51.5),
                      int(piece.xcor() + 51.5)) and y in \
                range(int(piece.ycor() - 51.5),
                      int(piece.ycor() + 51.5)):
            print(piece.board_position, piece.player)
            piece.selected = True


while True:

    screen.update()
    for piece in gameboard.pieces_list:
        if piece.selected == False:
            for positions in gameboard.positions:
                gameboard.positions[positions].hideturtle()
            # break
        if piece.moved:
            piece.selected = False
            piece.moved = False
            turn_over(player1, player2)
        if piece.selected:
            gameboard.positions[piece.board_position].showturtle()
            piece.forward(0)
            screen.onclick(piece.move)
            #super secret allegra attack
            #piece.ondrag(piece.move)
            break
        if piece.taken:
            gameboard.to_graveyard(piece)

        else:
            screen.onscreenclick(get_mouse_click_coor)

    if check_winner():
        gameboard.game_over()
        break

screen.mainloop()
