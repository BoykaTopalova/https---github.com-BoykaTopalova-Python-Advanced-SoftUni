n = int(input())
matrix = []
player_position = []

target_count = 0
count = 0
for row in range(n):
    line = list(input().split())
    matrix.append(line)
    if "p" in line:
        player_position = [row, line.index("p")]
    if "t" in line:
        target_count += line.count("t")

m = int(input())
for _ in range(m):
    command = input().split(" ")
    com = command[0]
    if com == "move":
        way = command[1]
        steps = int(command[2])
        dirs = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
        change_way = dirs[way]
        next_row = change_way[0] * steps + player_position[0]
        next_col = change_way[1] * steps + player_position[1]
        next_pos = [next_row, next_col]
        if 0 <= next_col < n and 0 <= next_row < n:
            if matrix[next_row][next_col] == ".":
                matrix[player_position[0]][player_position[1]] = "."
                matrix[next_row][next_col] = "p"
                player_position = next_pos
    elif com == "shoot":
        shot_dir = command[1]
        steps_p = int(command[2])
        dirs = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
        change_way = dirs[shot_dir]
        next_row_p = change_way[0] * steps_p + player_position[0]
        next_col_p = change_way[1] * steps_p + player_position[1]
        next_pos_p = [next_row_p, next_col_p]
        if 0 <= next_row_p < n and 0 <= next_col_p < n:
            if matrix[next_row_p][next_col_p] == "t":
                matrix[next_row_p][next_col_p] = "x"
                count += 1
                if count == target_count:
                    break
            elif matrix[next_row_p][next_col_p] == ".":
                matrix[next_row_p][next_col_p] = "x"
if target_count - count == 0:
    print(f"Mission accomplished! All {count} targets destroyed.")
else:
    print(f"Mission failed! {target_count - count} targets left.")

[print(' '.join(row)) for row in matrix]
