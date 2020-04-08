from collections import deque

cups = deque([int(cup) for cup in input().split()])

stack_bottles = [int(bottle) for bottle in input().split()]
diff_water = 0
remaining_water = 0
diff = 0
while cups:

    if len(stack_bottles) != 0:
        current_cup = cups.popleft()
        current_bottle = stack_bottles.pop()
        diff_water = current_bottle - current_cup
        if diff_water >= 0:
            remaining_water += diff_water
        else:
            while diff_water < 0:
                if len(stack_bottles) != 0:
                    current_bottle = stack_bottles.pop()
                    diff_water = current_bottle - abs(diff_water)
                    if diff_water >= 0:
                        remaining_water += diff_water
                else:
                    break
    else:
        break
if len(cups) == 0:
    stack_bottles = reversed(stack_bottles)
    stack_bottles = [str(x) for x in stack_bottles]
    print(f"Bottles: {' '.join(stack_bottles)}")
if len(stack_bottles) == 0:
    cups = [str(i) for i in cups]
    print(f"Cups: {' '.join(cups)}")
print(f"Wasted litters of water: {remaining_water}")
