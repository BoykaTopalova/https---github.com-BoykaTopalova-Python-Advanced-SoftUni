from collections import deque

waves = int(input())
plates = deque(int(x) for x in input().split())
warriors = []
end = False

for wave in range(1, waves + 1):
    if end:
        break

    warriors.extend([int(x) for x in input().split()])

    if wave % 3 == 0:
        new_plate = int(input())
        plates.append(new_plate)

    while warriors:
        if not plates:
            end = True
            break

        current_warrior = warriors.pop()
        current_plate = plates.popleft()

        if current_warrior == current_plate:
            continue

        elif current_plate > current_warrior:
            current_plate -= current_warrior
            plates.appendleft(current_plate)

        else:
            current_warrior -= current_plate
            warriors.append(current_warrior)

if not plates:
    print("The Trojans successfully destroyed the Spartan defense.")
else:
    print("The Spartans successfully repulsed the Trojan attack.")

if plates:
    print(f"Plates left: {', '.join([str(x) for x in plates])}")
elif warriors:
    print(f"Warriors left: {', '.join([str(x) for x in reversed(warriors)])}")