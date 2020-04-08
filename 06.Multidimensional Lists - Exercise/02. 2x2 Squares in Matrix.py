(row_count, col_count) = [int(x) for x in input().split()]
matrix = []
count = 0

for x in range(0, row_count):
    matrix.append(input().split())

for x in range(0, row_count - 1):
    for y in range(0, col_count - 1):
        if matrix[x][y] == matrix[x][y + 1] == matrix[x + 1][y] == matrix[x + 1][y + 1]:
            count += 1

print(count)
