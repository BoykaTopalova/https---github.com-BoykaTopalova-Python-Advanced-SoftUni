def explode_bomb(b):
    rw, cl = b
    global size
    global matrix
    bomb_exp = matrix[rw][cl]
    if bomb_exp > 0:

        for n in range(-1, 2):
            for m in range(-1, 2):
                if 0 <= rw - n < size and 0 <= cl - m < size and 0 <= rw < size and 0 <= cl < size:
                    if matrix[rw - n][cl - m] > 0:
                        matrix[rw - n][cl - m] -= bomb_exp
        # matrix[rw][cl] = 0


size = int(input())

matrix = []
for _ in range(size):
    rows = [int(x) for x in input().split()]
    matrix.append(rows)

bombs = []
coordinates_bomb = input().split()
for item in coordinates_bomb:
    bomb_row, bomb_col = (map(int, item.split(",")))
    bombs.append((bomb_row, bomb_col))
[explode_bomb(bomb) for bomb in bombs]

counter = 0
sums = 0
for r in range(size):
    for c in range(size):
        if matrix[r][c] > 0:
            counter += 1
            sums += matrix[r][c]
print(f"Alive cells: {counter}")
print(f"Sum: {sums}")
for item_row in matrix:
    print(" ".join(str(el) for el in item_row))
