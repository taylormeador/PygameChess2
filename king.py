import move as m

files_to_cols_white = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
files_to_cols_black = {'a': 7, 'b': 6, 'c': 5, 'd': 4, 'e': 3, 'f': 2, 'g': 1, 'h': 0}
ranks_to_rows = {1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}

class King:
    def __init__(self, color, row, col):
        self.color = color
        self.piece_type = 'K'
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
        moves = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        for move in moves:
            candidate_row = self.row + move[0]
            candidate_col = self.col + move[1]
            if 0 <= candidate_row <= 7 and 0 <= candidate_col <= 7:
                start_square = gs.board[self.row][self.col]
                end_square = gs.board[candidate_row][candidate_col]
                end_piece = end_square.piece
                if end_square.name not in gs.squares_attacked:  # if the square is not attacked by an enemy piece
                    if end_piece == 0:  # empty square
                        gs.valid_moves.append(m.Move(start_square, end_square, gs.board))
        return gs.valid_moves

    def find_attacks(self, gs):
        self.is_attacking = []


# initialize queens
e1 = King("w", 7, 4)

e8 = King("b", 0, 4)
