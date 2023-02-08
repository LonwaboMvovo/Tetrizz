"""Tetris clone in terminal"""
import time
import os
import random

from rich import print


def display_grid(playfield_grid, chosen_tetromino):
    grid_colour = "grey53"
    tetromino_colour = "bright_yellow"

    if chosen_tetromino == "I":
        tetromino_colour = "bright_cyan"
    elif chosen_tetromino == "S":
        tetromino_colour = "green"
    elif chosen_tetromino == "Z":
        tetromino_colour = "bright_red"
    elif chosen_tetromino == "L":
        tetromino_colour = "orange3"
    elif chosen_tetromino == "J":
        tetromino_colour = "bright_blue"
    elif chosen_tetromino == "T":
        tetromino_colour = "bright_magenta"

    playfield_output = f"\n[{grid_colour}]{' ---' * 10}"

    for y in range(2, 22):
        playfield_output += "\n|"

        for x in range(10):
            play_field_block = f" [{tetromino_colour}]■[{grid_colour}] |" if playfield_grid[y][x] == 1 else f"   |"
            playfield_output += play_field_block

    playfield_output += f"\n{' ---' * 10}\n"

    print(playfield_output)


def get_seven_bag():
    tetrominos = ["O", "I", "S", "Z", "L", "J", "T"]
    
    seven_bag = []

    for _ in range(7):
        chosen_piece = random.choice(tetrominos)
        seven_bag.append(chosen_piece)
        tetrominos.remove(chosen_piece)

    return seven_bag

def drop_row(block_pos):
    new_block_pos = list()

    for i in range(4):
        new_block_pos.append([block_pos[i][0]+1, block_pos[i][1]])

    return new_block_pos


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
    legacy_grid = [[0 for _ in range(10)] for _ in range(22)]

    seven_bag = get_seven_bag()

    piece_iteration = 1

    while True:
        playfield_grid = legacy_grid.copy()
        os.system('clear' if os.name == 'posix' else 'cls')
        
        if len(seven_bag) == 0:
            seven_bag = get_seven_bag()

        chosen_tetromino = seven_bag.pop(0)

        block_pos = get_tetromino_coords(chosen_tetromino)

        for frame in range(21):
            for pos in block_pos:
                playfield_grid[pos[0]][pos[1]] = 1



            block_pos = drop_row(block_pos)

            print(piece_iteration, chosen_tetromino, frame)
            display_grid(playfield_grid, chosen_tetromino)

            time.sleep(0.1)
            os.system('clear' if os.name == 'posix' else 'cls')

            if frame < 20:
                playfield_grid = [[0 for _ in range(10)] for _ in range(22)]


        legacy_grid = playfield_grid.copy()

        piece_iteration += 1


if __name__ == "__main__":
    play_game()
