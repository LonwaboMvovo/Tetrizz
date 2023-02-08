playfield_grid = [[0 for _ in range(10)] for _ in range(22)]

playfield_output = f"""\n{' ---' * 10}"""
for y in range(20):
    playfield_output += "\n|"

    for x in range(10):
        play_field_block = " ■ |" if playfield_grid[y][x] == 1 else "   |"
        playfield_output += play_field_block
playfield_output += f"\n{' ---' * 10}\n"

print(playfield_output)
