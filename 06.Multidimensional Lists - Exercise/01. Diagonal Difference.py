size = int(input())
matrix = []

sum_prime = 0
sum_secondary = 0

for x in range(0, size):
    matrix.append([int(x) for x in input().split()])
for i in range(len(matrix)):
    sum_prime += matrix[i][i]
    sum_secondary += matrix[i][size - i - 1]

diff = abs(sum_secondary - sum_prime)

print(diff)
