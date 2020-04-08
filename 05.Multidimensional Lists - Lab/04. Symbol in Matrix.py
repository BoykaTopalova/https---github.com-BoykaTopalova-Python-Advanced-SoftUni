size = int(input())
matrix = [[None] * size for row in range(0, size)]
# creating empty matrix with zero

flag = False
for x in range(0, size):
    line = [x for x in input()]
    for y in range(0, size):
        matrix[x][y] = line[y]
search = input()
for i in range(size):
    for j in range(size):
        if search == matrix[i][j]:
            flag = True
            print(f"({i}, {j})")
            exit(0)

if not flag:
    print(f"{search} does not occur in the matrix")
