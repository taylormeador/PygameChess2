import move as m
import engine

files_to_cols_white = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
files_to_cols_black = {'a': 7, 'b': 6, 'c': 5, 'd': 4, 'e': 3, 'f': 2, 'g': 1, 'h': 0}
ranks_to_rows = {1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}


class Bishop:
    def __init__(self, color, row, col):
        self.color = color  # 'w' or 'b'
        self.piece_type = 'B'  # bishop
        self.name = self.color + self.piece_type  # e.g.'wB'
        self.row = row  # 0-7
        self.col = col  # 0-7
        self.is_attacking = []  # [a3, h5, etc]

    def __str__(self):
        return self.name

    def location(self):
        location = (self.row, self.col)
        return location

    def get_moves(self, gs):
        moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for move in moves:
            for i in range(1, 8):
                candidate_row = self.row + move[0] * i  # row that we are looking at moving to
                candidate_col = self.col + move[1] * i  # col that we are looking at moving to
                if 0 <= candidate_row <= 7 and 0 <= candidate_col <= 7:  # make sure the move is on the board
                    start_square = gs.board[self.row][self.col]  # the square we are moving from
                    end_square = gs.board[candidate_row][candidate_col]  # the square we are moving to
                    end_piece = end_square.piece  # the piece (if it exists) at the square that is being attacked
                    if end_piece == 0:  # empty square
                        gs.valid_moves.append(m.Move(start_square, end_square, gs.board))
                    elif end_piece.name == gs.enemy_color + 'K':  # if the move attacks the enemy king
                        if engine.is_checkmate(gs, start_square, end_square):
                            gs.valid_moves.append(m.Move(start_square, end_square, gs.board, is_checkmate=True))
                            break
                        else:
                            gs.valid_moves.append(m.Move(start_square, end_square, gs.board, is_check=True))
                            break
                    elif end_piece.color == gs.enemy_color:  # if the move is a capture
                        gs.valid_moves.append(m.Move(start_square, end_square, gs.board))
                        break
                    else:
                        break
        return None

    def find_attacks(self, gs):
        self.is_attacking = []
        moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for move in moves:
            for i in range(1, 8):
                candidate_row = self.row + move[0] * i  # row that we are looking at moving to
                candidate_col = self.col + move[1] * i  # col that we are looking at moving to
                if 0 <= candidate_row <= 7 and 0 <= candidate_col <= 7:  # make sure the move is on the board
                    start_square = gs.board[self.row][self.col]  # the square we are moving from
                    end_square = gs.board[candidate_row][candidate_col]  # the square we are moving to
                    end_piece = end_square.piece  # the piece (if it exists) at the square that is being attacked
                    if end_piece == 0:  # empty square
                        self.is_attacking.append(end_square.name)
                        continue
                    elif end_piece.color == gs.ally_color:  # if it attacks our piece
                        self.is_attacking.append(end_square.name)
                        break
                    else:  # it attacks its own piece
                        break
        return self.is_attacking


# initialize bishops
c1 = Bishop("w", 7, 2)
f1 = Bishop("w", 7, 5)

c8 = Bishop("b", 0, 2)
f8 = Bishop("b", 0, 5)
