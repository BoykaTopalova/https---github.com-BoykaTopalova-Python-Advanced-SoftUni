from collections import deque

numbers = [int(x) for x in input().split()]
to_push, to_pop, searched_number = numbers

queue = deque([int(x) for x in input().split()])

[queue.popleft() for _ in range(to_pop)]

if searched_number in queue:
    print("True")
else:
    if queue:
        print(min(queue))
    else:
        print(0)