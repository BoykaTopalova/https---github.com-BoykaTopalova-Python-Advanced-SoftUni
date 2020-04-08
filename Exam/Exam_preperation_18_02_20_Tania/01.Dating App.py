from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
count_matches = 0
while males and females:
    current_female = females[0]
    current_male = males[-1]
    if current_female <= 0:
        females.popleft()
    elif current_male <= 0:
        males.pop()
    elif current_female == current_male:
        males.pop()
        females.popleft()
        count_matches += 1
    elif current_female % 25 == 0:
        females.popleft()
        females.popleft()
    elif current_male % 25 == 0:
        males.pop()
        males.pop()
    else:
        females.popleft()
        males.append(males.pop() - 2)
print(f"Matches: {count_matches}")
if males:
    print(f"Males left: {', '.join([str(x) for x in reversed(males)])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")
