def solve(s):
    return s[::-1]


def solve(string):
    stack = []
    for ch in string:
        stack.append(ch)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str


text = input()
print(solve(text))
