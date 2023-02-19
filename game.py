"""Tetris (with rizz)"""
import pygame
from random import choice
from sys import exit


def can_move(playfield_grid, block_pos, direction="D"):
    if direction == "L":
        new_block_pos = move_left(block_pos)
    elif direction == "R":
        new_block_pos = move_right(block_pos)
    elif direction == "D":
        new_block_pos = move_down(block_pos)

    if (any(x > 9  for y, x in new_block_pos[:-1]) or
            any(x < 0  for y, x in new_block_pos[:-1]) or
            any(y > 21 or playfield_grid[y][x][0] == 1 for y, x in new_block_pos[:-1])):
        return False, block_pos, playfield_grid

    return True, new_block_pos, playfield_grid


def move_down(block_pos):
    new_block_pos = block_pos.copy()

    for i in range(4):
        new_block_pos[i] = [block_pos[i][0]+1, block_pos[i][1]]

    return new_block_pos


def move_right(block_pos):
    new_block_pos = block_pos.copy()

    for i in range(4):
        new_block_pos[i] = [block_pos[i][0], block_pos[i][1]+1]

    return new_block_pos


def move_left(block_pos):
    new_block_pos = block_pos.copy()

    for i in range(4):
        new_block_pos[i] = [block_pos[i][0], block_pos[i][1]-1]

    return new_block_pos


def can_rotate(playfield_grid, block_pos, current_tetronimo, direction="C"):
    if direction == "AC":
        new_block_pos = rotate_anti_clockwise(block_pos, current_tetronimo)
    elif direction == "C":
        new_block_pos = rotate_clockwise(block_pos, current_tetronimo)

    if (any(x > 9  for y, x in new_block_pos[:-1]) or
            any(x < 0  for y, x in new_block_pos[:-1]) or
            any(y > 21 or playfield_grid[y][x][0] == 1 for y, x in new_block_pos[:-1])):
        return False, block_pos, playfield_grid

    return True, new_block_pos, playfield_grid


