energy = int(input())
n = int(input())
matrix = []
paris_pos = []
for i in range(n):
    row = list(input())
    matrix.append(row)
    if "P" in row:
        paris_pos = [i, row.index('P')]

directions_paris = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
while True:
    command = input().split()
    directions = command[0]
    change_direction = directions_paris[directions]
    enemy_row = int(command[1])
    enemy_col = int(command[2])
    matrix[enemy_row][enemy_col] = "S"
    next_row = paris_pos[0] + change_direction[0]
    next_col = paris_pos[1] + change_direction[1]
    next_pos = [next_row, next_col]
    energy -= 1
    if 0 <= next_row < n and 0 <= next_col < n:
        if matrix[next_row][next_col] == "-":
            matrix[paris_pos[0]][paris_pos[1]] = "-"
            matrix[next_row][next_col] = "P"
            paris_pos = next_pos
        elif matrix[next_row][next_col] == "S":
            energy -= 2
            matrix[paris_pos[0]][paris_pos[1]] = "-"
            matrix[next_row][next_col] = "P"
            paris_pos = next_pos
        elif matrix[next_row][next_col] == "H":
            matrix[next_row][next_col] = "-"
            matrix[paris_pos[0]][paris_pos[1]] = "-"
            print(f"Paris has successfully abducted Helen! Energy left: {energy}")
            break
    if energy <= 0:
        print(f"Paris died at {paris_pos[0]};{paris_pos[1]}.")
        matrix[paris_pos[0]][paris_pos[1]] = "X"
        break

[print(''.join(row)) for row in matrix]
