rows_count, columns_count = [int(x) for x in input().split(' ')]
matrix = []
tmp1 = 0
tmp2 = 0

for row in range(rows_count):
    matrix.append([num for num in input().split()])

while True:
    command = input()
    if command == "END":
        break
    com = command.split()

    if len(com) == 5:
        (instruct, row1, col1, row2, col2) = com
        row1 = int(row1)
        row2 = int(row2)
        col1 = int(col1)
        col2 = int(col2)

        check = row1 == row2 and col1 == col2
        check1 = 0 <= row1 < rows_count and 0 <= row2 < rows_count \
                 and 0 <= col1 < columns_count and 0 <= col2 < columns_count
        if instruct == "swap" and not check and check1:
            tmp1 = matrix[row1][col1]
            tmp2 = matrix[row2][col2]
            matrix[row1][col1] = tmp2
            matrix[row2][col2] = tmp1
            for row in matrix:
                print(*row)

        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
