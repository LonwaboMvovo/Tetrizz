"""Tetris(with rizz) using pygame"""
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
    for y in range(22):
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

            screen.fill(tetromino_colour, pygame.Rect((x * 30 + 325, (y-2) * 30 + 70), (30, 30)))
    return


def display_ghost(pg, bp):
    while True:
        allowed_move, bp, pg = can_move(pg, bp)

        if not allowed_move:
            break
    
    for y, x in bp[:-1]:
        if pg[y][x][1]  == "E":
            pg[y][x][0] = 3
            pg[y][x][1] = "G"

    for y in range(2, 22):
        for x in range(10):
            current_tetronimo = pg[y][x][1]

            if current_tetronimo == "G":
                tetromino_colour = "grey"

                screen.fill(tetromino_colour, pygame.Rect((x * 30 + 325, (y-2) * 30 + 70), (30, 30)))
            

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
            break

    return playfield_grid, lines_cleared


def end_game():
    print("GAME OVER!!!")
    print("\nThanks for playing... o.O")
    pygame.quit()
    exit()


def play_game():
    # Make new empty field, "E" meaning empty and will be replaced by piece colour later
    playfield_grid = [[[0, "E"] for _ in range(10)] for _ in range(22)]

    # Get a new bag of 7 random pieces
    seven_bag = get_seven_bag() + get_seven_bag()
    # Get current piece shape
    chosen_tetromino = seven_bag.pop(0)
    # Get starting position of current tetromino
    block_pos = get_tetromino_coords(chosen_tetromino)

    # Add piece spawn to board
    for y, x in block_pos[:-1]:
        playfield_grid[y][x][0] = 1
        playfield_grid[y][x][1] = chosen_tetromino

    # Used too see if should get a new piece from bag
    new_iteration = False

    swapped_held_piece = False
    held_piece = ""

    # Game loop
    while True:
        # Check player inputs/events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
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
                    
                    for y in range(2, 22):
                        for x in range(10):
                            current_tetronimo = playfield_grid[y][x][1]

                            if current_tetronimo == "G":
                                playfield_grid[y][x][0] = 0
                                playfield_grid[y][x][1] = "E"
                elif event.key == pygame.K_RIGHT:
                    for y, x in block_pos[:-1]:
                        playfield_grid[y][x][0] = 0
                        playfield_grid[y][x][1] = "E"

                    allowed_move, block_pos, playfield_grid = can_move(playfield_grid, block_pos, "R")

                    for i in range(4):
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][0] = 2
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][1] = chosen_tetromino

                    for y in range(2, 22):
                        for x in range(10):
                            current_tetronimo = playfield_grid[y][x][1]

                            if current_tetronimo == "G":
                                playfield_grid[y][x][0] = 0
                                playfield_grid[y][x][1] = "E"
                if event.key == pygame.K_UP:
                    for y, x in block_pos[:-1]:
                        playfield_grid[y][x][0] = 0
                        playfield_grid[y][x][1] = "E"
        
                    allowed_move, block_pos, playfield_grid = can_rotate(playfield_grid, block_pos, chosen_tetromino)
                    
                    for i in range(4):
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][0] = 2
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][1] = chosen_tetromino
                    
                    for y in range(2, 22):
                        for x in range(10):
                            current_tetronimo = playfield_grid[y][x][1]

                            if current_tetronimo == "G":
                                playfield_grid[y][x][0] = 0
                                playfield_grid[y][x][1] = "E"
                elif event.key == pygame.K_s or event.key == pygame.K_z:
                    for y, x in block_pos[:-1]:
                        playfield_grid[y][x][0] = 0
                        playfield_grid[y][x][1] = "E"
        
                    allowed_move, block_pos, playfield_grid = can_rotate(playfield_grid, block_pos, chosen_tetromino, "AC")
                    
                    for i in range(4):
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][0] = 2
                        playfield_grid[block_pos[i][0]][block_pos[i][1]][1] = chosen_tetromino

                    for y in range(2, 22):
                        for x in range(10):
                            current_tetronimo = playfield_grid[y][x][1]

                            if current_tetronimo == "G":
                                playfield_grid[y][x][0] = 0
                                playfield_grid[y][x][1] = "E"
                elif event.key == pygame.K_DOWN:
                    for y, x in block_pos[:-1]:
                        playfield_grid[y][x][0] = 0
                        playfield_grid[y][x][1] = "E"

                    allowed_move, block_pos, playfield_grid = can_move(playfield_grid, block_pos)

                    for y, x in block_pos[:-1]:
                        playfield_grid[y][x][0] = 2
                        playfield_grid[y][x][1] = chosen_tetromino
                elif event.key == pygame.K_f or event.key == pygame.K_c:
                    if not swapped_held_piece:
                        for y, x in block_pos[:-1]:
                            playfield_grid[y][x][0] = 0
                            playfield_grid[y][x][1] = "E" 

                        if held_piece == "":
                            held_piece = chosen_tetromino
                            chosen_tetromino = seven_bag.pop(0)
                            block_pos = get_tetromino_coords(chosen_tetromino)
                        else:
                            old_held_piece = held_piece
                            held_piece = chosen_tetromino
                            chosen_tetromino = old_held_piece
                            block_pos = get_tetromino_coords(chosen_tetromino)

                        swapped_held_piece = True

                        for y in range(2, 22):
                            for x in range(10):
                                current_tetronimo = playfield_grid[y][x][1]

                                if current_tetronimo == "G":
                                    playfield_grid[y][x][0] = 0
                                    playfield_grid[y][x][1] = "E"
                
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
            swapped_held_piece = False

            # Set current tetromino to be part of board
            for y in range(2, 22):
                for x in range(10):
                    if playfield_grid[y][x][0] == 2:
                        playfield_grid[y][x][0] = 1

            playfield_grid, lines_cleared = check_lines_cleared(playfield_grid)

            while lines_cleared > 0:
                playfield_grid, lines_cleared = check_lines_cleared(playfield_grid)

            # If bag is empty get a new bag of 7 random pieces
            if len(seven_bag) <= 6:
                seven_bag += get_seven_bag()
            chosen_tetromino = seven_bag.pop(0)
            block_pos = get_tetromino_coords(chosen_tetromino)

            for y, x in block_pos[:-1]:
                playfield_grid[y][x][0] = 1
                playfield_grid[y][x][1] = chosen_tetromino

            new_iteration = False

        display_grid(playfield_grid)
        display_ghost(playfield_grid, block_pos)
        
        # Draw board outline
        for x in range(325, 330+325, 30):
            pygame.draw.line(screen, "black", (x, 70), (x, 670), width = 1)

        for y in range(70, 800, 30):
            pygame.draw.line(screen, "black", (0+325, y), (300+325, y), width = 1)

        # Drow hold piece area
        screen.fill((42,43,46), pygame.Rect((150, 70), (150, 120), border_radius = 10))
        pygame.draw.rect(screen, "black", (150, 70, 150, 120), width = 1, border_radius = 10)
        hold_text = pixel_type_font.render(f"Hold", False, "grey")
        hold_text_rect = hold_text.get_rect(midtop = (225, 80))
        screen.blit(hold_text, hold_text_rect)

        if held_piece == "O":
            screen.fill((180,154,51), pygame.Rect((195, 120), (30, 30)))
            screen.fill((180,154,51), pygame.Rect((225, 120), (30, 30)))
            screen.fill((180,154,51), pygame.Rect((225, 150), (30, 30)))
            screen.fill((180,154,51), pygame.Rect((195, 150), (30, 30)))
            pygame.draw.rect(screen, "black", (195, 120, 60, 60), width = 1)
            pygame.draw.line(screen, "black", (225, 120), (225, 180), width = 1)
            pygame.draw.line(screen, "black", (195, 150), (255, 150), width = 1)
        elif held_piece == "I":
            screen.fill((50,180,132), pygame.Rect((165, 130), (30, 30)))
            screen.fill((50,180,132), pygame.Rect((195, 130), (30, 30)))
            screen.fill((50,180,132), pygame.Rect((225, 130), (30, 30)))
            screen.fill((50,180,132), pygame.Rect((255, 130), (30, 30)))
            pygame.draw.rect(screen, "black", (165, 130, 120, 30), width = 1)
            pygame.draw.line(screen, "black", (195, 130), (195, 160), width = 1)
            pygame.draw.line(screen, "black", (225, 130), (225, 160), width = 1)
            pygame.draw.line(screen, "black", (255, 130), (255, 160), width = 1)
        elif held_piece == "S":
            screen.fill((130,178,49), pygame.Rect((195, 120), (30, 30)))
            screen.fill((130,178,49), pygame.Rect((225, 120), (30, 30)))
            screen.fill((130,178,49), pygame.Rect((195, 150), (30, 30)))
            screen.fill((130,178,49), pygame.Rect((165, 150), (30, 30)))
            pygame.draw.rect(screen, "black", (195, 120, 30, 60), width = 1)
            pygame.draw.line(screen, "black", (165, 150), (225, 150), width = 1)
            pygame.draw.line(screen, "black", (165, 150), (165, 180), width = 1)
            pygame.draw.line(screen, "black", (165, 180), (195, 180), width = 1)
            pygame.draw.line(screen, "black", (225, 150), (255, 150), width = 1)
            pygame.draw.line(screen, "black", (225, 120), (255, 120), width = 1)
            pygame.draw.line(screen, "black", (255, 120), (255, 150), width = 1)
        elif held_piece == "Z":
            screen.fill((182,53,60), pygame.Rect((225, 120), (30, 30)))
            screen.fill((182,53,60), pygame.Rect((195, 120), (30, 30)))
            screen.fill((182,53,60), pygame.Rect((255, 150), (30, 30)))
            screen.fill((182,53,60), pygame.Rect((225, 150), (30, 30)))
            pygame.draw.rect(screen, "black", (225, 120, 30, 60), width = 1)
            pygame.draw.line(screen, "black", (195, 150), (285, 150), width = 1)
            pygame.draw.line(screen, "black", (285, 150), (285, 180), width = 1)
            pygame.draw.line(screen, "black", (255, 180), (255, 180), width = 1)
            pygame.draw.line(screen, "black", (195, 150), (225, 150), width = 1)
            pygame.draw.line(screen, "black", (195, 120), (225, 120), width = 1)
            pygame.draw.line(screen, "black", (195, 120), (195, 150), width = 1)
        elif held_piece == "L":
            screen.fill((181,100,51), pygame.Rect((165, 150), (30, 30)))
            screen.fill((181,100,51), pygame.Rect((225, 120), (30, 30)))
            screen.fill((181,100,51), pygame.Rect((225, 150), (30, 30)))
            screen.fill((181,100,51), pygame.Rect((195, 150), (30, 30)))
            pygame.draw.rect(screen, "black", (225, 120, 30, 60), width = 1)
            pygame.draw.line(screen, "black", (165, 150), (165, 180), width = 1)
            pygame.draw.line(screen, "black", (195, 150), (195, 180), width = 1)
            pygame.draw.line(screen, "black", (165, 150), (255, 150), width = 1)
            pygame.draw.line(screen, "black", (165, 180), (225, 180), width = 1)
        elif held_piece == "J":
            screen.fill((81,64,167), pygame.Rect((195, 120), (30, 30)))
            screen.fill((81,64,167), pygame.Rect((255, 150), (30, 30)))
            screen.fill((81,64,167), pygame.Rect((225, 150), (30, 30)))
            screen.fill((81,64,167), pygame.Rect((195, 150), (30, 30)))
            pygame.draw.rect(screen, "black", (195, 120, 30, 60), width = 1)
            pygame.draw.line(screen, "black", (255, 150), (255, 180), width = 1)
            pygame.draw.line(screen, "black", (285, 150), (285, 180), width = 1)
            pygame.draw.line(screen, "black", (195, 150), (285, 150), width = 1)
            pygame.draw.line(screen, "black", (225, 180), (285, 180), width = 1)
        elif held_piece == "T":
            screen.fill((207,60,193), pygame.Rect((225, 120), (30, 30)))
            screen.fill((207,60,193), pygame.Rect((255, 150), (30, 30)))
            screen.fill((207,60,193), pygame.Rect((225, 150), (30, 30)))
            screen.fill((207,60,193), pygame.Rect((195, 150), (30, 30)))
            pygame.draw.rect(screen, "black", (195, 150, 90, 30), width = 1)
            pygame.draw.line(screen, "black", (255, 120), (255, 180), width = 1)
            pygame.draw.line(screen, "black", (225, 120), (225, 180), width = 1)
            pygame.draw.line(screen, "black", (225, 120), (255, 120), width = 1)

        # Show next piece
        screen.fill((42,43,46), pygame.Rect((650, 70), (150, 120), border_radius = 10))
        pygame.draw.rect(screen, "black", (650, 70, 150, 120), width = 1, border_radius = 10)
        next_text = pixel_type_font.render(f"Next", False, "grey")
        next_text_rect = next_text.get_rect(midtop = (725, 80))
        screen.blit(next_text, next_text_rect)

        next_piece = seven_bag[0]

        if next_piece == "O":
            screen.fill((180,154,51), pygame.Rect((695, 120), (30, 30)))
            screen.fill((180,154,51), pygame.Rect((725, 120), (30, 30)))
            screen.fill((180,154,51), pygame.Rect((725, 150), (30, 30)))
            screen.fill((180,154,51), pygame.Rect((695, 150), (30, 30)))
            pygame.draw.rect(screen, "black", (695, 120, 60, 60), width = 1)
            pygame.draw.line(screen, "black", (725, 120), (725, 180), width = 1)
            pygame.draw.line(screen, "black", (695, 150), (755, 150), width = 1)
        elif next_piece == "I":
            screen.fill((50,180,132), pygame.Rect((665, 130), (30, 30)))
            screen.fill((50,180,132), pygame.Rect((695, 130), (30, 30)))
            screen.fill((50,180,132), pygame.Rect((725, 130), (30, 30)))
            screen.fill((50,180,132), pygame.Rect((755, 130), (30, 30)))
            pygame.draw.rect(screen, "black", (665, 130, 120, 30), width = 1)
            pygame.draw.line(screen, "black", (695, 130), (695, 160), width = 1)
            pygame.draw.line(screen, "black", (725, 130), (725, 160), width = 1)
            pygame.draw.line(screen, "black", (755, 130), (755, 160), width = 1)
        elif next_piece == "S":
            screen.fill((130,178,49), pygame.Rect((695, 120), (30, 30)))
            screen.fill((130,178,49), pygame.Rect((725, 120), (30, 30)))
            screen.fill((130,178,49), pygame.Rect((695, 150), (30, 30)))
            screen.fill((130,178,49), pygame.Rect((665, 150), (30, 30)))
            pygame.draw.rect(screen, "black", (695, 120, 30, 60), width = 1)
            pygame.draw.line(screen, "black", (665, 150), (725, 150), width = 1)
            pygame.draw.line(screen, "black", (665, 150), (665, 180), width = 1)
            pygame.draw.line(screen, "black", (665, 180), (695, 180), width = 1)
            pygame.draw.line(screen, "black", (725, 150), (755, 150), width = 1)
            pygame.draw.line(screen, "black", (725, 120), (755, 120), width = 1)
            pygame.draw.line(screen, "black", (755, 120), (755, 150), width = 1)
        elif next_piece == "Z":
            screen.fill((182,53,60), pygame.Rect((725, 120), (30, 30)))
            screen.fill((182,53,60), pygame.Rect((695, 120), (30, 30)))
            screen.fill((182,53,60), pygame.Rect((755, 150), (30, 30)))
            screen.fill((182,53,60), pygame.Rect((725, 150), (30, 30)))
            pygame.draw.rect(screen, "black", (725, 120, 30, 60), width = 1)
            pygame.draw.line(screen, "black", (695, 150), (785, 150), width = 1)
            pygame.draw.line(screen, "black", (785, 150), (785, 180), width = 1)
            pygame.draw.line(screen, "black", (755, 180), (755, 180), width = 1)
            pygame.draw.line(screen, "black", (695, 150), (725, 150), width = 1)
            pygame.draw.line(screen, "black", (695, 120), (725, 120), width = 1)
            pygame.draw.line(screen, "black", (695, 120), (695, 150), width = 1)
        elif next_piece == "L":
            screen.fill((181,100,51), pygame.Rect((665, 150), (30, 30)))
            screen.fill((181,100,51), pygame.Rect((725, 120), (30, 30)))
            screen.fill((181,100,51), pygame.Rect((725, 150), (30, 30)))
            screen.fill((181,100,51), pygame.Rect((695, 150), (30, 30)))
            pygame.draw.rect(screen, "black", (725, 120, 30, 60), width = 1)
            pygame.draw.line(screen, "black", (665, 150), (665, 180), width = 1)
            pygame.draw.line(screen, "black", (695, 150), (695, 180), width = 1)
            pygame.draw.line(screen, "black", (665, 150), (755, 150), width = 1)
            pygame.draw.line(screen, "black", (665, 180), (725, 180), width = 1)
        elif next_piece == "J":
            screen.fill((81,64,167), pygame.Rect((695, 120), (30, 30)))
            screen.fill((81,64,167), pygame.Rect((755, 150), (30, 30)))
            screen.fill((81,64,167), pygame.Rect((725, 150), (30, 30)))
            screen.fill((81,64,167), pygame.Rect((695, 150), (30, 30)))
            pygame.draw.rect(screen, "black", (695, 120, 30, 60), width = 1)
            pygame.draw.line(screen, "black", (755, 150), (755, 180), width = 1)
            pygame.draw.line(screen, "black", (785, 150), (785, 180), width = 1)
            pygame.draw.line(screen, "black", (695, 150), (785, 150), width = 1)
            pygame.draw.line(screen, "black", (725, 180), (785, 180), width = 1)
        elif next_piece == "T":
            screen.fill((207,60,193), pygame.Rect((725, 120), (30, 30)))
            screen.fill((207,60,193), pygame.Rect((755, 150), (30, 30)))
            screen.fill((207,60,193), pygame.Rect((725, 150), (30, 30)))
            screen.fill((207,60,193), pygame.Rect((695, 150), (30, 30)))
            pygame.draw.rect(screen, "black", (695, 150, 90, 30), width = 1)
            pygame.draw.line(screen, "black", (755, 120), (755, 180), width = 1)
            pygame.draw.line(screen, "black", (725, 120), (725, 180), width = 1)
            pygame.draw.line(screen, "black", (725, 120), (755, 120), width = 1)

        # Update screen/display
        pygame.display.update()
        # max set to 60 frames/sec
        clock.tick(60)


if __name__ != "__main__":
    input("""\nWelcome to Tetrizz! It's basically tetris (but with rizz)

    Controls:
    left arrow - move tetromino left
    right arrow - move tetromino right
    up arrow - rotate tetromino clockwise
    down arrow - soft drop
    spacebar - hard drop
    s/z - rotate tetromino clockwise
    f/c - swap/hold tetromino
    esc/q - quit game
            
    press any key to continue...
    """)

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
    screen = pygame.display.set_mode((1000, 700))
    screen_bg_colour = (42,43,46)
    screen.fill(screen_bg_colour)

    # Timers:
    tetromino_drop_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(tetromino_drop_timer, 500)

    # Audio:
    pygame.mixer.music.load('audio/Tetrizz soundtrack-1.wav')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    pixel_type_font = pygame.font.Font("font/Pixeltype.ttf", 50)
    play_game()
