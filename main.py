import pygame as p
import move as m
import gamestate
import engine


p.init()
BOARD_WIDTH = BOARD_HEIGHT = 512
DIMENSION = 8
SQ_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

light_square_color = "ivory"
dark_square_color = "dark green"
white_pov = True


"""
This function will load the images for our pieces. Different piece sets are stored in different folders
"""
def load_images(piece_set):
    # TODO implement alternate piece image options
    pieces = ['wP', 'wN', 'wB', 'wR', 'wQ', 'wK', 'bP', 'bN', 'bB', 'bR', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/' + piece_set + '/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))


"""
Main game loop. Handles user input and graphics
"""
def main():
    p.init()
    p.display.set_caption('Pygame Chess 2')
    screen = p.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    load_images('standard')  # TODO more image options
    square_selected = None  # keeps track of which square the player last selected
    player_clicks = []  # list that keeps track of two consecutive player clicks' squares
    game_over = False
    clock = p.time.Clock()
    gs = gamestate.GameState()  # init gamestate instance
    gs.valid_moves = engine.get_valid_moves(gs)  # get the valid first moves of the game
    engine.get_attacks(gs)  # get the squares black is attacking
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                if not game_over:
                    location = p.mouse.get_pos()  # (x, y) of mouse click position
                    col = location[0] // SQ_SIZE  # get column number from location
                    row = location[1] // SQ_SIZE  # get row number from location
                    if square_selected == gs.board[row][col]:  # if the player selects the same square twice
                        square_selected = None  # deselect
                        player_clicks = []  # clear player_clicks
                    else:  # if the player clicks on a piece or empty square
                        square_selected = gs.board[row][col]
                        player_clicks.append(square_selected)  # appends for both 1st or 2nd click
                    if len(player_clicks) == 2:  # after second click
                        move = m.Move(player_clicks[0], player_clicks[1], gs.board)  # store desired move info
                        for i in range(len(gs.valid_moves)):  # loop through all the valid moves
                            if move == gs.valid_moves[i]:  # if the player move is valid
                                gs.make_move(gs.valid_moves[i])  # execute the valid move
                                break  # stop looping
                        square_selected = None  # deselect
                        player_clicks = []  # clear player_clicks

        draw_game_state(gs, screen)

        p.display.flip()
        clock.tick(MAX_FPS)


"""
Draws the current board state
"""
def draw_game_state(gs, screen):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            square = gs.board[row][col]
            draw_square(screen, square, light_square_color, dark_square_color)


"""
Helper function for the draw_game_state() function. Draws a square and it's piece
"""
def draw_square(screen, square, light_square_color, dark_square_color):
    color = light_square_color if square.color == "light" else dark_square_color
    p.draw.rect(screen, color, p.Rect(square.x, square.y, SQ_SIZE, SQ_SIZE))
    if square.piece != 0:
        screen.blit(IMAGES[str(square.piece)], p.Rect(square.x, square.y, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
