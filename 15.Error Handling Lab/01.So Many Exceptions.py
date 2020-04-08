def multiply(*args):
    result = 1
    for i in range(len(args)):
        number = args[i]
        if number <= 6:
            result *= number
        elif number <= 10:
            result /= number
    return result


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
