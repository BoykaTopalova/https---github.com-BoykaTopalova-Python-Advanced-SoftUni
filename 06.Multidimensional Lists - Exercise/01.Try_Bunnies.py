n, m = [int(x) for x in input().split()]
matrix = []
player_pos = []
flag_won = False
flag_dead = False
for row in range(n):
    line = list(input())
    matrix.append(line)
    if "P" in line:
        player_pos = [row, line.index("P")]


def move_player(player_pos, next_pos, matrix):
    flag_won = False
    if 0 <= next_row < n and 0 <= next_col < m:
        if matrix[next_row][next_col] == ".":
            matrix[player_pos[0]][player_pos[1]] = "."
            matrix[next_row][next_col] = "P"
            player_pos = next_pos
        else:
            matrix[player_pos[0]][player_pos[1]] = "P"
    else:
        matrix[player_pos[0]][player_pos[1]] = "."
        flag_won = True
    return flag_won


def bunni_position(matrix):
    bunni_pos = []
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == "B":
                bunni_pos.append([r, c])
    return bunni_pos


def multi_bunni(matrix, bunni_pos):
    is_dead = False
    for (row, col) in bunni_pos:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i + j != 0 and i != j:
                    if 0 <= row + i < len(matrix) and 0 <= col + j < len(matrix[row]):
                        if matrix[row + i][col + j] == ".":
                            matrix[row + i][col + j] = "B"
                        elif matrix[row + i][col + j] == "P":
                            matrix[row + i][col + j] = "B"
                            is_dead = True
    return is_dead


ways = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
command = input()
for com in command:
    change_way = ways[com]
    next_row = change_way[0] + player_pos[0]
    next_col = change_way[1] + player_pos[1]
    next_pos = [next_row, next_col]

    flag_won = move_player(player_pos, next_pos, matrix)
    bunni_pos = bunni_position(matrix)
    flag_dead = multi_bunni(matrix, bunni_pos)

    if flag_won:
        [print(''.join(row)) for row in matrix]
        print(f"won: {player_pos[0]} {player_pos[1]}")
        break
    player_pos = next_pos
    if flag_dead:
        [print(''.join(row)) for row in matrix]
        print(f"dead: {player_pos[0]} {player_pos[1]}")
        break
