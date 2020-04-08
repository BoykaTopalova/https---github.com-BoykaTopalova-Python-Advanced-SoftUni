from collections import deque

price_bullet = int(input())
size_gun = int(input())
stack_bullets = [int(bullet) for bullet in input().split()]
locks_queue = deque(int(lock) for lock in input().split())
intelligence = int(input())
diff = size_gun
current_lock = 0


while stack_bullets and locks_queue:

    current_bullet = stack_bullets.pop()
    current_lock = locks_queue.popleft()
    if current_bullet <= current_lock:
        print("Bang!")
        diff -= 1
        intelligence -= price_bullet

    else:
        print("Ping!")
        locks_queue.appendleft(current_lock)
        diff -= 1
        intelligence -= price_bullet
    if diff == 0:
        if stack_bullets:
            print("Reloading!")
            diff = size_gun
if stack_bullets:
    print(f"{len(stack_bullets)} bullets left. Earned ${intelligence}")
elif locks_queue:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")
else:
    print(f"{len(stack_bullets)} bullets left. Earned ${intelligence}")

