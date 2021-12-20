class Bishop:
    def __init__(self, color, start_location):
        self.color = color
        self.start_location = start_location

    def __str__(self):
        return self.color + "B"

    def get_all_possible_moves(self, board):
        pass

    def get_all_valid_moves(self, board):
        pass


# initialize bishops
c1 = Bishop("w", "c1")
f1 = Bishop("w", "f1")

c8 = Bishop("b", "c8")
f8 = Bishop("b", "f8")
