def solve(numbers):
    dictionary = {}

    for num in numbers:
        if num not in dictionary:
            dictionary[num] = 0
        dictionary[num] += 1

    for (number, count) in dictionary.items():
        print(f"{number} - {count} times")


numbers_f = list(map(float, input().split(" ")))
solve(numbers_f)
