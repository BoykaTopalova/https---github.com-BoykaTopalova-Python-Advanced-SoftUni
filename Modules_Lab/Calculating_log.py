from math import log


def solve(number, base_str):
    result = None
    if base_str == "natural":
        result = log(number)
    else:
        base = int(base_str)
        result = log(number, base)
    return f"{result:.2f}"


number = int(input())
base_str = input()
print(solve(number, base_str))

