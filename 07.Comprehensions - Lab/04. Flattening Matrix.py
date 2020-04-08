n = int(input())
matrix = [map(int, input().split(",")) for _ in range(n)]
flattened = [num for sublist in matrix for num in sublist]
print(flattened)
