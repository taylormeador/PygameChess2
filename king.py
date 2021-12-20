class King:
    def __init__(self, color, start_location):
        self.color = color
        self.start_location = start_location

    def __str__(self):
        return self.color + "K"

    def get_all_possible_moves(self, board):
        pass

    def get_all_valid_moves(self, board):
        pass


# initialize queens
e1 = King("w", "e1")

e8 = King("b", "e8")
