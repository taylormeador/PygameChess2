class Knight:
    def __init__(self, color, start_location):
        self.color = color
        self.start_location = start_location

    def __str__(self):
        return self.color + "N"

    def get_all_possible_moves(self, board):
        pass

    def get_all_valid_moves(self, board):
        pass


# initialize knights
b1 = Knight("w", "b1")
g1 = Knight("w", "g1")

b8 = Knight("b", "b8")
g8 = Knight("b", "g8")
