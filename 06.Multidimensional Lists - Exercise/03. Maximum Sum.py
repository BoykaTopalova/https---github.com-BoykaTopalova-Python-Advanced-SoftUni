rows_count, columns_count = [int(x) for x in input().split(' ')]
matrix = []
for row in range(rows_count):
    matrix.append([int(num) for num in input().split()])

best_sum = 0
best_row = 0
best_col = 0
for row in range(rows_count - 2):
    for col in range(columns_count - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] +\
                      matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] +\
                      matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

        if current_sum > best_sum:
            best_sum = current_sum
            best_col = col
            best_row = row

print(f"Sum = {best_sum}")
for row in range(best_row, best_row + 3):
    for col in range(best_col, best_col + 3):
        print(matrix[row][col], end=" ")
    print()
