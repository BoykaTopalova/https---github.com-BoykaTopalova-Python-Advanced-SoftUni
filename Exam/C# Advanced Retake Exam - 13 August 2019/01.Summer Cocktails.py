from collections import deque

ingredient = deque(int(x) for x in input().split(" "))
freshness = [int(x) for x in input().split(" ")]
cocktails = {'Mimosa': 150, 'Daiquiri': 250, 'Sunshine': 300, 'Mojito': 400}
count_cocktails = {'Mimosa': 0, 'Daiquiri': 0, 'Sunshine': 0, 'Mojito': 0}

while len(ingredient) != 0 and len(freshness) != 0:
    if ingredient[0] == 0:
        ingredient.popleft()
        continue
    produkts = (ingredient[0] * freshness[-1])
    if produkts in cocktails.values():
        for name, value in cocktails.items():
            if produkts == value:
                count_cocktails[name] += 1
                ingredient.popleft()
                freshness.pop()
    elif produkts not in cocktails.values():
        freshness.pop()
        n = ingredient.popleft() + 5
        ingredient.append(n)

if all(count_cocktails.values()):
    print("It's party time! The cocktails are ready!")
else:
    print("What a pity! You didn't manage to prepare all cocktails.")
if len(ingredient) != 0:
    sums = 0
    for i in reversed(ingredient):
        sums += i
    print(f"Ingredients left: {sums}")
for name_cocktails, count in sorted(count_cocktails.items(), key=lambda x: x[0]):
    if count > 0:
        print(f" # {name_cocktails} --> {count}")
