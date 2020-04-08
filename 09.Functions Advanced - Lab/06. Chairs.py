def combinations(values, k, comb=[]):
    if len(comb) == k:
        print(", ".join(comb))
        return
    for i in range(len(values)):
        x = values[i]
        comb.append(x)
        combinations(values[i + 1:], k, comb)
        comb.pop()


name = input().split(", ")
k = int(input())
combinations(name, k)
