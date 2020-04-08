from collections import deque

males = [int(x) for x in input().split(" ")]
females = deque([int(x) for x in input().split(" ")])
matches = 0
males = list(filter(lambda x: x > 0, males))
females = deque(filter(lambda x: x > 0, females))

while True:
    if len(males) == 0 or len(females) == 0:
        break
    elif males[-1] % 25 == 0:
        males.pop()
        if len(males) != 0:
            males.pop()
        else:
            break
    elif females[0] % 25 == 0:
        females.popleft()
        if len(females) != 0:
            females.popleft()
        else:
            break
    elif females[0] == males[-1]:
        males.pop()
        females.popleft()
        matches += 1
    else:
        females.popleft()
        males.append(males.pop() - 2)
        if males[-1] <= 0:
            males.pop()

print(f"Matches: {matches}")
if not males:
    print(f"Males left: none")
else:
    males = reversed(males)
    print(f"Males left: {', '.join([str(x) for x in males])}")
if not females:
    print(f"Females left: none")
else:
    print(f"Females left: {', '.join([str(x) for x in females])}")
