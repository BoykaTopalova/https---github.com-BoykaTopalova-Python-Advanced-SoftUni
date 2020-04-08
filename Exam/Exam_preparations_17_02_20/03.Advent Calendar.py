def fix_calendar(n):
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i] < n[j]:
                n[i], n[j] = n[j], n[i]
    return n


numbers = [3, 2, 1, 7, 9, 2]
fixed = fix_calendar(numbers)
print(fixed)
