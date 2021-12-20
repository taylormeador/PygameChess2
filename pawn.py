class Pawn:
    def __init__(self, color, start_location):
        self.color = color
        self.start_location = start_location

    def __str__(self):
        return self.color + "P"

    def get_all_possible_moves(self, board):
        pass

    def get_all_valid_moves(self, board):
        pass


# initialize pawns
a7 = Pawn("b", "a7")
b7 = Pawn("b", "b7")
c7 = Pawn("b", "c7")
d7 = Pawn("b", "d7")
e7 = Pawn("b", "e7")
f7 = Pawn("b", "f7")
g7 = Pawn("b", "g7")
h7 = Pawn("b", "h7")

a2 = Pawn("w", "a7")
b2 = Pawn("w", "b7")
c2 = Pawn("w", "c7")
d2 = Pawn("w", "d7")
e2 = Pawn("w", "e7")
f2 = Pawn("w", "f7")
g2 = Pawn("w", "g7")
h2 = Pawn("w", "h7")