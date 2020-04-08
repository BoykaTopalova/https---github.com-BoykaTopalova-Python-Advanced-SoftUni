size = int(input())
commands = input().split()
matrix = []
miner_position = []
coals = 0
total_coals = 0
end = False

for i in range(size):
    row = input().split()
    matrix.append(row)
    if "s" in row:
        miner_position = [i, row.index("s")]
    total_coals += row.count("c")

ways = {'left': [0, -1], 'right': [0, 1], 'up': [-1, 0], 'down': [1, 0]}

for command in commands:
    change_way = ways[command]
    next_miner_row = miner_position[0] + change_way[0]
    next_miner_col = miner_position[1] + change_way[1]
    next_miner_position = [next_miner_row, next_miner_col]

    if 0 <= next_miner_row < len(matrix) and 0 <= next_miner_col < len(matrix):
        if matrix[next_miner_row][next_miner_col] == "*":
            matrix[miner_position[0]][miner_position[1]] = "*"
            matrix[next_miner_row][next_miner_col] = "s"
            miner_position = next_miner_position
        elif matrix[next_miner_row][next_miner_col] == "e":
            print(f"Game over! ({next_miner_row}, {next_miner_col})")
            end = True
            break
        elif matrix[next_miner_row][next_miner_col] == "c":
            coals += 1
            if coals == total_coals:
                print(f"You collected all coals! ({next_miner_row}, {next_miner_col})")
                end = True
                break
            matrix[miner_position[0]][miner_position[1]] = "*"
            matrix[next_miner_row][next_miner_col] = "s"
            miner_position = next_miner_position
if not end:
    print(f"{total_coals - coals} coals left. ({miner_position[0]}, {miner_position[1]})")
