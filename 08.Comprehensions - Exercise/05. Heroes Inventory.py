names = input().split(', ')
heroes = {hero: {} for hero in names}
while True:
    command = input()
    if command == "End":
        break
    name, item, cost = command.split('-')
    if name in heroes:
        if item not in heroes[name]:
            heroes[name][item] = int(cost)
[print(f"{hero} -> Items: {len(heroes[hero])}, Cost: {sum(heroes[hero].values())}") for hero in heroes]
