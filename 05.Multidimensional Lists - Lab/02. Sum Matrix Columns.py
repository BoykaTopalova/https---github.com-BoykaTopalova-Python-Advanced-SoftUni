size_matrix = [int(x) for x in input().split(", ")]
rows, cols = size_matrix
matrix = [0 for x in range(rows)]

sum_lines = 0
for row in range(rows):
    lines = [int(x) for x in input().split(" ")]
    matrix[row] = lines

sums = [0]*cols
for col in range(cols):
    for row in range(rows):
        sums[col] += matrix[row][col]
    print(sums[col])
