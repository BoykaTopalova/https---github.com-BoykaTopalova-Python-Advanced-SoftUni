def read_matrix():
    n = int(input())
    return [input() for _ in range(n)]


def find_symbol(m, symbol):
    size = len(m)
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == symbol:
                return (i, j)
    return None


matrix = read_matrix()
search_symbol = input()
result = find_symbol(matrix, search_symbol)
if not result:
    print(f"{search_symbol} does not occur in the matrix")
else:
    print(result)
