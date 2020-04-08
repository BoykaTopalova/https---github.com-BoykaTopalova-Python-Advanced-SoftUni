n = int(input())
matrix = []
for row in range(n):
    row = list(input().split())
    matrix.append(row)
command = input()
directions_g = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
collected = []
g_collected = []
while command != "Sunset":
    com = command.split(" ")
    if com[0] == "Collect":
        r = int(com[1])
        c = int(com[2])
        if 0 <= r < n and 0 <= c < len(matrix[r]):
            if matrix[r][c] in "MNC":
                collected.append(matrix[r][c])
                matrix[r][c] = "-"
    elif com[0] == "Steal":
        row_g = int(com[1])
        col_g = int(com[2])
        direction = com[3]
        if 0 <= row_g < n and 0 <= col_g < len(matrix[row_g]):
            if matrix[row_g][col_g] in "MNC":
                g_collected.append(matrix[row_g][col_g])
                matrix[row_g][col_g] = '-'
                for i in range(1, 4):
                    directions_g = {'up': [-i, 0], 'down': [i, 0], 'left': [0, -i], 'right': [0, i]}
                    change_directions = directions_g[direction]
                    next_pos = [change_directions[0] + row_g, change_directions[1] + col_g]
                    next_row = next_pos[0]
                    next_col = next_pos[1]
                    if 0 <= next_row <= n and 0 <= next_col < len(matrix[next_row]):
                        if matrix[next_row][next_col] in "NMC":
                            g_collected.append(matrix[next_row][next_col])
                            matrix[next_row][next_col] = "-"
    command = input()
[print(*row) for row in matrix]
if len(collected) != 0:
    print(f"Collected seashells: {len(collected)} -> {', '.join(collected)}")
else:
    print(f"Collected seashells: {len(collected)}")

print(f"Stolen seashells: {len(g_collected)}")
