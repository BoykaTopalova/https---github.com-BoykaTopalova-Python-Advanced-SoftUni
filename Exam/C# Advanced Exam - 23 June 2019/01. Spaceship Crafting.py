from collections import deque

chemical_liquids = deque([int(x) for x in input().split(" ")])
physical_items = [int(x) for x in input().split(" ")]
table = {'Glass': 25, 'Aluminium': 50, 'Lithium': 75, 'Carbon fiber': 100}
table_mix = {'Glass': 0, 'Aluminium': 0, 'Lithium': 0, 'Carbon fiber': 0}
sums = 0
while chemical_liquids and physical_items:
    sums = chemical_liquids[0] + physical_items[-1]
    if sums in table.values():
        chemical_liquids.popleft()
        physical_items.pop()
        for (item, value) in table.items():
            if sums == value:
                table_mix[item] += 1
    else:
        chemical_liquids.popleft()
        temp = physical_items.pop() + 3
        physical_items.append(temp)
    sums = 0
if all(x > 0 for x in table_mix.values()):
    print("Wohoo! You succeeded in building the spaceship!")
else:
    print("Ugh, what a pity! You didn't have enough materials to build the spaceship.")
if chemical_liquids:
    print(f"Liquids left: {', '.join(map(str, chemical_liquids))}")
else:
    print("Liquids left: none")
if physical_items:
    physical_items = reversed(physical_items)
    print(f"Physical items left: {', '.join(map(str, physical_items))}")
else:
    print("Physical items left: none")
for item, value in sorted(table_mix.items(), key=lambda x: x[0]):
    print(f"{item}: {value}")
