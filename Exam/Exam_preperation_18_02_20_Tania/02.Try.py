text = input()
n = int(input())
matrix = []
player_pos = []
for row in range(n):
    line = list(input())
    matrix.append(line)
    if "P" in line:
        player_pos = [row, line.index("P")]
m = int(input())
way = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
for i in range(m):
    command = input()
    change_way = way[command]
    next_row = change_way[0] + player_pos[0]
    next_col = change_way[1] + player_pos[1]
    next_pos = [next_row, next_col]
    if 0 <= next_row < n and 0 <= next_col < n:
        if matrix[next_row][next_col] == "-":
            matrix[player_pos[0]][player_pos[1]] = "-"
            matrix[next_row][next_col] = "P"
            player_pos = next_pos
        else:
            text += matrix[next_row][next_col]
            matrix[player_pos[0]][player_pos[1]] = "-"
            matrix[next_row][next_col] = "P"
            player_pos = next_pos
    else:
        if text:
            text = text[:-1]
print(text)
[print(''.join(row)) for row in matrix]
