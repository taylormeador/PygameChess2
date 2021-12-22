class Move:
    def __init__(self, start_square, end_square, gs, en_passant_possible_left=False, en_passant_possible_right=False,
                 en_passant_move=False, castle_move=False, promotion_move=False, is_check=False, is_checkmate=False, is_stalemate=False,
                 is_draw=False):
        # square info
        self.start_square = start_square
        self.start_row = start_square.row
        self.start_col = start_square.col
        self.end_square = end_square
        self.end_row = end_square.row
        self.end_col = end_square.col
        self.piece_moved = start_square.piece
        self.end_piece = end_square.piece
        self.is_capture = self.end_piece != 0
        self.piece_captured = self.end_piece if self.is_capture else 0
        # en passant
        self.en_passant_possible_left = en_passant_possible_left
        self.en_passant_possible_right = en_passant_possible_right
        self.en_passant_move = en_passant_move
        if self.en_passant_move:
            self.is_capture = True
            self.piece_captured = gs.board[self.end_row + 1][self.end_col].piece if gs.white_to_move else gs.board[self.end_row - 1][self.end_col].piece
        # castle
        self.castle_move = castle_move
        # promotion
        self.promotion_move = promotion_move
        # check, checkmate, stalemate
        self.is_check = is_check
        self.is_checkmate = is_checkmate
        self.is_stalemate = is_stalemate
        self.is_draw = is_draw
        # unique ID for every possible move
        self.move_ID = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col

    def __eq__(self, other):
        if isinstance(other, Move):
            return other.move_ID == self.move_ID
        return False