def rotate_clockwise(block_pos, current_tetronimo):
    new_block_pos = block_pos.copy()

    if block_pos[-1] == "up":
        if current_tetronimo == "I":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]+2]
            new_block_pos[1] = [new_block_pos[1][0], new_block_pos[1][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]]
            new_block_pos[3] = [new_block_pos[3][0]+2, new_block_pos[3][1]-1]
            new_block_pos[4] = "right"
        elif current_tetronimo == "J":
            new_block_pos[0] = [new_block_pos[0][0], new_block_pos[0][1]+2]
            new_block_pos[1] = [new_block_pos[1][0]-1, new_block_pos[1][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]-1]
            new_block_pos[4] = "right"
        elif current_tetronimo == "L":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]+2, new_block_pos[3][1]]
            new_block_pos[4] = "right"
        elif current_tetronimo == "S":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+2, new_block_pos[3][1]]
            new_block_pos[4] = "right"
        elif current_tetronimo == "T":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]-1]
            new_block_pos[4] = "right"
        elif current_tetronimo == "Z":
            new_block_pos[0] = [new_block_pos[0][0], new_block_pos[0][1]+2]
            new_block_pos[1] = [new_block_pos[1][0]+1, new_block_pos[1][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]-1]
            new_block_pos[4] = "right"
    elif block_pos[-1] == "right":
        if current_tetronimo == "I":
            new_block_pos[0] = [new_block_pos[0][0]+2, new_block_pos[0][1]+1]
            new_block_pos[1] = [new_block_pos[1][0]+1, new_block_pos[1][1]]
            new_block_pos[2] = [new_block_pos[2][0], new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]-2]
            new_block_pos[4] = "down"
        elif current_tetronimo == "J":
            new_block_pos[0] = [new_block_pos[0][0]+2, new_block_pos[0][1]]
            new_block_pos[1] = [new_block_pos[1][0]+1, new_block_pos[1][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]-1]
            new_block_pos[4] = "down"
        elif current_tetronimo == "L":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0], new_block_pos[3][1]-2]
            new_block_pos[4] = "down"
        elif current_tetronimo == "S":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0], new_block_pos[3][1]-2]
            new_block_pos[4] = "down"
        elif current_tetronimo == "T":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]-1]
            new_block_pos[4] = "down"
        elif current_tetronimo == "Z":
            new_block_pos[0] = [new_block_pos[0][0]+2, new_block_pos[0][1]]
            new_block_pos[1] = [new_block_pos[1][0]+1, new_block_pos[1][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]-1]
            new_block_pos[4] = "down"
    elif block_pos[-1] == "down":
        if current_tetronimo == "I":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]-2]
            new_block_pos[1] = [new_block_pos[1][0], new_block_pos[1][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]]
            new_block_pos[3] = [new_block_pos[3][0]-2, new_block_pos[3][1]+1]
            new_block_pos[4] = "left"
        elif current_tetronimo == "J":
            new_block_pos[0] = [new_block_pos[0][0], new_block_pos[0][1]-2]
            new_block_pos[1] = [new_block_pos[1][0]+1, new_block_pos[1][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]+1]
            new_block_pos[4] = "left"
        elif current_tetronimo == "L":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]-2, new_block_pos[3][1]]
            new_block_pos[4] = "left"
        elif current_tetronimo == "S":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-2, new_block_pos[3][1]]
            new_block_pos[4] = "left"
        elif current_tetronimo == "T":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]+1]
            new_block_pos[4] = "left"
        elif current_tetronimo == "Z":
            new_block_pos[0] = [new_block_pos[0][0], new_block_pos[0][1]-2]
            new_block_pos[1] = [new_block_pos[1][0]-1, new_block_pos[1][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]+1]
            new_block_pos[4] = "left"
    elif block_pos[-1] == "left":
        if current_tetronimo == "I":
            new_block_pos[0] = [new_block_pos[0][0]-2, new_block_pos[0][1]-1]
            new_block_pos[1] = [new_block_pos[1][0]-1, new_block_pos[1][1]]
            new_block_pos[2] = [new_block_pos[2][0], new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]+2]
            new_block_pos[4] = "up"
        elif current_tetronimo == "J":
            new_block_pos[0] = [new_block_pos[0][0]-2, new_block_pos[0][1]]
            new_block_pos[1] = [new_block_pos[1][0]-1, new_block_pos[1][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]+1]
            new_block_pos[4] = "up"
        elif current_tetronimo == "L":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0], new_block_pos[3][1]+2]
            new_block_pos[4] = "up"
        elif current_tetronimo == "S":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0], new_block_pos[3][1]+2]
            new_block_pos[4] = "up"
        elif current_tetronimo == "T":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]+1]
            new_block_pos[4] = "up"
        elif current_tetronimo == "Z":
            new_block_pos[0] = [new_block_pos[0][0]-2, new_block_pos[0][1]]
            new_block_pos[1] = [new_block_pos[1][0]-1, new_block_pos[1][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]+1]
            new_block_pos[4] = "up"

    return new_block_pos


