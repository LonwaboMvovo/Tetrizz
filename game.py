import pygame
from random import choice
from sys import exit


def get_seven_bag():
    tetrominos = ["O", "I", "S", "Z", "L", "J", "T"]
    
    seven_bag = []

    for _ in range(7):
        chosen_piece = choice(tetrominos)
        seven_bag.append(chosen_piece)
        tetrominos.remove(chosen_piece)

    return seven_bag


def get_tetromino_coords(chosen_tetromino):
    block_start_pos = list()

    if chosen_tetromino == "O":
        block_start_pos = [[1, 4], [0, 4], [0, 5], [1, 5]]
    elif chosen_tetromino == "I":
        block_start_pos = [[1, 3], [1, 4], [1, 5], [1, 6]]
    elif chosen_tetromino == "S":
        block_start_pos = [[1, 3], [1, 4], [0, 4], [0, 5]]
    elif chosen_tetromino == "Z":
        block_start_pos = [[0, 3], [0, 4], [1, 4], [1, 5]]
    elif chosen_tetromino == "L":
        block_start_pos = [[1, 3], [1, 4], [1, 5], [0, 5]]
    elif chosen_tetromino == "J":
        block_start_pos = [[0, 3], [1, 3], [1, 4], [1, 5]]
    elif chosen_tetromino == "T":
        block_start_pos = [[1,3], [1, 4], [0, 4], [1, 5]]

    return block_start_pos


def play_game():
    # Make new empty field, "E" meaning empty and will be replaced by piece colour later
    playfield_grid = [[[0, "E"] for _ in range(10)] for _ in range(22)]

    # Get a new bag of 7 random pieces
    seven_bag = get_seven_bag()

    # Game loop
    while True:
        # Check player inputs/events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # If bag is empty get a new bag of 7 random pieces
        if len(seven_bag) == 0:
            seven_bag = get_seven_bag()

        # Get current piece shape
        chosen_tetromino = seven_bag.pop(0)

        # Get starting position of current tetromino
        block_pos = get_tetromino_coords(chosen_tetromino)

        
        # Update screen/display
        pygame.display.update()


# inits bruv
pygame.init()
screen = pygame.display.set_mode((350, 700))
screen_bg_colour = (42,43,46)
screen.fill(screen_bg_colour)

# Draw board outline
for x in range(35, 400, 35):
    pygame.draw.line(screen, "black", (x, 0), (x, 700), width = 1)

for y in range(35, 800, 35):
    pygame.draw.line(screen, "black", (0, y), (400, y), width = 1)

# Set window icon
icon_surface = pygame.Surface((32, 32))
icon_surface.fill((139,0,139))
pygame.display.set_icon(icon_surface)

# Set Window title
pygame.display.set_caption("Tetrizz")

if __name__ == "__main__":
    play_game()