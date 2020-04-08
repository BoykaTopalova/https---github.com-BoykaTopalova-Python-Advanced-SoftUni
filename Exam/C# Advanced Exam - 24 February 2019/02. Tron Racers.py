DIRECTIONS = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}


def move_player(matrix, player, dir):
    pos_change = DIRECTIONS[dir]
    next_pos = [player['pos'][0] + pos_change[0], player['pos'][1] + pos_change[1]]


def read_matrix():
    size = int(input())
    m = []
    for _ in range(size):
        rows = [x for x in input()]
        m.append(rows)
    return m


def find_position_player(matrix):
    size = len(matrix)
    position_f = []
    position_s = []
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "f":
                position_f = (row, col)
            if matrix[row][col] == "s":
                position_s = (row, col)

    return position_f, position_s


matrix = read_matrix()
position_f, position_s = find_position_player()
first_player = {"symbol": "f", "pos": position_f}
second_player = {"symbol": "s", "pos": position_s}
while True:
    command = input().split()
    position_f_directions = command[0]
    position_s_directions = command[1]
    move_player(marix, first_player, position_f_directions)

[print(*row) for row in matrix]
