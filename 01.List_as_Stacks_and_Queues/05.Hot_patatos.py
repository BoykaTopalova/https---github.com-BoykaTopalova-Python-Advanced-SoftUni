# from collections import deque
#
#
# def solve(people, n):
#     people = deque(people)
#     index = 0
#     while people:
#         person = people.popleft()
#         index += 1
#         if index == n:
#             index = 0
#             if people:
#                 print(f'Removed {person}')
#             else:
#                 print(f'Last is {person}')
#
#         else:
#             people.append(person)
#
#
# solve(input().split(), int(input()))

from collections import deque


def solve(list_name, number):
    index = 0
    while list_name:
        person = list_name.popleft()
        index += 1
        if index == number:
            index = 0
            if list_name:
                print(f"Removed {person}")
            else:
                print(f"Last is {person}")
        else:
            list_name.append(person)


names = deque(input().split())
num = int(input())
solve(names, num)
