"""Tetris clone in terminal"""
import time
import os
import random
import keyboard

from termcolor import colored

# TODO have one can move function which takes a direction parameter as well
def can_move_down(playfield_grid, block_pos):
    new_block_pos = move_down(block_pos)

    if any(playfield_grid[y][x][0] == 1 for y, x in new_block_pos):
        return False, block_pos, playfield_grid

    return True, new_block_pos, playfield_grid


def move_down(block_pos):
    new_block_pos = list()

    for i in range(4):
        new_block_pos.append([block_pos[i][0]+1, block_pos[i][1]])

    return new_block_pos


def can_move_right(playfield_grid, block_pos):
    new_block_pos = move_right(block_pos)

    if any(x > 9  for y, x in new_block_pos) or any(playfield_grid[y][x][0] == 1 for y, x in new_block_pos):
        return False, block_pos, playfield_grid

    return True, new_block_pos, playfield_grid


def move_right(block_pos):
    new_block_pos = list()

    for i in range(4):
        new_block_pos.append([block_pos[i][0], block_pos[i][1]+1])

    return new_block_pos


def can_move_left(playfield_grid, block_pos):
    new_block_pos = move_left(block_pos)

    if any(x < 0  for y, x in new_block_pos) or any(playfield_grid[y][x][0] == 1 for y, x in new_block_pos):
        return False, block_pos, playfield_grid

    return True, new_block_pos, playfield_grid


def move_left(block_pos):
    new_block_pos = list()

    for i in range(4):
        new_block_pos.append([block_pos[i][0], block_pos[i][1]-1])

    return new_block_pos


def display_grid(playfield_grid):
    playfield_output = f"\n{' ---' * 10}"

    for y in range(2, 22):
        playfield_output += "\n|"

        for x in range(10):
            current_tetronimo = playfield_grid[y][x][1]

            tetromino_colour = "white"
            
            if current_tetronimo == "I":
                tetromino_colour = "cyan"
            elif current_tetronimo == "S":
                tetromino_colour = "green"
            elif current_tetronimo == "Z":
                tetromino_colour = "red"
            elif current_tetronimo == "L":
                tetromino_colour = "yellow"
            elif current_tetronimo == "J":
                tetromino_colour = "blue"
            elif current_tetronimo == "T":
                tetromino_colour = "magenta"

            the_block = colored("■", tetromino_colour)

            play_field_block = f" {the_block} |" if playfield_grid[y][x][1] != "E" else f"   |"
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
    playfield_grid = [[[0, "E"] for _ in range(10)] for _ in range(22)]
    seven_bag = get_seven_bag()

    piece_iteration = 1

    playing = True

    while playing:
        
        if len(seven_bag) == 0:
            seven_bag = get_seven_bag()

        chosen_tetromino = seven_bag.pop(0)

        block_pos = get_tetromino_coords(chosen_tetromino)

        for frame in range(20):
            for pos in block_pos:
                playfield_grid[pos[0]][pos[1]][0] = 2
                playfield_grid[pos[0]][pos[1]][1] = chosen_tetromino

            current_time = time.time()
            frame_time = 0.1
            end_time = current_time + frame_time

            while current_time < end_time:
                os.system('clear' if os.name == 'posix' else 'cls')
                print(piece_iteration, chosen_tetromino, frame)
                display_grid(playfield_grid)
                
                if keyboard.is_pressed("left"):
                    for pos in block_pos:
                        playfield_grid[pos[0]][pos[1]][0] = 2
                        playfield_grid[pos[0]][pos[1]][1] = chosen_tetromino

                    for y, x in block_pos:
                        playfield_grid[y][x][0] = 0
                        playfield_grid[y][x][1] = "E"

                    allowed_bot, block_pos, playfield_grid = can_move_left(playfield_grid, block_pos)

                    for i in range(4):
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][0] = 1
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][1] = chosen_tetromino
                
                elif keyboard.is_pressed("right"):
                    for pos in block_pos:
                        playfield_grid[pos[0]][pos[1]][0] = 2
                        playfield_grid[pos[0]][pos[1]][1] = chosen_tetromino

                    for y, x in block_pos:
                        playfield_grid[y][x][0] = 0
                        playfield_grid[y][x][1] = "E"

                    allowed_bot, block_pos, playfield_grid = can_move_right(playfield_grid, block_pos)

                    for i in range(4):
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][0] = 1
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][1] = chosen_tetromino
            
                current_time = time.time()

            for y, x in block_pos:
                playfield_grid[y][x][0] = 0
                playfield_grid[y][x][1] = "E"

            allowed_bot, block_pos, playfield_grid = can_move_down(playfield_grid, block_pos)

            for i in range(4):
                playfield_grid[block_pos[i][0]][block_pos[i][1]][0] = 1
                playfield_grid[block_pos[i][0]][block_pos[i][1]][1] = chosen_tetromino

            if not allowed_bot:
                if block_pos == get_tetromino_coords(chosen_tetromino):
                    playing = False
                break

        piece_iteration += 1

    print("GAME OVER!!!")


if __name__ == "__main__":
    play_game()
