
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
        return  {'score': -10}
    elif (check_winner(new_board, aiPlayer)):
        return {'score': 10}
    elif (len(possible_moves) == 0):
        return  {'score': 0}
    else:
        moves = []

        for i in range(len(possible_moves)):
            move_index = int(possible_moves[i])
            move = {}
            move['index'] = new_board[move_index]
            new_board[move_index] = player

            if (player == aiPlayer):
                minmax_result = minmax(new_board, human)
                move['score'] = minmax_result['score']
            else:
                minmax_result = minmax(new_board, aiPlayer)
                move['score'] = minmax_result['score']


            new_board[move_index] = move['index']

            moves.append(move)

        best_move = 'x'
        if (player == aiPlayer):
            best_score = -10000

            for i in range(len(moves)):
                if (int(moves[i]['score']) > best_score):
                    best_score = moves[i]['score']
                    best_move = i

        else:
            best_score = 10000
            for i in range(len(moves)):
                if (int(moves[i]['score']) < best_score):
                    best_score = moves[i]['score']
                    best_move = i

        return moves[best_move]




aiPlayer = 'X'
human = 'O'
board = ['0','1','2','3','4','5','6','7','8']

print(board[0] + " | " + board[1] + " | " + board[2])
print('----------')
print(board[3] + " | " + board[4] + " | " + board[5])
print('----------')
print(board[6] + " | " + board[7] + " | " + board[8])
print("\n")

while(not check_winner(board, human) and not check_winner(board, aiPlayer)):



    p_move = input("Player move")

    board[int(p_move)] = human

    if (check_winner(board, human)):
        print("Player 1 wins!")
        break

    else:

        print(board[0] + " | " + board[1] + " | " + board[2])
        print('----------')
        print(board[3] + " | " + board[4] + " | " + board[5])
        print ('----------')
        print(board[6] + " | " + board[7] + " | " + board[8])
        print("\n")



    if(check_winner(board, aiPlayer)):
        print("computer wins")
        break
    # elif (len(available_moves(board)) == 0):
    #     print("Cats game!")
    else:
        comp_move = minmax(board, aiPlayer)
        board[int(comp_move['index'])] = aiPlayer
        print(board[0] + " | " + board[1] + " | " + board[2])
        print('----------')
        print(board[3] + " | " + board[4] + " | " + board[5])
        print ('----------')
        print(board[6] + " | " + board[7] + " | " + board[8])
        print("\n")







