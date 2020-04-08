def get_input(n):
    matrix = []
    paris_pos = []

    for i in range(n):
        line = input()
        matrix.append([x for x in line])
        if 'P' in line:
            paris_pos = [i, line.index('P')]

    return matrix, paris_pos


energy = int(input())
n = int(input())
matrix, paris_pos = get_input(n)
while True:
    command_all = input().split(" ")
    spartans_pos = []
    command = command_all[0]
    spartans_pos = [int(command_all[1]), int(command_all[2])]
    rs = spartans_pos[0]
    cs = spartans_pos[1]
    matrix[rs][cs] = "S"

    next_position = []
    if command == "up":
        next_position = [paris_pos[0] - 1, paris_pos[1]]
    elif command == "down":
        next_position = [paris_pos[0] + 1, paris_pos[1]]
    elif command == "right":
        next_position = [paris_pos[0], paris_pos[1] + 1]
    elif command == "left":
        next_position = [paris_pos[0], paris_pos[1] - 1]

    if 0 <= next_position[0] < len(matrix) and 0 <= next_position[1] < len(matrix):
        r = next_position[0]
        c = next_position[1]
        if matrix[r][c] == "-":
            matrix[paris_pos[0]][paris_pos[1]] = "-"
            matrix[r][c] = "P"
            energy -= 1
            if energy <= 0:
                matrix[r][c] = "X"
                print(f"Paris died at {r};{c}.")
                break
            paris_pos = next_position
        elif matrix[r][c] == "S":
            energy -= 1
            matrix[paris_pos[0]][paris_pos[1]] = "-"
            matrix[r][c] = "P"
            energy -= 2
            if energy <= 0:
                matrix[r][c] = "X"
                print(f"Paris died at {r};{c}.")
                break
            paris_pos = next_position
        elif matrix[r][c] == "H":
            matrix[paris_pos[0]][paris_pos[1]] = "-"
            matrix[r][c] = "-"
            energy -= 1
            print(f"Paris has successfully abducted Helen! Energy left: {energy}")
            break
    else:
        energy -= 1
[print(''.join(row)) for row in matrix]
