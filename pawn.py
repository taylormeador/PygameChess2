import move as m

class Pawn:
    def __init__(self, color, row, col):
        self.color = color
        self.piece_type = 'P'
        self.name = self.color + self.piece_type
        self.row = row
        self.col = col
        self.is_attacking = []
        self.first_move = True
        self.en_passant_possible_left = False
        self.en_passant_possible_right = False

    def __str__(self):
        return self.name

    def location(self):
        location = (self.row, self.col)
        return location

    def get_moves(self, gs):
        start_square = gs.board[self.row][self.col]
        if gs.white_to_move and start_square.piece.color == 'w':  # pawns move from the bottom to the top of the board
            one_square_up = gs.board[self.row - 1][self.col]
            # single square move
            if one_square_up.piece == 0:  # square in front of the pawn is empty
                if one_square_up.row == 0:  # pawn is promoting
                    gs.valid_moves.append(m.Move(start_square, one_square_up, gs, promotion_move=True))  # append the move
                else:
                    gs.valid_moves.append(m.Move(start_square, one_square_up, gs))  # append the move
                # double square move
                if self.first_move:  # pawns can move two squares forward on their first move
                    two_squares_up = gs.board[self.row - 2][self.col]
                    if two_squares_up.piece == 0:  # two squares in front of the pawn is empty
                        double_move = m.Move(start_square, two_squares_up, gs)  # we will need to access for en passant
                        en_passant_possible_left = False  # reset flags
                        en_passant_possible_right = False
                        if self.col > 0:  # we are not on the 'a' file
                            left_piece = gs.board[double_move.end_row][double_move.end_col - 1].piece
                            if left_piece != 0:
                                if left_piece.name == 'bP':  # there is an enemy pawn on the row we are moving to, to the left
                                    en_passant_possible_right = True  # pawn on our left can take towards the right
                        if self.col < 7:  # we are not on the 'h' file
                            right_piece = gs.board[double_move.end_row][double_move.end_col + 1].piece
                            if right_piece != 0:
                                if right_piece.name == 'bP':  # it is an enemy pawn on the row we are moving to, to the right
                                    en_passant_possible_left = True  # pawn on our right can take towards the left
                        double_move = m.Move(start_square, two_squares_up, gs, en_passant_possible_left=en_passant_possible_left,
                                             en_passant_possible_right=en_passant_possible_right)
                        gs.valid_moves.append(double_move)  # append the move with en passant flags
            # capture moves
            if self.col > 0:  # we are not on the 'a' file, so we look left
                left_diagonal = gs.board[self.row - 1][self.col - 1]
                if left_diagonal.piece != 0:  # square diagonal left of the pawn is not empty
                    if left_diagonal.piece.color == 'b':  # the piece on the square is an enemy piece
                        if one_square_up.row == 0:  # pawn is promoting
                            gs.valid_moves.append(m.Move(start_square, left_diagonal, gs, promotion_move=True))  # append the move
                        else:
                            gs.valid_moves.append(m.Move(start_square, left_diagonal, gs))  # append the move
            if self.col < 7:  # we are not on the 'h' file, so we can look right
                right_diagonal = gs.board[self.row - 1][self.col + 1]
                if right_diagonal.piece != 0:  # square diagonal right of the pawn is not empty
                    if right_diagonal.piece.color == 'b':  # the piece on the square is an enemy piece
                        if one_square_up.row == 0:  # pawn is promoting
                            gs.valid_moves.append(m.Move(start_square, right_diagonal, gs, promotion_move=True))  # append the move
                        else:
                            gs.valid_moves.append(m.Move(start_square, right_diagonal, gs))  # append the move
            # en passant move
            if self.en_passant_possible_left:
                left_diagonal = gs.board[self.row - 1][self.col - 1]
                gs.valid_moves.append(m.Move(start_square, left_diagonal, gs, en_passant_move=True))  # append the move
            if self.en_passant_possible_right:
                right_diagonal = gs.board[self.row - 1][self.col + 1]
                gs.valid_moves.append(m.Move(start_square, right_diagonal, gs, en_passant_move=True))  # append the move
        else:  # pawns move from the top to the bottom of the board
            one_square_down = gs.board[self.row + 1][self.col]
            # single square move
            if one_square_down.piece == 0:  # square in front of the pawn is empty
                if one_square_down.row == 7:  # pawn is promoting
                    gs.valid_moves.append(m.Move(start_square, one_square_down, gs, promotion_move=True))  # append the move
                else:
                    gs.valid_moves.append(m.Move(start_square, one_square_down, gs))  # append the move
                # double square move
                if self.first_move:  # pawns can move two squares forward on their first move
                    two_squares_down = gs.board[self.row + 2][self.col]
                    if two_squares_down.piece == 0:  # two squares in front of the pawn is empty
                        double_move = m.Move(start_square, two_squares_down, gs)  # we will need to access for en passant
                        en_passant_possible_left = False  # reset flags
                        en_passant_possible_right = False
                        if self.col > 0:  # we are not on the 'a' file
                            left_piece = gs.board[double_move.end_row][double_move.end_col - 1].piece
                            if left_piece != 0:
                                if left_piece.name == 'wP':  # there is an enemy pawn on the row we are moving to, to the left
                                    en_passant_possible_right = True  # pawn on our left can take toward its right
                        if self.col < 7:  # we are not on the 'h' file
                            right_piece = gs.board[double_move.end_row][double_move.end_col + 1].piece
                            if right_piece != 0:
                                if right_piece.name == 'wP':  # it is an enemy pawn on the row we are moving to, to the right
                                    en_passant_possible_left = True  # pawn on our right can take toward its left
                        gs.valid_moves.append(m.Move(start_square, two_squares_down, gs,
                                              en_passant_possible_left=en_passant_possible_left,
                                              en_passant_possible_right=en_passant_possible_right))  # append the move with en passant flags

            # capture moves
            if self.col > 0:  # we are not on the 'a' file, so we look left
                left_diagonal = gs.board[self.row + 1][self.col - 1]
                if left_diagonal.piece != 0:  # square diagonal left of the pawn is not empty
                    if left_diagonal.piece.color == 'w':  # the piece on the square is an enemy piece
                        if one_square_down.row == 7:  # pawn is promoting
                            gs.valid_moves.append(m.Move(start_square, left_diagonal, gs, promotion_move=True))  # append the move
                        else:
                            gs.valid_moves.append(m.Move(start_square, left_diagonal, gs))  # append the move
            if self.col < 7:  # we are not on the 'h' file, so we can look right
                right_diagonal = gs.board[self.row + 1][self.col + 1]
                if right_diagonal.piece != 0:  # square diagonal right of the pawn is not empty
                    if right_diagonal.piece.color == 'w':  # the piece on the square is an enemy piece
                        if one_square_down.row == 7:  # pawn is promoting
                            gs.valid_moves.append(m.Move(start_square, right_diagonal, gs, promotion_move=True))  # append the move
                        else:
                            gs.valid_moves.append(m.Move(start_square, right_diagonal, gs))  # append the move
            # en passant move
            if self.en_passant_possible_left:
                left_diagonal = gs.board[self.row + 1][self.col - 1]
                gs.valid_moves.append(m.Move(start_square, left_diagonal, gs, en_passant_move=True))  # append the move
            if self.en_passant_possible_right:
                right_diagonal = gs.board[self.row + 1][self.col + 1]
                gs.valid_moves.append(m.Move(start_square, right_diagonal, gs, en_passant_move=True))  # append the move
        return None

    def find_attacks(self, gs):
        self.is_attacking = []
        start_square = gs.board[self.row][self.col]
        if not gs.white_to_move and start_square.piece.color == 'w':  # pawns move from the bottom to the top of the board
            if self.col > 0:  # we are not on the 'a' file, so we look left
                left_diagonal = gs.board[self.row - 1][self.col - 1]
                self.is_attacking.append(left_diagonal.name)  # append the square
            if self.col < 7:  # we are not on the 'h' file, so we can look right
                right_diagonal = gs.board[self.row - 1][self.col + 1]
                self.is_attacking.append(right_diagonal.name)  # append the square
        elif gs.white_to_move and start_square.piece.color == 'b':
            if self.col > 0:  # we are not on the 'a' file, so we look left
                left_diagonal = gs.board[self.row + 1][self.col - 1]
                self.is_attacking.append(left_diagonal.name)  # append the square
            if self.col < 7:  # we are not on the 'h' file, so we can look right
                right_diagonal = gs.board[self.row + 1][self.col + 1]
                self.is_attacking.append(right_diagonal.name)  # append the square
        return self.is_attacking

    """
    When a pawn is moved, if the move results in the other color being able to take en passant,
    this function sets the attributes of the pawn(s) that can take the pawn.
    The function is called before the move is executed
    Left/Right is from the pawn's perspective who is capturing
    """
    def set_en_passant_possibilities(self, gs, move):
        start_square = gs.board[self.row][self.col]
        if gs.white_to_move and start_square.piece.color == 'w':  # pawns move from the bottom to the top of the board
            if move.en_passant_possible_right:  # if there is a pawn directly on our left after the move
                left_square = gs.board[self.row - 2][self.col - 1]
                left_square.piece.en_passant_possible_right = True  # the opposing pawn takes towards the right
            if move.en_passant_possible_left:  # if there is a pawn on the end row and immediately right
                right_square = gs.board[self.row - 2][self.col + 1]
                right_square.piece.en_passant_possible_left = True  # the opposing pawn can take toward the left
        if not gs.white_to_move and start_square.piece.color == 'b':  # pawns move from the top to the bottom of the board
            if move.en_passant_possible_right:  # if there is a pawn on the end row and immediately right
                left_square = gs.board[self.row + 2][self.col - 1]
                left_square.piece.en_passant_possible_right = True  # the opposing pawn can take toward the right
            if move.en_passant_possible_left:  # if there is a pawn on the end row and immediately right
                right_square = gs.board[self.row + 2][self.col + 1]
                right_square.piece.en_passant_possible_left = True  # the opposing pawn can take toward the left


# initialize pawns
a7 = Pawn("b", 1, 0)
b7 = Pawn("b", 1, 1)
c7 = Pawn("b", 1, 2)
d7 = Pawn("b", 1, 3)
e7 = Pawn("b", 1, 4)
f7 = Pawn("b", 1, 5)
g7 = Pawn("b", 1, 6)
h7 = Pawn("b", 1, 7)

a2 = Pawn("w", 6, 0)
b2 = Pawn("w", 6, 1)
c2 = Pawn("w", 6, 2)
d2 = Pawn("w", 6, 3)
e2 = Pawn("w", 6, 4)
f2 = Pawn("w", 6, 5)
g2 = Pawn("w", 6, 6)
h2 = Pawn("w", 6, 7)
