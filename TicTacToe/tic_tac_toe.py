
def check_winner(current_board, player):
   if(
        (current_board[0] == player and current_board[1] == player and current_board[2] == player) or
        (current_board[3] == player and current_board[4] == player and current_board[5] == player) or
        (current_board[6] == player and current_board[7] == player and current_board[8] == player) or
        (current_board[0] == player and current_board[3] == player and current_board[6] == player) or
        (current_board[1] == player and current_board[4] == player and current_board[7] == player) or
        (current_board[2] == player and current_board[5] == player and current_board[8] == player) or
        (current_board[0] == player and current_board[4] == player and current_board[8] == player) or
        (current_board[2] == player and current_board[4] == player and current_board[6] == player)
   ):
       return True
   else:
       return False


def available_moves(board_state):
    return filter(lambda move: move != 'X' and move != 'O', board_state)



def minmax(new_board, player):

    possible_moves = available_moves(new_board)
    if (check_winner(new_board, human)):
        return  -10
    elif (check_winner(new_board, aiPlayer)):
        return 10
    elif (len(possible_moves) == 0):
        return  0
    else:
        moves = []

        for i in range(len(possible_moves)):
            move_index = int(possible_moves[i])
            move = {}
            move['index'] = new_board[move_index]
            new_board[move_index] = player

            if (player == aiPlayer):
                minmax_result = minmax(new_board, human)
                move['score'] = minmax_result
            else:
                minmax_result = minmax(new_board, aiPlayer)
                move['score'] = minmax_result

            new_board[move_index] = move['index']

            moves.append(move)

        best_move = 'x'
        if (player == aiPlayer):
            best_score = -10000

            for move in moves:
                if (int(move['score']) > best_score):
                    best_score = move['score']
                    best_move = move['index']

        else:
            best_score = 10000
            for move in moves:
                if (int(move['score']) < best_score):
                    best_score = move['score']
                    best_move = move['index']

        return best_move













