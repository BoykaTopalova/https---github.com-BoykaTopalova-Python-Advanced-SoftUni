def operate(sing, *args):
    m = 0
    if sing == "*" or sing == "/":
        m = 1
    for n in args:
        if sing == "+":
            m += n
        elif sing == "/":
            m /= n
        elif sing == "-":
            m -= n
        elif sing == "*":
            m *= n
    return m


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
