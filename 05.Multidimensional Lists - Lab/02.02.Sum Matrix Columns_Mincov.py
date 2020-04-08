def read_matrix():
    rows_count, columns_count = map(int, input().split(","))
    return [list(map(int, input().split(" "))) for _ in range(rows_count)]


def sums_columns_matrix(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    sum_columns = [0] * columns_count
    for row in range(rows_count):
        for col in range(columns_count):
            sum_columns[col] += matrix[row][col]
    return sum_columns


def print_result(sums):
    [print(element) for element in sums]


matrix = read_matrix()
sum_columns = sums_columns_matrix(matrix)
print_result(sum_columns)
