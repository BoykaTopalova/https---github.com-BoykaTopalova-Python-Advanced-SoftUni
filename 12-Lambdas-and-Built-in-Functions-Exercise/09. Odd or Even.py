command = input()
numbers = list(map(int, input().split()))
length = len(numbers)
if command == "Even":
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(sum(even_numbers)*length)
elif command == "Odd":
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    print(sum(odd_numbers)*length)

