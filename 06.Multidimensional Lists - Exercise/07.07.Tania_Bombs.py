def is_valid(m, row, col):
    size = len(m)
    result = 0 <= row < size and 0 <= col < size and m[row][col] > 0
    return result


def explode(matrix, row, col):
    bomb_value = matrix[row][col]
    if bomb_value > 0:
        for current_row in range(-1, 2):
            for current_col in range(-1, 2):
                neighbor_row = row + current_row
                neighbor_col = col + current_col
                if current_row == 0 and current_col == 0:
                    continue
                if is_valid(matrix, neighbor_row, neighbor_col):
                    matrix[neighbor_row][neighbor_col] -= bomb_value
        matrix[row][col] = 0


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
bombs = [[int(y) for y in x.split(",")] for x in input().split()]

for bomb in bombs:
    row = bomb[0]
    col = bomb[1]
    explode(matrix, row, col)

alive_cells = [x for row in matrix for x in row if x > 0]
count_alive_cells = len(alive_cells)
sum_alive_cells = sum(alive_cells)

print(f"Alive cells: {count_alive_cells}")
print(f"Sum: {sum_alive_cells}")
[print(*row) for row in matrix]