playfield_grid = [["0" for _ in range(10)] for _ in range(22)]

for row in playfield_grid[2:]:
    print("".join(row))


playfield_output = f"""{' ---' * len(playfield_grid[0])}"""
for i in range(len(playfield_grid)):
    playfield_output += "\n"
    playfield_output += "|" + "   |" * len(playfield_grid[0])
    playfield_output += "\n"
    playfield_output += " ---" * len(playfield_grid[0])

print(playfield_output)