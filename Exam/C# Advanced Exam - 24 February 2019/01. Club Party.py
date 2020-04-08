from collections import deque

max_capacity = int(input())
info = [x for x in input().split(" ")]
hals = deque([])
reservations = []
sums = 0
while info:
    n = info.pop()
    if n.isalpha():
        hals.append(n)
        continue
    if not hals:
        continue
    new_reservation = int(n)
    if sum(reservations) + new_reservation <= max_capacity:
        reservations.append(new_reservation)
    else:
        print(f"{hals.popleft()} -> {', '.join([str(x) for x in reservations])}")
        reservations = []
        info.append(n)
