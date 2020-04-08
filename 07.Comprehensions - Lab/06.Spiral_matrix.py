def in_range(r, num):
    if 0 <= r < num:
        return True
    return False


n = int(input())

rows_dirs = [0, +1, 0, -1]
col_dirs = [+1, 0, -1, 0]
matrix = [[None] * n for _ in range(n)]
row = 0
col = 0
dir = 0

for count in range(n * n):
    matrix[row][col] = count + 1
    next_row = row + rows_dirs[dir]
    next_col = col + col_dirs[dir]
    if not in_range(next_row, n) \
            or not in_range(next_col, n) \
            or matrix[next_row][next_col]:
        dir += 1
        dir %= 4

    row += rows_dirs[dir]
    col += col_dirs[dir]
[print(row) for row in matrix]
