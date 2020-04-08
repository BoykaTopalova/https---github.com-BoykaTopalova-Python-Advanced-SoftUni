def fix_calendar(n):
    for i in range(len(n)):
        for j in range(len(n) - 1):
            if n[j] > n[j + 1]:
                n[j + 1], n[j] = n[j], n[j + 1]
    return n


numbers = [3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)
