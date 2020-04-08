def solve(numbers):
    dictionary = {}

    for num in numbers:
        if num not in dictionary:
            dictionary[num] = 0
        dictionary[num] += 1

    for (alpha, count) in sorted(dictionary.items(), key=lambda x: x[0]):
        print(f"{alpha}: {count} time/s")


numbers_f = input()
solve(numbers_f)