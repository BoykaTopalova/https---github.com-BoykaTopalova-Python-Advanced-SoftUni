def get_input(n):
    matrix = []
    first_player_pos = []
    black_hole_pos = []

    for i in range(n):
        line = input()
        matrix.append([x for x in line])
        if 'S' in line:
            first_player_pos = [i, line.index('S')]
        if 'O' in line:
            black_hole_pos.append([i, line.index('O')])

    return matrix, first_player_pos, black_hole_pos


n = int(input())

matrix, first_player_pos, black_hole_pos = get_input(n)
sums = 0

flag = False
while True:
    command = input()
    next_position = []
    if command == "up":
        next_position = [first_player_pos[0] - 1, first_player_pos[1]]
    elif command == "down":
        next_position = [first_player_pos[0] + 1, first_player_pos[1]]
    elif command == "right":
        next_position = [first_player_pos[0], first_player_pos[1] + 1]
    elif command == "left":
        next_position = [first_player_pos[0], first_player_pos[1] - 1]
    if 0 <= next_position[0] < len(matrix) and 0 <= next_position[1] < len(matrix):
        r = next_position[0]
        c = next_position[1]
        if matrix[r][c].isdigit():
            sums += int(matrix[r][c])
            matrix[first_player_pos[0]][first_player_pos[1]] = "-"
            matrix[r][c] = "S"
            first_player_pos = next_position
            if sums >= 50:
                flag = True
                break
        elif matrix[r][c] == "-":
            matrix[first_player_pos[0]][first_player_pos[1]] = "-"
            matrix[r][c] = "S"
            first_player_pos = next_position
        elif matrix[r][c] == "O":
            matrix[first_player_pos[0]][first_player_pos[1]] = "-"
            matrix[r][c] = "-"
            matrix[black_hole_pos[1][0]][black_hole_pos[1][1]] = "S"
            r = black_hole_pos[1][0]
            c = black_hole_pos[1][1]
            next_position = (r, c)
            first_player_pos = next_position
    else:
        matrix[first_player_pos[0]][first_player_pos[1]] = "-"
        print("Bad news, the spaceship went to the void.")
        break
if flag:
    print("Good news! Stephen succeeded in collecting enough star power!")

print(f"Star power collected: {sums}")
[print(''.join(row)) for row in matrix]
