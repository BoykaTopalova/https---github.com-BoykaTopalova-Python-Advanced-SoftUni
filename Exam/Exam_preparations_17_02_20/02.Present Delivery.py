count_present = int(input())
n = int(input())
matrix = []
santa_pos = []
nice_kids = 0
for i in range(n):
    line = list(input().split())
    matrix.append(line)
    if 'S' in line:
        santa_pos = [i, line.index('S')]
    if 'V' in line:
        nice_kids += line.count('V')
way = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
nice_kids_present = 0
while True:
    command = input()
    if command == "Christmas morning":
        break
    change_way = way[command]
    next_row = santa_pos[0] + change_way[0]
    next_col = santa_pos[1] + change_way[1]
    next_pos = [next_row, next_col]
    if 0 <= next_row < n and 0 <= next_col < n:
        if matrix[next_row][next_col] == "-":
            matrix[santa_pos[0]][santa_pos[1]] = "-"
            matrix[next_row][next_col] = "S"
            santa_pos = next_pos
        elif matrix[next_row][next_col] == "V":
            count_present -= 1
            nice_kids_present += 1
            matrix[santa_pos[0]][santa_pos[1]] = "-"
            matrix[next_row][next_col] = "S"
            santa_pos = next_pos
            if count_present == 0:
                break
        elif matrix[next_row][next_col] == "X":
            matrix[santa_pos[0]][santa_pos[1]] = "-"
            matrix[next_row][next_col] = "S"
            santa_pos = next_pos
        elif matrix[next_row][next_col] == "C":
            matrix[santa_pos[0]][santa_pos[1]] = "-"
            matrix[next_row][next_col] = "S"
            santa_pos = next_pos
            ways = ('left', 'right', 'up', 'down')
            for it in ways:
                change_direction = way[it]
                present_row = santa_pos[0] + change_direction[0]
                present_col = santa_pos[1] + change_direction[1]
                present_pos = [present_row, present_col]
                if 0 <= present_row < n and 0 <= present_col < n:
                    if matrix[present_row][present_col] == "V" or matrix[present_row][present_col] == "X":
                        count_present -= 1
                        if matrix[present_row][present_col] == "V":
                            nice_kids_present += 1
                        matrix[present_row][present_col] = "-"
                        if count_present == 0:
                            break
    if count_present == 0:
        break

if count_present == 0 and nice_kids - nice_kids_present != 0:
    print("Santa ran out of presents!")
[print(' '.join(row)) for row in matrix]
if nice_kids == nice_kids_present:
    print(f"Good job, Santa! {nice_kids_present} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_present} nice kid/s.")
