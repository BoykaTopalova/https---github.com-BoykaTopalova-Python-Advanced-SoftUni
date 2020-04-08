text = input()
n = int(input())

field = []
player_position = []

dirs = {'up': [-1, 0], 'down': [1, 0],'left': [0, -1], 'right': [0, 1]}

for row in range(n):
    line = list(input())
    field.append(line)
    if "P" in line:
        player_position = [row, line.index("P")]

commands_count = int(input())
for _ in range(commands_count):
    command = input()
    direction_change = dirs[command]
    next_row = player_position[0] + direction_change[0]
    next_col = player_position[1] + direction_change[1]
    next_pos = [next_row, next_col]
    # validate indices
    if 0 <= next_row < n and 0 <= next_col < n:
        if field[next_row][next_col] == "-":
            field[player_position[0]][player_position[1]] = "-"
            field[next_row][next_col] = "P"
            player_position = next_pos
        else:
            field[player_position[0]][player_position[1]] = "-"
            text += field[next_row][next_col]
            field[next_row][next_col] = "P"
            player_position = next_pos
    else:
        text = text[:-1]
print(text)
[print(''.join(row)) for row in field]
