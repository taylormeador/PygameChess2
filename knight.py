import move as m
import engine

files_to_cols_white = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
files_to_cols_black = {'a': 7, 'b': 6, 'c': 5, 'd': 4, 'e': 3, 'f': 2, 'g': 1, 'h': 0}
ranks_to_rows = {1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}

class Knight:
    def __init__(self, color, row, col):
        self.color = color
        self.piece_type = 'N'
        self.name = self.color + self.piece_type
        self.row = row
        self.col = col
        self.is_attacking = []

    def __str__(self):
        return self.name

    def location(self):
        location = (self.row, self.col)
        return location

    def get_moves(self, gs):
        knight_moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        for move in knight_moves:
            candidate_row = self.row + move[0]  # row that we are looking at moving to
            candidate_col = self.col + move[1]  # col that we are looking at moving to
            if 0 <= candidate_row <= 7 and 0 <= candidate_col <= 7:  # make sure the move is on the board
                start_square = gs.board[self.row][self.col]  # the square we are moving from
                end_square = gs.board[candidate_row][candidate_col]  # the square we are moving to
                end_piece = end_square.piece  # the piece (if it exists) at the square that is being attacked
                if end_piece == 0:  # empty square
                    gs.valid_moves.append(m.Move(start_square, end_square, gs.board))
                elif end_piece.name == gs.enemy_color + 'K':  # if the move attacks the enemy king
                    if engine.is_checkmate(gs, start_square, end_square):
                        gs.valid_moves.append(m.Move(start_square, end_square, gs.board, is_checkmate=True))
                    else:
                        gs.valid_moves.append(m.Move(start_square, end_square, gs.board, is_check=True))
                elif end_piece.color == gs.enemy_color:  # if the move is a capture
                    gs.valid_moves.append(m.Move(start_square, end_square, gs.board))
        return None

    def find_attacks(self, gs):
        self.is_attacking = []
        knight_moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        for move in knight_moves:
            candidate_row = self.row + move[0]  # row that we are looking at moving to
            candidate_col = self.col + move[1]  # col that we are looking at moving to
            if 0 <= candidate_row <= 7 and 0 <= candidate_col <= 7:  # make sure the move is on the board
                end_square = gs.board[candidate_row][candidate_col]  # the square we are moving to
                end_piece = end_square.piece
                if end_piece == 0:  # attacks an empty square
                    self.is_attacking.append(end_square.name)  # add square to list of squares this piece is attacking
                elif end_piece.color == gs.ally_color:  # attacks an enemy piece
                    self.is_attacking.append(end_square.name)  # add square to list of squares this piece is attacking
        return self.is_attacking


# initialize knights
b1 = Knight("w", 7, 1)
g1 = Knight("w", 7, 6)

b8 = Knight("b", 0, 1)
g8 = Knight("b", 0, 6)
