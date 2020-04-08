number = int(input())
numbers = map(int, input().split(" "))
multiplication = map(lambda a: a * number, numbers)
print(*multiplication)
