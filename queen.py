class Queen:
    def __init__(self, color, start_location):
        self.color = color
        self.start_location = start_location

    def __str__(self):
        return self.color + "Q"

    def get_all_possible_moves(self, board):
        pass

    def get_all_valid_moves(self, board):
        pass


# initialize queens
d1 = Queen("w", "d1")

d8 = Queen("b", "d8")