def rotate_anti_clockwise(block_pos, current_tetronimo):
    new_block_pos = block_pos.copy()

    if block_pos[-1] == "up":
        if current_tetronimo == "I":
            new_block_pos[0] = [new_block_pos[0][0]+2, new_block_pos[0][1]+1]
            new_block_pos[1] = [new_block_pos[1][0]+1, new_block_pos[1][1]]
            new_block_pos[2] = [new_block_pos[2][0], new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]-2]
            new_block_pos[4] = "left"
        elif current_tetronimo == "J":
            new_block_pos[0] = [new_block_pos[0][0]+2, new_block_pos[0][1]]
            new_block_pos[1] = [new_block_pos[1][0]+1, new_block_pos[1][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]-1]
            new_block_pos[4] = "left"
        elif current_tetronimo == "L":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0], new_block_pos[3][1]-2]
            new_block_pos[4] = "left"
        elif current_tetronimo == "S":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0], new_block_pos[3][1]-2]
            new_block_pos[4] = "left"
        elif current_tetronimo == "T":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]-1]
            new_block_pos[4] = "left"
        elif current_tetronimo == "Z":
            new_block_pos[0] = [new_block_pos[0][0]+2, new_block_pos[0][1]]
            new_block_pos[1] = [new_block_pos[1][0]+1, new_block_pos[1][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]-1]
            new_block_pos[4] = "left"
    elif block_pos[-1] == "left":
        if current_tetronimo == "I":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]+2]
            new_block_pos[1] = [new_block_pos[1][0], new_block_pos[1][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]]
            new_block_pos[3] = [new_block_pos[3][0]+2, new_block_pos[3][1]-1]
            new_block_pos[4] = "down"
        elif current_tetronimo == "J":
            new_block_pos[0] = [new_block_pos[0][0], new_block_pos[0][1]+2]
            new_block_pos[1] = [new_block_pos[1][0]-1, new_block_pos[1][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]-1]
            new_block_pos[4] = "down"
        elif current_tetronimo == "L":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]+2, new_block_pos[3][1]]
            new_block_pos[4] = "down"
        elif current_tetronimo == "S":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+2, new_block_pos[3][1]]
            new_block_pos[4] = "down"
        elif current_tetronimo == "T":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]+1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]-1]
            new_block_pos[4] = "down"
        elif current_tetronimo == "Z":
            new_block_pos[0] = [new_block_pos[0][0], new_block_pos[0][1]+2]
            new_block_pos[1] = [new_block_pos[1][0]+1, new_block_pos[1][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]-1]
            new_block_pos[4] = "down"
    elif block_pos[-1] == "down":
        if current_tetronimo == "I":
            new_block_pos[0] = [new_block_pos[0][0]-2, new_block_pos[0][1]-1]
            new_block_pos[1] = [new_block_pos[1][0]-1, new_block_pos[1][1]]
            new_block_pos[2] = [new_block_pos[2][0], new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]+2]
            new_block_pos[4] = "right"
        elif current_tetronimo == "J":
            new_block_pos[0] = [new_block_pos[0][0]-2, new_block_pos[0][1]]
            new_block_pos[1] = [new_block_pos[1][0]-1, new_block_pos[1][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]+1]
            new_block_pos[4] = "right"
        elif current_tetronimo == "L":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]+1, new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0], new_block_pos[3][1]+2]
            new_block_pos[4] = "right"
        elif current_tetronimo == "S":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0], new_block_pos[3][1]+2]
            new_block_pos[4] = "right"
        elif current_tetronimo == "T":
            new_block_pos[0] = [new_block_pos[0][0]-1, new_block_pos[0][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]+1]
            new_block_pos[4] = "right"
        elif current_tetronimo == "Z":
            new_block_pos[0] = [new_block_pos[0][0]-2, new_block_pos[0][1]]
            new_block_pos[1] = [new_block_pos[1][0]-1, new_block_pos[1][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]+1, new_block_pos[3][1]+1]
            new_block_pos[4] = "right"
    elif block_pos[-1] == "right":
        if current_tetronimo == "I":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]-2]
            new_block_pos[1] = [new_block_pos[1][0], new_block_pos[1][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]]
            new_block_pos[3] = [new_block_pos[3][0]-2, new_block_pos[3][1]+1]
            new_block_pos[4] = "up"
        elif current_tetronimo == "J":
            new_block_pos[0] = [new_block_pos[0][0], new_block_pos[0][1]-2]
            new_block_pos[1] = [new_block_pos[1][0]+1, new_block_pos[1][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]+1]
            new_block_pos[4] = "up"
        elif current_tetronimo == "L":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]+1]
            new_block_pos[3] = [new_block_pos[3][0]-2, new_block_pos[3][1]]
            new_block_pos[4] = "up"
        elif current_tetronimo == "S":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-2, new_block_pos[3][1]]
            new_block_pos[4] = "up"
        elif current_tetronimo == "T":
            new_block_pos[0] = [new_block_pos[0][0]+1, new_block_pos[0][1]-1]
            new_block_pos[2] = [new_block_pos[2][0]-1, new_block_pos[2][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]+1]
            new_block_pos[4] = "up"
        elif current_tetronimo == "Z":
            new_block_pos[0] = [new_block_pos[0][0], new_block_pos[0][1]-2]
            new_block_pos[1] = [new_block_pos[1][0]-1, new_block_pos[1][1]-1]
            new_block_pos[3] = [new_block_pos[3][0]-1, new_block_pos[3][1]+1]
            new_block_pos[4] = "up"

    return new_block_pos


