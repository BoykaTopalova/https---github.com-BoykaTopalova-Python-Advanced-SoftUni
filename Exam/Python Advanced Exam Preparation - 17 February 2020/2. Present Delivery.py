def read_matrix(n):
    m = []
    s_pos = []
    nice = 0
    for i in range(n):
        line = input().split(" ")
        m.append([x for x in line])
        if 'S' in line:
            s_pos = [i, line.index('S')]
        if 'V' in line:
            nice += line.count('V')
    return m, s_pos, nice


count_present = int(input())
size_area = int(input())
matrix, santa_position, nice = read_matrix(size_area)

good = 0
diff = 0

while True:
    command = input()
    if command == "Christmas morning":
        break

    next_position = []
    if command == "up":
        next_position = [santa_position[0] - 1, santa_position[1]]
    elif command == "down":
        next_position = [santa_position[0] + 1, santa_position[1]]
    elif command == "right":
        next_position = [santa_position[0], santa_position[1] + 1]
    elif command == "left":
        next_position = [santa_position[0], santa_position[1] - 1]

    if 0 <= next_position[0] < len(matrix) and 0 <= next_position[1] < len(matrix):
        r = next_position[0]
        c = next_position[1]
        if matrix[r][c] == "V":
            good += 1
            count_present -= 1
            matrix[santa_position[0]][santa_position[1]] = "-"
            matrix[r][c] = "S"
            santa_position = next_position
            if count_present == 0:
                break
        elif matrix[r][c] == "X":
            matrix[santa_position[0]][santa_position[1]] = "-"
            matrix[r][c] = "S"
            santa_position = next_position
        elif matrix[r][c] == "-":
            matrix[santa_position[0]][santa_position[1]] = "-"
            matrix[r][c] = "S"
            santa_position = next_position
        elif matrix[r][c] == "C":
            matrix[santa_position[0]][santa_position[1]] = "-"
            matrix[r][c] = "S"
            if matrix[r][c - 1] == "V" or matrix[r][c - 1] == "X":
                if count_present != 0:
                    if matrix[r][c - 1] == "V":
                        good += 1
                    count_present -= 1
                    matrix[r][c - 1] = "-"
                else:
                    break
            if matrix[r][c + 1] == "V" or matrix[r][c + 1] == "X":
                if count_present != 0:
                    if matrix[r][c + 1] == "V":
                        good += 1
                    count_present -= 1
                    matrix[r][c + 1] = "-"
                else:
                    break

            if matrix[r - 1][c] == "V" or matrix[r - 1][c] == "X":
                if count_present != 0:
                    if matrix[r - 1][c] == "V":
                        good += 1
                    count_present -= 1
                    matrix[r - 1][c] = "-"
                else:
                    break
            if matrix[r + 1][c] == "V" or matrix[r + 1][c] == "X":
                if count_present != 0:
                    if matrix[r + 1][c] == "V":
                        good += 1
                    count_present -= 1
                    matrix[r + 1][c] = "-"
                else:
                    break
    if count_present == 0:
        break
if count_present == 0 and nice - good != 0:
    print("Santa ran out of presents!")

[print(" ".join(line)) for line in matrix]

if nice == good:
    print(f"Good job, Santa! {nice} happy nice kid/s.")
else:
    print(f"No presents for {nice - good} nice kid/s.")
