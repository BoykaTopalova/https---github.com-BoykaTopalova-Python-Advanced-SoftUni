from collections import deque

row_count, col_count = [int(x) for x in input().split()]
text = deque(input())
matrix = []

for row in range(row_count):
    matrix.append(["" for _ in range(col_count)])

for row in range(row_count):
    if row % 2 == 0:
        for col in range(col_count):
            el = text.popleft()
            matrix[row][col] = el
            text.append(el)
    else:
        for col in range(col_count - 1, -1, -1):
            el = text.popleft()
            matrix[row][col] = el
            text.append(el)

for row in range(row_count):
    print(''.join(matrix[row]))
