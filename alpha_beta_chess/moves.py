
global king_pos_c
global king_pos_l
global game_board
global moves
def possible_moves(incoming_board, k_p_c, k_p_l):
    """Returns all possible moves for any game state
        {x1, y1, x2, y2, captured piece}
    """
    global king_pos_c
    global king_pos_l
    global game_board
    global moves
    game_board = incoming_board
    king_pos_c = k_p_c
    king_pos_l = k_p_l
    # try:
    #     while game_board[king_pos_c // 8][king_pos_c % 8] != 'A':
    #         king_pos_c = king_pos_c + 1
    #
    #     while game_board[king_pos_l // 8][king_pos_l % 8] != 'a':
    #         king_pos_l = king_pos_l + 1
    # except:
    #     pass
    moves = ""
    for i in range(64):
        board_piece = game_board[i // 8][i % 8]
        board_case = {
                'P': possibleP,
                'R': possibleR,
                'K': possibleK,
                'B': possibleB,
                'Q': possibleQ,
                'A': possibleA,
                ' ': 'blank space'
                }
        if board_piece == ' ' or board_piece.islower():
            pass
        else:
            board_case[board_piece](i)
    return moves


#Possible moves for each piece methods
def possibleP(location):
    global moves
    move_range = [-1, 1]
    row = location // 8
    column = location % 8
    temp = 1
    for i in move_range:
        try:
            if game_board[row - 1][column + i].islower() and location >= 16:
                if row - 1 >= 0 and column + i >= 0:
                    old_piece = game_board[row - 1][column + i]
                    game_board[row][column] = ' '
                    game_board[row - 1][column + i] = 'P'
                    if king_safe():
                        #x1 y1 x2 y2 capture
                        # MOVES CHANGED TO STRING
                        moves = moves + str(column) + str(row) + str(row - 1) + str(column + i) + old_piece
                    game_board[row][column] = 'P'
                    game_board[row - 1][column + i] = old_piece
                else:
                    pass
        except:
            pass
        try:
            if game_board[row - 1][column + i].islower() and location < 16:
                temp_pieces = ['Q', 'R', 'B', 'K']
                if row - 1 >= 0 and column + i >= 0:
                    for piece in temp_pieces:
                        old_piece = game_board[row - 1][column + i]
                        game_board[row][column] = ' '
                        game_board[row -1][column + i] = piece
                        if king_safe():
                            # MOVES CHANGED TO STRING
                            #x1x2 capture promote_piece "P"
                            moves = moves + str(column) + str(column + i) + old_piece + piece + "P"
                        game_board[row][column] = 'P'
                        game_board[row - 1][column + i] = old_piece
                else:
                    pass
        except:
            pass

    try:  # move two up
        if ((game_board[row - 1][column] == ' ') and (game_board[row - 2][column] == ' ')) and location >= 48:
            if row - 2 >= 0 and column >= 0:
                old_piece = game_board[row - 2][column]
                game_board[row][column] = ' '
                game_board[row - 2][column] = 'P'
                if king_safe():
                    #MOVES CHANGED TO STRING
                    #x1y1x2y2 capture
                    moves = moves + str(column) + str(row) + str(column) + str(row - 2) + old_piece
                game_board[row][column] = 'P'
                game_board[row - 2][column] = old_piece
            else:
                pass
    except:
        pass

    try: #regular move
        if game_board[row - 1][column] == ' ' and location >= 16:
            if row - 1 >= 0 and column >= 0:
                old_piece = game_board[row - 1][column]
                game_board[row][column] = ' '
                game_board[row -1][column] = 'P'
                # MOVES CHANGED TO STRING
                if king_safe():
                    moves = moves + str(column) + str(row) + str(column) + str(row - 1) + old_piece
                    # move = {
                    #     'y1': row,
                    #     'x1': column,
                    #     'y2': row - 1,
                    #     'x2': column ,
                    #     'captured': old_piece,
                    #     'promotion': False,
                    #     'score': 0,
                    #     'isKing': False
                    #
                    # }
                game_board[row][column] = 'P'
                game_board[row - 1][column] = old_piece
            else:
                pass
    except:
        pass

    try: # promotion with no capture-----------------------
        if game_board[row - 1][column] == ' ' and location < 16:
            temp_pieces = ['Q', 'R', 'B', 'K']
            if row - 1 >= 0 and column >= 0:
                for piece in temp_pieces:
                    old_piece = game_board[row - 1][column]
                    game_board[row][column] = ' '
                    game_board[row -1][column] = piece
                    # MOVES CHANGED TO STRING
                    if king_safe():
                        moves = moves + str(column) +  str(column + i)  + old_piece + piece + 'P'
                        # move = {
                        #     'y1': row,
                        #     'x1': column,
                        #     'x2': column + i,
                        #     'captured': old_piece,
                        #     'promotion': True,
                        #     'new': piece,
                        #     'score': 0,
                        #     'isKing': False
                        # }
                    game_board[row][column] = 'P'
                    game_board[row - 1][column + i] = old_piece
            else:
                pass
    except:
        pass
    return moves

def possibleR(location):
    global moves
    move_range = [-1, 1]
    row = location // 8
    column = location % 8
    temp = 1
    for i in move_range:
        try:
            while game_board[row][column + temp * i] == ' ':
                if row < 0 or column + temp * i < 0:
                    break
                old_piece = game_board[row][column + temp * i]
                game_board[row][column] = ' '
                game_board[row][column + temp * i] = 'R'
                if king_safe():
                    # MOVES CHANGED TO STRING
                    moves = moves + str(column) + str(row) + str(column + temp * i) + str(row) + old_piece
                    # move = {
                    #     'y1': row,
                    #     'x1': column,
                    #     'y2': row,
                    #     'x2': column + temp * i,
                    #     'captured': old_piece,
                    #     'promotion': False,
                    #     'score': 0,
                    #     'isKing': False
                    # }
                game_board[row][column] = 'R'
                game_board[row][column + temp * i] = old_piece
                temp = temp + 1
            if game_board[row][column + temp * i].islower():
                if row >= 0 and column + temp * i >= 0:
                    old_piece = game_board[row][column + temp * i]
                    game_board[row][column] = ' '
                    game_board[row][column + temp * i] = 'R'
                    if king_safe():
                        moves = moves + str(column) + str(row) + str(column + temp * i) + str(row) + old_piece
                        # move = {
                        #     'y1': row,
                        #     'x1': column,
                        #     'y2': row,
                        #     'x2': column + temp * i,
                        #     'captured': old_piece,
                        #     'promotion': False,
                        #     'score': 0,
                        #     'isKing': False
                        # }
                    game_board[row][column] = 'R'
                    game_board[row][column + temp * i] = old_piece
                    temp = temp + 1
        except:
            pass
        temp = 1
        try:
            while game_board[row + temp * i][column] == ' ':
                if row + temp * i < 0 or column < 0:
                    break
                old_piece = game_board[row + temp * i][column]
                game_board[row][column] = ' '
                game_board[row + temp * i][column] = 'R'
                if king_safe():
                    moves = moves + str(column) + str(row) + str(column) + str(row  + temp * i) + old_piece
                    # move = {
                    #     'y1': row,
                    #     'x1': column,
                    #     'y2': row + temp * i,
                    #     'x2': column,
                    #     'captured': old_piece,
                    #     'promotion': False,
                    #     'score': 0,
                    #     'isKing': False
                    # }
                game_board[row][column] = 'R'
                game_board[row + temp * i][column] = old_piece
                temp = temp + 1
            if game_board[row + temp * i][column].islower():
                if row + temp * i >= 0 and column >= 0:
                    old_piece = game_board[row + temp * i][column]
                    game_board[row][column] = ' '
                    game_board[row + temp * i][column] = 'R'
                    if king_safe():
                        moves = moves + str(column) + str(row) + str(column) + str(row + temp * i) + old_piece
                        # move = {
                        #     'y1': row,
                        #     'x1': column,
                        #     'y2': row + temp * i,
                        #     'x2': column,
                        #     'captured': old_piece,
                        #     'promotion': False,
                        #     'score': 0,
                        #     'isKing': False
                        # }
                    game_board[row][column] = 'R'
                    game_board[row + temp * i][column] = old_piece
                    temp = temp + 1

        except:
            pass
        temp = 1
    return moves

def possibleK(location):
    move_range = [-1,1]
    global moves
    row = location // 8
    column = location % 8
    for i in move_range:
        for j in move_range:
            try:
                if game_board[row + i][column + j * 2].islower()  or game_board[row + i][column + j * 2] == ' ':
                    if row + i >=0 and column + j * 2 >=0:
                        old_piece = game_board[row + i][column + j * 2]
                        game_board[row][column] = ' '
                        if king_safe():
                            moves = moves + str(column) + str(row) + str(column + j * 2) + str(row + i) + old_piece
                            # move = {
                            #     'y1': row,
                            #     'x1': column,
                            #     'y2': row + i,
                            #     'x2': column + j * 2,
                            #     'captured': old_piece,
                            #     'promotion': False,
                            #     'score': 0,
                            #     'isKing': False
                            # }
                        game_board[row][column] = 'K'
                        game_board[row + i][column + j * 2] = old_piece
            except:
                pass
            try:
                if game_board[row + i * 2][column + j].islower() or game_board[row + i * 2][column + j] == ' ':
                    if row + i * 2 >= 0 and column + j >= 0:
                        old_piece = game_board[row + i * 2][column + j]
                        game_board[row][column] = ' '
                        if king_safe():
                            moves = moves + str(column) + str(row) + str(column + j) + str(row + i * 2) + old_piece
                            # move = {
                            #     'y1': row,
                            #     'x1': column,
                            #     'y2': row + i * 2,
                            #     'x2': column + j,
                            #     'captured': old_piece,
                            #     'promotion': False,
                            #     'score': 0,
                            #     'isKing': False
                            # }
                        game_board[row][column] = 'K'
                        game_board[row + i * 2][column + j] = old_piece
                    else:
                        pass
            except:
                pass
    return moves

def possibleB(location):
    move_range = [-1, 1]
    global moves
    row = location // 8
    column = location % 8
    temp = 1
    for i in move_range:
        for j in move_range:
            try:
                while game_board[row + temp * i][column + temp * j] == ' ':
                    if row + temp * i < 0 or column + temp * j < 0:
                        break
                    old_piece = game_board[row + temp * i][column + temp * j]
                    game_board[row][column] = ' '
                    game_board[row + temp * i][column + temp * j] = 'B'
                    if king_safe():
                        moves = moves + str(column) + str(row) + str(column + temp * j) + str(row + temp * i) + old_piece
                        # move = {
                        #     'y1': row,
                        #     'x1': column,
                        #     'y2': row + temp * i,
                        #     'x2': column + temp * j,
                        #     'captured': old_piece,
                        #     'promotion': False,
                        #     'score': 0,
                        #     'isKing': False
                        # }
                    game_board[row][column] = 'B'
                    game_board[row + temp * i][column + temp * j] = old_piece
                    temp = temp + 1

                if game_board[row + temp * i][column + temp * j].islower():
                    if row + temp * i >= 0 and column + temp * j >= 0:
                        old_piece = game_board[row + temp * i][column + temp * j]
                        game_board[row][column] = ' '
                        game_board[row + temp * i][column + temp * j] = 'B'
                        if king_safe():
                            moves = moves + str(column) + str(row) + str(column + temp * j) + str(row + temp * i) + old_piece
                            # move = {
                            #     'y1': row,
                            #     'x1': column,
                            #     'y2': row + temp * i,
                            #     'x2': column + temp * j,
                            #     'captured': old_piece,
                            #     'promotion': False,
                            #     'score': 0,
                            #     'isKing': False
                            # }
                        game_board[row][column] = 'B'
                        game_board[row + temp * i][column + temp * j] = old_piece
            except:
                pass
            temp = 1
    return moves


def possibleQ(location):
    """Returns possible moves for the queen at a given position"""
    move_range = [-1,0, 1]
    global moves
    row = location // 8
    column = location % 8
    temp = 1
    for i in move_range:
        for j in move_range:
            try:
                while game_board[row + temp * i][column + temp * j] == ' ':
                    if row + temp * i < 0 or column + temp * j < 0:
                        break
                    old_piece = game_board[row + temp * i][column + temp * j]
                    game_board[row][column] = ' '
                    game_board[row + temp * i][column + temp * j] = 'Q'
                    if king_safe():
                        moves = moves + str(column) + str(row) + str(column + temp * j) + str(row + temp * i) + old_piece
                        # move = {
                        #     'y1': row,
                        #     'x1': column,
                        #     'y2': row + temp * i,
                        #     'x2': column + temp * j,
                        #     'captured': old_piece,
                        #     'promotion': False,
                        #     'score': 0,
                        #     'isKing': False
                        # }
                    game_board[row][column] = 'Q'
                    game_board[row + temp * i][column + temp * j] = old_piece
                    temp = temp + 1

                if game_board[row + temp * i][column + temp * j].islower():
                    if row + temp * i >=0 and column + temp * j >=0:
                        old_piece = game_board[row + temp * i][column + temp * j]
                        game_board[row][column] = ' '
                        game_board[row + temp * i][column + temp * j] = 'Q'
                        if king_safe():
                            moves = moves + str(column) + str(row) + str(column + temp * j) + str(row + temp * i) + old_piece
                            # move = {
                            #     'y1':row,
                            #     'x1':column,
                            #     'y2': row + temp * i,
                            #     'x2': column + temp * j,
                            #     'captured': old_piece,
                            #     'promotion': False,
                            #     'score': 0,
                            #     'isKing': False
                            # }
                        game_board[row][column] = 'Q'
                        game_board[row + temp * i][column + temp * j] = old_piece
                    else:
                        pass
            except:
                pass
            temp = 1
    return moves


def possibleA(location):
    """Returns possible moves for a king at a given position"""
    global king_pos_c
    global king_pos_l
    global moves
    row = location//8
    column = location%8
    for i in range(9):
        if i != 4:
            try:
                if game_board[row - 1 + i//3][column - 1 + i%3].islower() or game_board[row - 1 + i//3][column - 1 + i%3] == ' ':
                    if row - 1 + i//3 >=0 and column - 1 + i%3 >=0:
                        old_piece = game_board[row - 1 + i//3][column - 1 + i%3]
                        game_board[row][column] = ' '
                        game_board[row - 1 + i // 3][column - 1 + i % 3] = 'A'
                        king_temp = king_pos_c
                        king_pos_c = location + (i // 3) * 8 + i % 3 - 9
                        if king_safe():
                            moves = moves + str(column) + str(row) + str(column - 1 + i%3) + str(row - 1 + i//3) + old_piece
                            # move = {
                            #     'y1': row,
                            #     'x1': column,
                            #     'y2': row - 1 + i//3,
                            #     'x2': column - 1 + i%3,
                            #     'captured': old_piece,
                            #     'promotion': False,
                            #     'score': 0,
                            #     'isKing': True
                            # }

                        game_board[row][column] = 'A'
                        game_board[row - 1 + i // 3][column - 1 + i % 3] = old_piece
                        king_pos_c = king_temp
                    else:
                        pass
            except:
                pass
        #need to add castling still
    return moves



def king_safe():
    """Returns true or false whether or not king is in check or not"""
    move_range = [-1, 1]

    #bishop/queen
    temp = 1
    for i in move_range:
        for j in move_range:
            try:
                if king_pos_c // 8 + temp * i >= 0 and king_pos_c % 8 + temp * j >= 0:
                    while game_board[king_pos_c // 8 + temp * i][king_pos_c % 8 + temp * j]==' ':
                        temp = temp + 1
                    if (game_board[king_pos_c // 8 + temp * i][king_pos_c % 8 + temp * j] == 'b') or (game_board[king_pos_c // 8 + temp * i][king_pos_c % 8 + temp * j] == 'q'):
                        return False
            except:
                pass
            temp = 1

    #rook/queen
    temp = 1
    for i in move_range:
        try:
            while (game_board[king_pos_c // 8 ][king_pos_c % 8 + temp * i] == ' '):
                    temp = temp + 1
            if game_board[king_pos_c // 8][king_pos_c % 8 + temp * i] == 'r' or game_board[king_pos_c // 8][king_pos_c % 8 + temp * i] == 'q':
                return False

        except:
            pass
        temp = 1
        try:
            while (game_board[king_pos_c // 8 + temp * i][king_pos_c % 8 ] == ' '):
                temp = temp + 1
            if game_board[king_pos_c // 8 + temp * i][king_pos_c % 8] == 'r' or game_board[king_pos_c // 8 + temp * i][king_pos_c % 8] == 'q':
                return False
        except:
            pass

    #knight
    for i in move_range:
        for j in move_range:
            if king_pos_c / 8 + i >= 0 and king_pos_c % 8 + j * 2 >= 0:
                try:
                    if game_board[king_pos_c / 8 + i][king_pos_c % 8 + j * 2]=='k':
                        return False
                except:
                    pass
                try:
                    if game_board[king_pos_c / 8 + i * 2][king_pos_c % 8 + j] =='k':
                        return False
                except:
                    pass

     #pawn (in danger if pawn one diaganol in any direction)
    if king_pos_c >= 16:
        try:
            if game_board[king_pos_c/80-1][king_pos_c%8-1] == 'p':
                return False
        except:
            pass
        try:
            if game_board[king_pos_c/80-1][king_pos_c%8+1] == 'p':
                return False
        except:
            pass
    #king
    move_range = [-1,0,1]
    for i in move_range:
        for j in move_range:
            if (i != 0 or j != 0) and (king_pos_c / 8 + i >=0 and king_pos_c % 8 + j >=0):
                try:
                    if game_board[king_pos_c / 8 + i][king_pos_c % 8 + j] =='a':
                        return False
                except:
                    pass

    return True

def make_move(move):
    """Make a move"""
    #moves are in format x1x2y2 capture newPiece promotion for pawns with promotions
    #PAWNS###############################################
    #               x1y1x2y2 capture
    #               x1x2 capture promote_piece "P"
    ###################################################
    print(move)

    if (move[4] != 'P'):
        game_board[int(move[3])][int(move[2])] = game_board[int(move[1])][int(move[0])]
        game_board[int(move[1])][int(move[0])] = ' '
    else:
        game_board[int(move[0])][1] = ' '
        game_board[int(move[1])][0] = move[3]



def undo_move(move):
    """undo a move"""
    if (move[4] != 'P'):
        game_board[int(move[1])][int(move[0])] = game_board[int(move[3])][int(move[2])]
        game_board[int(move[3])][int(move[2])] = move[4]
    else:
        game_board[int(move[0])][1] = 'P'
        game_board[int(move[1])][0] = move[3].lower()

