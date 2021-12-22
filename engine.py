import move as m
import square as s
import gamestate
import pawn
import knight
import bishop
import rook
import queen
import king as k

'''
Updates and returns a list of move objects representing valid moves
'''
def get_valid_moves(gs):
    #  traverse the board looking for pieces
    for row in range(8):
        for col in range(8):
            square = gs.board[row][col]
            piece = square.piece
            if piece != 0:
                # if you find a piece and it's their turn
                if (piece.color == 'w' and gs.white_to_move) or (piece.color == 'b' and not gs.white_to_move):
                    piece.get_moves(gs)  # find all the valid moves for that piece
    return gs.valid_moves


'''
Returns a list of lists of squares that are under attack
'''
def get_attacks(gs):
    gs.squares_attacked = []
    for row in range(8):
        for col in range(8):
            piece = gs.board[row][col].piece
            if piece != 0:
                if piece.color == gs.enemy_color:
                    gs.squares_attacked.append(piece.find_attacks(gs))
    return gs.squares_attacked


'''
Returns True if the move would result in checkmate, False otherwise
'''
def is_checkmate(gs, start_square, end_square):
    look_ahead = gs
    look_ahead.make_move(m.Move(start_square, end_square, look_ahead.board))
    king_name = 'wK' if not look_ahead.white_to_move else 'bK'
    '''for row in range(8):
        for col in range(8):
            square = look_ahead.board[row][col]
            if square.piece != 0:
                if square.piece.name == king_name:
                    king = square.piece
                    if len(king.get_moves(look_ahead)) == 0:
                        return True'''
    return False
