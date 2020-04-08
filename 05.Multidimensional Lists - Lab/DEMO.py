# Creating 3X3 Grid with Numbers
print("Creating 3X3 Grid with Numbers")
x = []
for i in range(3):
    x.append([])
    for j in range(1, 4):
        x[i].append(j)
print(x)

print("-----------------------------------------------")

# Using comprehension
x = [[i for i in range(1, 4)] for j in range(3)]
print(x)

print("-----------------------------------------------")
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j], end=" ")
    print()

print("-----------------------------------------------")
# Using comprehension to traverse multidimensional lists

[print(num) for num in [j for j in x]]
print()
[print(*num) for num in [j for j in x]]

print("-----------------------------------------------")

# Example: Increasing each value by 1

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j] += 1
print(x)

print("-----------------------------------------------")
columns = 2
rows = 3
x = [[j + columns * i for j in range(columns)] for i in range(rows)]
print(x)

print("--------------------------------------------")

x = []
rows = 3
columns = 2
for row in range(rows):
    x.append([])
    for col in range(1, columns + 1):
        x[-1].append(col + row * columns)
print(x)

print("--------------------------------------------")

x = []
for i in range(3):
    x.append([])
    for j in range(2):
        x[i].append(0)
print(x)

print("--------------------------------------------")

x = [[0 for i in range(2)] for i in range(3)]
print(x)