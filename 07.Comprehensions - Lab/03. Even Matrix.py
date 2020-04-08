size = int(input())
matrix = []
for _ in range(size):
    r = [int(num) for num in input().split(", ") if int(num) % 2 == 0]
    matrix.append(r)

print(matrix)
