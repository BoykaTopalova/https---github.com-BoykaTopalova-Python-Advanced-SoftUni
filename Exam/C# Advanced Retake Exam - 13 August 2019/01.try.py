from collections import deque

ingredients = deque([int(x) for x in input().split()])
freshness = [int(x) for x in input().split()]
table = {
    'Mimosa': 150,
    'Daiquiri': 250,
    'Sunshine': 300,
    'Mojito': 400
}
count_table = {
    'Mimosa': 0,
    'Daiquiri': 0,
    'Sunshine': 0,
    'Mojito': 0
}
while ingredients and freshness:
    if ingredients[0] == 0:
        ingredients.popleft()
        continue
    multiplication = ingredients[0] * freshness[-1]
    if multiplication in table.values():
        for cocktail, value in table.items():
            if value == multiplication:
                count_table[cocktail] += 1
                ingredients.popleft()
                freshness.pop()

    elif multiplication not in table.values():
        freshness.pop()
        temp = ingredients.popleft() + 5
        ingredients.append(temp)

if all(count_table.values()):
    print("It's party time! The cocktails are ready!")
else:
    print("What a pity! You didn't manage to prepare all cocktails.")
if ingredients:
    print(f"Ingredients left: {sum(ingredients)}")
for cocktail, value in sorted(count_table.items(), key=lambda x: x[0]):
    if value > 0:
        print(f"# {cocktail} --> {value}")
