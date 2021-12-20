import pawn
import knight
import bishop
import rook
import queen
import king
import main

SQ_SIZE = 64
files_to_cols_white = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
files_to_cols_black = {"a": 7, "b": 6, "c": 5, "d": 4, "e": 3, "f": 2, "g": 1, "h": 0}
ranks_to_rows = {1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}


class Square:
    def __init__(self, name, piece, color):
        self.name = name
        self.piece = piece
        self.color = color
        self.row = ranks_to_rows[int(name[1])] if main.white_pov else int(name[1]) - 1
        self.col = files_to_cols_white[name[0]] if main.white_pov else files_to_cols_black[name[0]]
        self.x = self.col * SQ_SIZE
        self.y = self.row * SQ_SIZE


# initialize squares
# pawns
a2 = Square("a2", pawn.a2, "light")
b2 = Square("b2", pawn.b2, "dark")
c2 = Square("c2", pawn.c2, "light")
d2 = Square("d2", pawn.d2, "dark")
e2 = Square("e2", pawn.e2, "light")
f2 = Square("f2", pawn.f2, "dark")
g2 = Square("g2", pawn.g2, "light")
h2 = Square("h2", pawn.h2, "dark")
a7 = Square("a7", pawn.a7, "dark")
b7 = Square("b7", pawn.b7, "light")
c7 = Square("c7", pawn.c7, "dark")
d7 = Square("d7", pawn.d7, "light")
e7 = Square("e7", pawn.e7, "dark")
f7 = Square("f7", pawn.f7, "light")
g7 = Square("g7", pawn.g7, "dark")
h7 = Square("h7", pawn.h7, "light")

# knights
b1 = Square("b1", knight.b1, "light")
g1 = Square("g1", knight.g1, "dark")
b8 = Square("b8", knight.b8, "dark")
g8 = Square("g8", knight.g8, "light")

# bishops
c1 = Square("c1", bishop.c1, "dark")
f1 = Square("f1", bishop.f1, "light")
c8 = Square("c8", bishop.c8, "light")
f8 = Square("f8", bishop.f8, "dark")

# rooks
a1 = Square("a1", rook.a1, "dark")
h1 = Square("h1", rook.h1, "light")
a8 = Square("a8", rook.a8, "light")
h8 = Square("h8", rook.h8, "dark")

# queens
d1 = Square("d1", queen.d1, "light")
d8 = Square("d8", queen.d8, "dark")

# kings
e1 = Square("e1", king.e1, "dark")
e8 = Square("e8", king.e8, "light")

# empty squares
a3 = Square("a3", 0, "dark")
b3 = Square("b3", 0, "light")
c3 = Square("c3", 0, "dark")
d3 = Square("d3", 0, "light")
e3 = Square("e3", 0, "dark")
f3 = Square("f3", 0, "light")
g3 = Square("g3", 0, "dark")
h3 = Square("h3", 0, "light")

a4 = Square("a4", 0, "light")
b4 = Square("b4", 0, "dark")
c4 = Square("c4", 0, "light")
d4 = Square("d4", 0, "dark")
e4 = Square("e4", 0, "light")
f4 = Square("f4", 0, "dark")
g4 = Square("g4", 0, "light")
h4 = Square("h4", 0, "dark")

a5 = Square("a5", 0, "dark")
b5 = Square("b5", 0, "light")
c5 = Square("c5", 0, "dark")
d5 = Square("d5", 0, "light")
e5 = Square("e5", 0, "dark")
f5 = Square("f5", 0, "light")
g5 = Square("g5", 0, "dark")
h5 = Square("h5", 0, "light")

a6 = Square("a6", 0, "light")
b6 = Square("b6", 0, "dark")
c6 = Square("c6", 0, "light")
d6 = Square("d6", 0, "dark")
e6 = Square("e6", 0, "light")
f6 = Square("f6", 0, "dark")
g6 = Square("g6", 0, "light")
h6 = Square("h6", 0, "dark")
