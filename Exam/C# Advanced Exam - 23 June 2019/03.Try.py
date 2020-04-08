def read_spaceship(n):
    count = 0
    matrix = []
    player_pos = []
    blacks_holes = []
    for row in range(n):
        line = list(input())
        matrix.append(line)
        if "S" in line:
            player_pos = [row, line.index("S")]
        if "O" in line:
            blacks_holes.append([row, line.index("O")])

    return matrix, player_pos, blacks_holes


num = int(input())
matrix, player_pos, blacks_holes = read_spaceship(num)

dirs = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
sums = 0
flag = False
while True:
    command = input()
    direction_change = dirs[command]
    next_row = player_pos[0] + direction_change[0]
    next_col = player_pos[1] + direction_change[1]
    next_pos = [next_row, next_col]
    if 0 <= next_row < num and 0 <= next_col < num:
        if matrix[next_row][next_col].isdigit():
            sums += int(matrix[next_row][next_col])
            matrix[player_pos[0]][player_pos[1]] = "-"
            matrix[next_row][next_col] = "S"
            player_pos = next_pos
            if sums >= 50:
                flag = True
                break
        elif matrix[next_row][next_col] == "-":
            matrix[player_pos[0]][player_pos[1]] = "-"
            matrix[next_row][next_col] = "S"
            player_pos = next_pos
        elif matrix[next_row][next_col] == "O":
            matrix[player_pos[0]][player_pos[1]] = "-"
            matrix[next_row][next_col] = "-"
            matrix[blacks_holes[1][0]][blacks_holes[1][1]] = "S"
            next_pos = [blacks_holes[1][0], blacks_holes[1][1]]
            player_pos = next_pos
    else:
        matrix[player_pos[0]][player_pos[1]] = "-"
        print("Bad news, the spaceship went to the void.")
        break

if flag:
    print("Good news! Stephen succeeded in collecting enough star power!")
print(f"Star power collected: {sums}")
[print(''.join(row)) for row in matrix]
