# from collections import deque
#
#
# def solve():
#     liters = int(input())
#     people = deque()
#     while True:
#         person = input()
#         if person == 'Start':
#             break
#         people.append(person)
#
#     while people:
#         command = input()
#         if command.startswith('refill'):
#             liters += int(command.split()[1])
#             continue
#
#         person = people.popleft()
#         person_liters = int(command)
#         if liters < person_liters:
#             print(f'{person} must wait')
#         else:
#             liters -= person_liters
#             print(f'{person} got water')
#
#     print(f'{liters} liters left')
#
#
# solve()
from collections import deque

liters = int(input())
people = deque()

while True:
    name = input()
    people.append(name)
    if name == "Start":
        break

while True:
    command = input()

    if command == "End":
        break

    if command.startswith("refill"):
        water = int(command.split(' ')[1])
        liters += water
    else:
        water = int(command)
        person = people.popleft()

        if liters >= water:
            liters -= water

            print(f'{person} got water')
        else:
            print(f'{person} must wait')
            people.append(person)

print(f'{liters} liters left')