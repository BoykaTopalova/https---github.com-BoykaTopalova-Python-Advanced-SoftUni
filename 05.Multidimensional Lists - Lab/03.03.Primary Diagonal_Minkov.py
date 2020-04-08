def read_matrix(delimiter):
    size = int(input())
    return [list(map(int, input().split(delimiter))) for _ in range(size)]


def first_diagonal(matrix):
    size = len(matrix)
    sum_first = 0
    for i in range(size):
        sum_first += matrix[i][i]
    return sum_first


def second_diagonal(matrix):
    size = len(matrix)
    sum_second = 0
    for i in range(size):
        for j in range(size):
            if i + j == size-1:
                sum_second += matrix[i][j]
    return sum_second


matrix = read_matrix(" ")
print(first_diagonal(matrix))
print(second_diagonal(matrix))
