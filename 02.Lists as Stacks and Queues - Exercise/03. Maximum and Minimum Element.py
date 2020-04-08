number = int(input())
stack = []
for _ in range(number):
    command = list(map(int,input().split(" ")))
    com = command[0]

    if com == 1:
        item = command[1]
        stack.append(item)
    if stack:
        if com == 2:
            stack.pop()
        elif com == 3:
            print(max(stack))
        elif com == 4:
            print(min(stack))

print(", ".join([str(x) for x in reversed(stack)]))
