import square
import engine
import queen


class GameState:
    def __init__(self):
        # the board will always be represented internally with white being at the bottom of the board
        # if the player chooses to play as black, the board will be drawn flipped but remain the same internally
        self.board = [[square.a8, square.b8, square.c8, square.d8, square.e8, square.f8, square.g8, square.h8],
                      [square.a7, square.b7, square.c7, square.d7, square.e7, square.f7, square.g7, square.h7],
                      [square.a6, square.b6, square.c6, square.d6, square.e6, square.f6, square.g6, square.h6],
                      [square.a5, square.b5, square.c5, square.d5, square.e5, square.f5, square.g5, square.h5],
                      [square.a4, square.b4, square.c4, square.d4, square.e4, square.f4, square.g4, square.h4],
                      [square.a3, square.b3, square.c3, square.d3, square.e3, square.f3, square.g3, square.h3],
                      [square.a2, square.b2, square.c2, square.d2, square.e2, square.f2, square.g2, square.h2],
                      [square.a1, square.b1, square.c1, square.d1, square.e1, square.f1, square.g1, square.h1]]
        self.white_to_move = True
        self.ally_color = 'w'  # white
        self.enemy_color = 'b'  # black
        self.checkmate = False
        self.stalemate = False
        self.draw = False
        self.valid_moves = []  # will contain move objects
        self.squares_attacked = []  # will contain square names which are hit by enemy pieces

    def change_turns(self):
        self.white_to_move = not self.white_to_move  # change turn
        self.ally_color = 'w' if self.white_to_move else 'b'  # update ally color
        self.enemy_color = 'b' if self.white_to_move else 'w'  # update enemy color
        self.valid_moves = []  # clear valid moves
        self.valid_moves = engine.get_valid_moves(self)  # get new valid moves
        engine.get_attacks(self)  # get new attacks

    def make_move(self, move):
        if move.en_passant_possible_left or move.en_passant_possible_right:
            move.piece_moved.set_en_passant_possibilities(self, move)  # tell pawns that they can take en passant
        self.board[move.start_row][move.start_col].piece = 0  # make the starting square empty
        if move.is_capture:  # if a piece was captured
            if move.en_passant_move:  # if it was en passant, find the square that the captured pawn was on
                for row in range(8):
                    for col in range(8):
                        captured_square = self.board[row][col]
                        if captured_square.location() == move.piece_captured.location():  # square the pawn was captured from
                            captured_square.piece = 0  # delete the piece from that square
            move.end_square.piece = 0
            move.piece_captured.row = None  # update row and col
            move.piece_captured.col = None

        if move.promotion_move:
            self.board[move.end_row][move.end_col].piece = 0
            self.board[move.end_row][move.end_col].piece = queen.Queen(move.piece_moved.color, move.end_square.name)  # give the piece to the new square
        else:
            self.board[move.end_row][move.end_col].piece = move.piece_moved  # give the piece to the new square
            self.board[move.end_row][move.end_col].piece.row = move.end_row  # update row of piece moved
            self.board[move.end_row][move.end_col].piece.col = move.end_col  # update col of piece moved

        if move.piece_moved.piece_type == 'P':  # update pawn property if it moved
            move.piece_moved.first_move = False
        self.change_turns()  # change turns

    def undo_move(self, gs):
        pass
