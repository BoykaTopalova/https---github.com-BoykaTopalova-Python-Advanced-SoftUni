from collections import deque

liquids = deque([int(x) for x in input().split()])
items = [int(x) for x in input().split()]
table = {
    'Glass': 25,
    'Aluminium': 50,
    'Lithium': 75,
    'Carbon fiber': 100
}
table_counter = {
    'Glass': 0,
    'Aluminium': 0,
    'Lithium': 0,
    'Carbon fiber': 0
}
sums = 0
while items and liquids:
    liquid_temp = liquids[0]
    temp_item = items[-1]
    sums = liquid_temp + temp_item
    if sums in table.values():
        liquids.popleft()
        items.pop()
        for element, number in table.items():
            if sums == number:
                table_counter[element] += 1

    else:
        liquids.popleft()
        temp = items.pop() + 3
        items.append(temp)
    sums = 0
if all(x > 0 for x in table_counter.values()):
    print("Wohoo! You succeeded in building the spaceship!")
else:
    print("Ugh, what a pity! You didn't have enough materials to build the spaceship.")
if liquids:
    print(f"Liquids left: {', '.join(map(str, liquids))}")
else:
    print("Liquids left: none")
if items:
    print(f"Physical items left: {', '.join(map(str, reversed(items)))}")
else:
    print("Physical items left: none")
for element, value in sorted(table_counter.items(), key=lambda x: x[0]):
    print(f"{element}: {value}")