def display_grid(playfield_grid):
    for y in range(2, 22):
        for x in range(10):
            current_tetronimo = playfield_grid[y][x][1]

            tetromino_colour = (42,43,46)

            if current_tetronimo == "O":
                tetromino_colour = (180,154,51)
            elif current_tetronimo == "I":
                tetromino_colour = (50,180,132)
            elif current_tetronimo == "S":
                tetromino_colour = (130,178,49)
            elif current_tetronimo == "Z":
                tetromino_colour = (182,53,60)
            elif current_tetronimo == "L":
                tetromino_colour = (181,100,51)
            elif current_tetronimo == "J":
                tetromino_colour = (81,64,167)
            elif current_tetronimo == "T":
                tetromino_colour = (207,60,193)

            screen.fill(tetromino_colour, pygame.Rect((x * 35, (y-2) * 35), (35, 35)))
    return


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
        block_start_pos = [[1, 4], [0, 4], [0, 5], [1, 5], "up"]
    elif chosen_tetromino == "I":
        block_start_pos = [[1, 3], [1, 4], [1, 5], [1, 6], "up"]
    elif chosen_tetromino == "S":
        block_start_pos = [[1, 3], [1, 4], [0, 4], [0, 5], "up"]
    elif chosen_tetromino == "Z":
        block_start_pos = [[0, 3], [0, 4], [1, 4], [1, 5], "up"]
    elif chosen_tetromino == "L":
        block_start_pos = [[1, 3], [1, 4], [1, 5], [0, 5], "up"]
    elif chosen_tetromino == "J":
        block_start_pos = [[0, 3], [1, 3], [1, 4], [1, 5], "up"]
    elif chosen_tetromino == "T":
        block_start_pos = [[1,3], [1, 4], [0, 4], [1, 5], "up"]

    return block_start_pos


def clear_lines(y, next_y, playfield_grid):
    for y in range(y, next_y):
        for x in range(0, 10):
            playfield_grid[y][x][0] = 0
            playfield_grid[y][x][1] = "E"

    for _ in range(y-next_y):
        playfield_grid.pop(y)
        playfield_grid = [[[0, "E"] for _ in range(10)]] + playfield_grid

    return playfield_grid


def check_lines_cleared(playfield_grid):
    for y in range(21, 1, -1):
        lines_cleared = 0
        next_y = y-1

        if all(col[0] for col in playfield_grid[y]):
            if not (next_y > 0 and all(col[0] for col in playfield_grid[next_y])):
                lines_cleared += 1

                print("SINGLE")
                playfield_grid = clear_lines(y, next_y, playfield_grid)
            else:
                next_y -=1
                lines_cleared += 1

                if not (next_y > 0 and all(col[0] for col in playfield_grid[next_y])):
                    print("DOUBLE")
                    playfield_grid = clear_lines(y, next_y, playfield_grid)
                else:
                    next_y -=1
                    lines_cleared += 1

                    if not (next_y > 0 and all(col[0] for col in playfield_grid[next_y])):
                        print("TRIPLE")
                        playfield_grid = clear_lines(y, next_y, playfield_grid)
                    else:
                        next_y -=1
                        lines_cleared += 1

                        if not (next_y > 0 and all(col[0] for col in playfield_grid[next_y])):
                            print("TETRIS")
                            playfield_grid = clear_lines(y, next_y, playfield_grid)

        if lines_cleared > 0:
            lines_cleared += 1
            print(lines_cleared)
            break

    return playfield_grid


def end_game():
    print("GAME OVER!!!")
    pygame.quit()
    exit()


