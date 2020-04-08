def read_matrix():
    rows_count, columns_count = map(int, input().split(", "))
    return [list(map(int, input().split(","))) for _ in range(rows_count)]


def sums_matrix(matrix):
    sums_m = 0
    rows_count = len(matrix)
    for row in range(rows_count):
        sums_m += sum(matrix[row])
    return sums_m


matrix = read_matrix()
print(sums_matrix(matrix))
print(matrix)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0