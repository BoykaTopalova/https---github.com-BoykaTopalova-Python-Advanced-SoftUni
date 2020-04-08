size_matrix = [int(x) for x in input().split(", ")]

rows, cols = size_matrix

matrix = [0 for x in range(rows)]

sum_matrix = 0
sum_lines = 0

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    sum_matrix += sum(lines)
    matrix[row] = lines

print(sum_matrix)
print(matrix)
