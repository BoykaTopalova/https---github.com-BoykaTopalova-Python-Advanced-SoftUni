from collections import deque

waves = int(input())

plates = deque([int(x) for x in input().split()])
warriors = []
flag = False
for wave in range(1, waves + 1):
    if flag:
        break
    warriors.extend([int(x) for x in input().split()])
    if wave % 3 == 0:
        new_plate = int(input())
        plates.append(new_plate)
    while warriors:
        if not plates:
            flag = True
            break
        current_warrior = warriors.pop()
        current_plate = plates.popleft()
        if current_warrior == current_plate:
            continue
        elif current_warrior > current_plate:
            current_warrior -= current_plate
            warriors.append(current_warrior)
        else:
            current_plate -= current_warrior
            plates.appendleft(current_plate)
if not plates:
    print("The Trojans successfully destroyed the Spartan defense.")
else:
    print("The Spartans successfully repulsed the Trojan attack.")

if warriors:
    print(f"Warriors left: {', '.join([str(x) for x in reversed(warriors)])}")

if plates:
    print(f"Plates left: {', '.join(map(str, plates))}")