def play_game():
    # Make new empty field, "E" meaning empty and will be replaced by piece colour later
    playfield_grid = [[[0, "E"] for _ in range(10)] for _ in range(22)]

    # Get a new bag of 7 random pieces
    seven_bag = get_seven_bag()
    # Get current piece shape
    chosen_tetromino = seven_bag.pop(0)
    # Get starting position of current tetromino
    block_pos = get_tetromino_coords(chosen_tetromino)

    # Used too see if should get a new piece from bag
    new_iteration = False

    # Game loop
    while True:
        # Check player inputs/events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                end_game()
            
            if event.type == tetromino_drop_timer:
                for y, x in block_pos[:-1]:
                    playfield_grid[y][x][0] = 0
                    playfield_grid[y][x][1] = "E"

                allowed_move, block_pos, playfield_grid = can_move(playfield_grid, block_pos)

                if not allowed_move:
                    if block_pos == get_tetromino_coords(chosen_tetromino):
                        end_game()

                    new_iteration = True

                for y, x in block_pos[:-1]:
                    playfield_grid[y][x][0] = 2
                    playfield_grid[y][x][1] = chosen_tetromino

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    for y, x in block_pos[:-1]:
                        playfield_grid[y][x][0] = 0
                        playfield_grid[y][x][1] = "E"

                    allowed_move, block_pos, playfield_grid = can_move(playfield_grid, block_pos, "L")

                    for i in range(4):
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][0] = 2
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][1] = chosen_tetromino
                elif event.key == pygame.K_RIGHT:
                    for y, x in block_pos[:-1]:
                        playfield_grid[y][x][0] = 0
                        playfield_grid[y][x][1] = "E"

                    allowed_move, block_pos, playfield_grid = can_move(playfield_grid, block_pos, "R")

                    for i in range(4):
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][0] = 2
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][1] = chosen_tetromino
                
                if event.key == pygame.K_UP:
                    for y, x in block_pos[:-1]:
                        playfield_grid[y][x][0] = 0
                        playfield_grid[y][x][1] = "E"
        
                    allowed_move, block_pos, playfield_grid = can_rotate(playfield_grid, block_pos, chosen_tetromino)
                    
                    for i in range(4):
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][0] = 2
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][1] = chosen_tetromino
                elif event.key == pygame.K_s:
                    for y, x in block_pos[:-1]:
                        playfield_grid[y][x][0] = 0
                        playfield_grid[y][x][1] = "E"
        
                    allowed_move, block_pos, playfield_grid = can_rotate(playfield_grid, block_pos, chosen_tetromino, "AC")
                    
                    for i in range(4):
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][0] = 2
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][1] = chosen_tetromino
                
                # TODO might not add soft drop
                # if event.key == pygame.K_DOWN:
                #     print("SOFT DROP - MOVE PIECE DOWN 1")
                
                if event.key == pygame.K_SPACE:
                    while True:
                        for y, x in block_pos[:-1]:
                            playfield_grid[y][x][0] = 0
                            playfield_grid[y][x][1] = "E"

                        allowed_move, block_pos, playfield_grid = can_move(playfield_grid, block_pos)

                        for y, x in block_pos[:-1]:
                            playfield_grid[y][x][0] = 2
                            playfield_grid[y][x][1] = chosen_tetromino

                        if not allowed_move:
                            break
                    
                    new_iteration = True

        if new_iteration:
            # Set current tetromino to be part of board
            for y in range(2, 22):
                for x in range(10):
                    if playfield_grid[y][x][0] == 2:
                        playfield_grid[y][x][0] = 1

            playfield_grid = check_lines_cleared(playfield_grid)

            # If bag is empty get a new bag of 7 random pieces
            if len(seven_bag) == 0:
                seven_bag = get_seven_bag()
            chosen_tetromino = seven_bag.pop(0)
            block_pos = get_tetromino_coords(chosen_tetromino)

            new_iteration = False
        
        display_grid(playfield_grid)

        # Draw board outline
        for x in range(35, 400, 35):
            pygame.draw.line(screen, "black", (x, 0), (x, 700), width = 1)

        for y in range(35, 800, 35):
            pygame.draw.line(screen, "black", (0, y), (400, y), width = 1)

        # Update screen/display
        pygame.display.update()
        # max set to 60 frames/sec
        clock.tick(60)
        

# inits bruv
pygame.init()
clock = pygame.time.Clock()

# Set Window title
pygame.display.set_caption("Tetrizz")

# Set window icon
icon_surface = pygame.Surface((32, 32))
icon_surface.fill((139,0,139))
pygame.display.set_icon(icon_surface)

# Set background
screen = pygame.display.set_mode((350, 700))
screen_bg_colour = (42,43,46)
screen.fill(screen_bg_colour)

# Timers:
tetromino_drop_timer = pygame.USEREVENT + 1
pygame.time.set_timer(tetromino_drop_timer, 500)


if __name__ == "__main__":
    play_game()

# TODO CLEAR BOARD WHEN GETS LINE IN A ROW
# TODO SHOW GHOST PIECE