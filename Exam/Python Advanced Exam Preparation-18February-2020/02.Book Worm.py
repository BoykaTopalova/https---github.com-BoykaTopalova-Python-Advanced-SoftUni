def read_matrix(size):
    m = []
    for _ in range(size):
        rows = [x for x in input()]
        m.append(rows)
    return m


def find_position_player(matrix):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "P":
                return row, col


def move_player(com, pos):
    global position
    r = pos[0]
    c = pos[1]
    command = {
        'up': (r - 1, c),
        'down': (r + 1, c),
        'left': (r, c - 1),
        'right': (r, c + 1)
    }
    next_row = command[com][0]
    next_col = command[com][1]
    if next_row not in range(size) or next_col not in range(size):
        if text:
            text.pop()
        return
    if matrix[next_row][next_col] != "-":
        text.append(matrix[next_row][next_col])
    matrix[r][c] = "-"
    matrix[next_row][next_col] = "P"
    position = command[com]


text = list(input())
size = int(input())
matrix = read_matrix(size)
num_command = int(input())
position = find_position_player(matrix)
eat_alpha = ""

for i in range(num_command):
    command = input()
    move_player(command, position)

print(f"{''.join(text)}")
for row in matrix:
    print(f"{''.join(row)}")
