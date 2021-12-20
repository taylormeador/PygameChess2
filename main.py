import pygame as p
import gamestate


p.init()
BOARD_WIDTH = BOARD_HEIGHT = 512
DIMENSION = 8
SQ_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

light_square_color = "white"
dark_square_color = "dark green"
white_pov = True


def load_images():
    # TODO implement alternate piece image options
    pieces = ['wP', 'wN', 'wB', 'wR', 'wQ', 'wK', 'bP', 'bN', 'bB', 'bR', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/standard/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))


def main():
    p.init()
    p.display.set_caption('Pygame Chess 2')
    screen = p.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    load_images()
    clock = p.time.Clock()
    gs = gamestate.GameState()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        draw_game_state(gs, screen)

        p.display.flip()
        clock.tick(MAX_FPS)


def draw_game_state(gs, screen):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            square = gs.board[row][col]
            draw_square(screen, square, light_square_color, dark_square_color)


def draw_square(screen, square, light_square_color, dark_square_color):
    color = light_square_color if square.color == "light" else dark_square_color
    p.draw.rect(screen, color, p.Rect(square.x, square.y, SQ_SIZE, SQ_SIZE))
    if square.piece != 0:
        screen.blit(IMAGES[str(square.piece)], p.Rect(square.x, square.y, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()
