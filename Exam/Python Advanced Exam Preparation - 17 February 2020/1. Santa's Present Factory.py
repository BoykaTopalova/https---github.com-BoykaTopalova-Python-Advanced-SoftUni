from collections import deque

stack_materials = [int(x) for x in input().split(" ")]
magic_level_queue = deque(int(x) for x in input().split(" "))

dict_table = {'Doll': 150, 'Wooden train': 250, 'Teddy bear': 300, 'Bicycle': 400}
new_dict = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}
sum_mix = 0

while len(magic_level_queue) != 0 and len(stack_materials) != 0:

    mix = (magic_level_queue[0] * stack_materials[-1])
    if stack_materials[-1] == 0:
        stack_materials.pop()
    if magic_level_queue[0] == 0:
        magic_level_queue.popleft()

    if mix in dict_table.values():
        stack_materials.pop()
        magic_level_queue.popleft()
        for (k, v) in dict_table.items():
            if mix == int(v):
                new_dict[k] += 1
    elif mix < 0:
        sum_mix = (stack_materials.pop() + magic_level_queue.popleft())
        if sum_mix != 0:
            stack_materials.append(sum_mix)
    elif mix not in dict_table.values() and mix > 0:
        magic_level_queue.popleft()
        n = (stack_materials.pop() + 15)
        if n != 0:
            stack_materials.append(n)

if new_dict['Doll'] != 0 and new_dict['Wooden train'] != 0 \
        or new_dict['Teddy bear'] != 0 and new_dict['Bicycle'] != 0:

    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if len(stack_materials) != 0:
    print(f"Materials left: {', '.join(map(str, reversed(stack_materials)))}")
if len(magic_level_queue) != 0:
    print(f"Magic left: {', '.join(map(str, magic_level_queue))}")
for (toy_name, amount) in sorted(new_dict.items(), key=lambda x: x[0]):
    if amount > 0:
        print(f"{toy_name}: {amount}")
