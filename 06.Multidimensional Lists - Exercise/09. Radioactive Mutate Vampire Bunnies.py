def input_matrix(row, col):
    mat = []
    for i in range(row):
        rows = [x for x in input()]
        mat.append(rows)
    return mat


def find_start(mat, r, c):
    for i in range(r):
        for j in range(c):
            if mat[i][j] == "P":
                return i, j


def is_valid(coordinates):
    r, c = coordinates
    if r in range(n) and c in range(m):
        return True
    return False


def reproduction():
    bunnies = []
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == "B":
                bunnies.append((r, c))

    for bunny in bunnies:

        r, c = bunny
        up = (r - 1, c)
        down = (r + 1, c)
        left = (r, c - 1)
        right = (r, c + 1)
        directions = [up, down, left, right]
        for direction in directions:
            if is_valid(direction):
                if matrix[direction[0]][direction[1]] == "P":
                    matrix[direction[0]][direction[1]] = "B"
                    print(matrix[direction[0]][direction[1]])
                    print(f"dead: {direction[0]} {direction[1]}")
                    exit()
                matrix[direction[0]][direction[1]] = "B"


def move_bunnies(direction, coordinates):
    r, c = coordinates
    directions = {"U": (r - 1, c), "D": (r + 1, c), "L": (r, c - 1), "R": (r, c + 1)}

    if is_valid(directions[direction]) and \
            matrix[directions[direction][0]][directions[direction][1]] != "B":
        matrix[r][c] = "."
        return directions[direction]
    elif is_valid(directions[direction]) and \
            matrix[directions[direction][0]][directions[direction][1]] == "B":
        matrix[r][c] = "."
        reproduction()
        print_matrix()
        print(f"dead: {directions[direction][0]} {directions[direction][1]}")

        exit()
    elif not is_valid(directions[direction]):
        matrix[r][c] = "."
        reproduction()
        print_matrix()
        print(f"won: {r} {c}")
        exit()


def move_player(com):
    for command in com:
        global start

        if move_bunnies(command, start):
            matrix[start[0]][start[1]] = "."
            next_move = move_bunnies(command, start)
            start = next_move
            matrix[start[0]][start[1]] = "P"
            reproduction()


def print_matrix():
    for row in matrix:
        print(f'{"".join(x for x in row)}')


n, m = map(int, input().split())
matrix = input_matrix(n, m)
commands = input()
start = find_start(matrix, n, m)
move_player(commands)
