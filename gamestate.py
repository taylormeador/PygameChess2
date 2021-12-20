import square


class GameState:
    def __init__(self):
        self.board = [[square.a8, square.b8, square.c8, square.d8, square.e8, square.f8, square.g8, square.h8],
                      [square.a7, square.b7, square.c7, square.d7, square.e7, square.f7, square.g7, square.h7],
                      [square.a6, square.b6, square.c6, square.d6, square.e6, square.f6, square.g6, square.h6],
                      [square.a5, square.b5, square.c5, square.d5, square.e5, square.f5, square.g5, square.h5],
                      [square.a4, square.b4, square.c4, square.d4, square.e4, square.f4, square.g4, square.h4],
                      [square.a3, square.b3, square.c3, square.d3, square.e3, square.f3, square.g3, square.h3],
                      [square.a2, square.b2, square.c2, square.d2, square.e2, square.f2, square.g2, square.h2],
                      [square.a1, square.b1, square.c1, square.d1, square.e1, square.f1, square.g1, square.h1]]
        self.white_to_move = True
        self.checkmate = False
        self.stalemate = False
        self.draw = False
