numbers = list(map(lambda x: round(float(x)), input().split(" ")))
length = len(numbers)
multiplied = map(lambda x: x * length, numbers)
print(sum(multiplied))
