num = int(input())
matrix = []
for i in range(num):
    line = [x for x in input().split()]
    matrix.append(line)
collected = []
seashell = ['N', 'M', 'C']
seagull_collected = []
while True:
    command = input()
    if command == "Sunset":
        break
    tokens = command.split(" ")
    com = tokens[0]
    if com == "Collect":
        row = int(tokens[1])
        col = int(tokens[2])
        if 0 <= row < num and 0 <= col < len(matrix[row]):
            if matrix[row][col] in seashell:
                collected.append(matrix[row][col])
                matrix[row][col] = '-'
    if com == "Steal":
        rows = int(tokens[1])
        cols = int(tokens[2])
        direction = tokens[3]
        if 0 <= rows < num and 0 <= cols < len(matrix[rows]):
            if matrix[rows][cols] in seashell:
                seagull_collected.append(matrix[rows][cols])
                matrix[rows][cols] = "-"
                for i in range(1, 4):
                    if direction == "up":
                        next_position = [rows - i, cols]
                    elif direction == "down":
                        next_position = [rows + i, cols]
                    elif direction == "right":
                        next_position = [rows, cols + i]
                    elif direction == "left":
                        next_position = [rows, cols - i]
                    if 0 <= next_position[0] < num and 0 <= next_position[1] < len(matrix[next_position[0]]):
                        if matrix[next_position[0]][next_position[1]] in seashell:
                            seagull_collected.append(matrix[next_position[0]][next_position[1]])
                            matrix[next_position[0]][next_position[1]] = "-"

[print(*row) for row in matrix]
if len(collected) != 0:
    print(f"Collected seashells: {len(collected)} -> {', '.join(collected)}")
else:
    print(f"Collected seashells: {len(collected)}")

print(f"Stolen seashells: {len(seagull_collected)}")
