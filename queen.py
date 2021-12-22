import engine
import move as m

class Queen:
    def __init__(self, color, row, col):
        self.color = color
        self.piece_type = 'Q'
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
        # The idea for queen moves is to combine the bishop and rook moves
        # bishop moves
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
        # rook moves
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for move in moves:
            for i in range(1, 8):
                candidate_row = self.row + move[0] * i
                candidate_col = self.col + move[1] * i
                if 0 <= candidate_row <= 7 and 0 <= candidate_col <= 7:
                    start_square = gs.board[self.row][self.col]  # the square we are moving from
                    end_square = gs.board[candidate_row][candidate_col]  # the square we are moving to
                    end_piece = end_square.piece  # the piece (if it exists) at the square that is being attacked
                    print(start_square, end_square)
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
                    else:  # ally piece
                        break
        return None

    def find_attacks(self, gs):
        self.is_attacking = []


# initialize queens
d1 = Queen("w", 7, 3)

d8 = Queen("b", 0, 3)
