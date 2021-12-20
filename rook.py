class Rook:
    def __init__(self, color, start_location):
        self.color = color
        self.start_location = start_location

    def __str__(self):
        return self.color + "R"

    def get_all_possible_moves(self, board):
        pass

    def get_all_valid_moves(self, board):
        pass


# initialize bishops
a1 = Rook("w", "a1")
h1 = Rook("w", "h1")

a8 = Rook("b", "a8")
h8 = Rook("b", "h8")
