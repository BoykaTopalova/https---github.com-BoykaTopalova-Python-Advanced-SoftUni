present = int(input())
rows = int(input())
matrix = []
santa_position = []
good_child = 0
count_presents = 0
good_c = 0
good_gift = 0

for i in range(rows):
    r = input().split()  # тука може да няма split!
    matrix.append(r)
    if 'S' in r:
        santa_position = (i, r.index('S'))
    good_child += r.count('V')

while True:
    command = input()
    if command == 'Christmas morning':
        break
    next_position = []
    if command == 'up':
        next_position = [santa_position[0] - 1, santa_position[1]]
    elif command == 'down':
        next_position = [santa_position[0] + 1, santa_position[1]]
    elif command == 'right':
        next_position = [santa_position[0], santa_position[1] + 1]
    elif command == 'left':
        next_position = [santa_position[0], santa_position[1] - 1]

    # check indices
    if 0 <= next_position[0] < len(matrix) and 0 <= next_position[1] < len(matrix):
        row = next_position[0]
        col = next_position[1]
        if matrix[row][col] == '-':
            matrix[santa_position[0]][santa_position[1]] = '-'
            matrix[row][col] = 'S'
            santa_position = next_position
        elif matrix[row][col] == 'X':
            matrix[santa_position[0]][santa_position[1]] = '-'
            matrix[row][col] = 'S'
            santa_position = next_position
        elif matrix[row][col] == 'V':
            count_presents += 1
            good_gift += 1
            matrix[santa_position[0]][santa_position[1]] = '-'
            matrix[row][col] = 'S'
            santa_position = next_position
        elif matrix[row][col] == 'C':
            matrix[santa_position[0]][santa_position[1]] = '-'
            matrix[row][col] = 'S'
            santa_position = next_position
            if (matrix[row][col - 1] == 'X' or matrix[row][col - 1] == 'V') and present > count_presents:
                count_presents += 1
                if matrix[row][col - 1] == 'V':
                    good_gift += 1
                matrix[row][col - 1] = '-'
            if (matrix[row][col + 1] == 'X' or matrix[row][col + 1] == 'V') and present > count_presents:
                count_presents += 1
                if matrix[row][col + 1] == 'V':
                    good_gift += 1
                matrix[row][col + 1] = '-'
            if (matrix[row - 1][col] == 'X' or matrix[row - 1][col] == 'V') and present > count_presents:
                count_presents += 1
                if matrix[row - 1][col] == 'V':
                    good_gift += 1
                matrix[row - 1][col] = '-'
            if (matrix[row + 1][col] == 'X' or matrix[row + 1][col] == 'V') and present > count_presents:
                count_presents += 1
                if matrix[row + 1][col] == 'V':
                    good_gift += 1
                matrix[row + 1][col] = '-'
        if count_presents == present:
            break

if (present - count_presents) == 0 and (good_child - good_gift) != 0:
    print('Santa ran out of presents!')
for m in matrix:
    good_c += m.count('V')
    print(*m)
if present >= count_presents and good_child - good_gift > 0:
    print(f'No presents for {good_c} nice kid/s.')
if good_c == 0:
    print(f'Good job, Santa! {good_child} happy nice kid/s.')