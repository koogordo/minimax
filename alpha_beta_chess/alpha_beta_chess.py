"""For the game board the white pieces are the capatals"""

import moves
from piece_tables import pawn_board,bishop_board,king_table,king_table_end, knight_table
import time

global k_p_c
global k_p_l
k_p_c = 60
k_p_l = 4
global global_depth
global game_board
global_depth = 4
game_board = [
    ['r', 'k', 'b', 'q', 'a', 'b', 'k', 'r'],
    ['p', 'p', 'p', 'p', ' ', 'p', 'p', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', 'p', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'P', 'K', ' ', ' ', 'K'],
    ['P', 'P', 'P', ' ', 'P', 'P', 'P', 'P'],
    ['R', ' ', 'B', 'Q', 'A', 'B', ' ', 'R'],
]

#global depth dicates depth of alpha-beta algorithm



global count
count = 0
def alpha_beta(depth=global_depth, beta=10000000, alpha=-10000000, move="", player=0):
    """Alpha beta pruning method that will return the bset chess move"""
    global k_p_c
    global k_p_l
    global count
    list = moves.possible_moves(game_board, k_p_c, k_p_l)
    if depth == 0 or len(list) == 0:
        return move + str(rating(len(list), depth) * (player * 2 - 1)) ## * (player*2-1))
    for i in range(0,len(list), 5):
        #need to make make move
        print(count)
        moves.make_move(list[i:i+5])
        flip_board() #make a move and then rotate board around and make move for opponent
        return_string = alpha_beta(depth - 1, beta, alpha, list[i:i+5], player)
        value = int(return_string[5: len(return_string)])
        flip_board()
        moves.undo_move(list[i:i+5])

        if player == 0:
            if value <= beta:
                beta = value
                if depth == global_depth:
                    move = return_string[0:5]
        else:
            if value > alpha:
                alpha = value
                if depth == global_depth:
                    move = return_string[0:5]
        if alpha >= beta:
            if player == 0:
                return move + str(beta)
            else:
                return move + str(alpha)

    if player == 0:
        return move + str(beta)
    else:
        return move + str(alpha)





def flip_board():
    """Flip board so that we have the perspective have the player
    whose turn it is"""
    global k_p_l
    global k_p_c
    temp = ' '
    for i in range(32):
        r, c = i // 8, i % 8
        if game_board[r][c].isupper():
            temp = game_board[r][c].lower()
        else:
            temp = game_board[r][c].upper()

        if game_board[7-r][7-c].isupper():
            game_board[r][c] = game_board[7-r][7-c].lower()
        else:
            game_board[r][c] = game_board[7 - r][7 - c].upper()
        game_board[7-r][7-c] = temp

    king_temp = k_p_c
    k_p_c = 63 - k_p_l
    k_p_l = 63 - king_temp



def rating(num_of_moves, depth):
    counter = 0
    counter = counter + rate_attack()
    counter = counter + rate_material()
    counter = counter + rate_moveability(num_of_moves, depth)
    #counter = counter + rate_positional(material)
    flip_board()
    counter = counter + rate_attack()
    counter = counter + rate_material()
    counter = counter + rate_moveability(num_of_moves, depth)
    #counter = counter + rate_positional(material)
    flip_board()
    return 0 - counter + depth * 50

def rate_attack():
    counter = 0
    temp_king_pos = moves.king_pos_c
    for i in range(64):
        board_piece = game_board[i // 8][i % 8]
        if board_piece == 'P':
            moves.king_pos_c = i
            if not moves.king_safe():
                counter = counter - 64
        if board_piece == 'R':
            moves.king_pos_c = i
            if not moves.king_safe():
                counter = counter - 500
        if board_piece == 'K':
            moves.king_pos_c = i
            if not moves.king_safe():
                counter = counter - 300
        if board_piece == 'B':
            moves.king_pos_c = i
            if not moves.king_safe():
                counter = counter - 300
        if board_piece == 'Q':
            moves.king_pos_c = i
            if not moves.king_safe():
                counter = counter - 900
    moves.king_pos_c = temp_king_pos
    return counter

def rate_material():
     counter = 0
     bishop_counter = 0
     for i in range(64):
        board_piece = game_board[i // 8][i % 8]
        if board_piece=='P': counter = (counter + 100)
        if board_piece=='R': counter = counter + 500
        if board_piece=='K': counter = (counter + 300)
        if board_piece=='B': bishop_counter = bishop_counter + 1
        if board_piece=='Q': counter = counter + 900
     if bishop_counter >= 2:
         counter = (counter + 300 * bishop_counter)
         if bishop_counter == 1:
             counter = (counter + 250)
     return counter

def rate_moveability(num_of_moves, depth):
    counter = 0
    counter = counter + num_of_moves
    if num_of_moves == 0:
        if not moves.king_safe():
            counter = counter + -200000 * depth
        else:
            counter = counter + -150000 * depth
    return counter



opt_move = alpha_beta(player=1)
print(opt_move)

