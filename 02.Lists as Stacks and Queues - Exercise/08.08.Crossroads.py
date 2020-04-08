from collections import deque


def crossroad():
    global queue, green_time, safe_time, passed_cars, crash
    green_time_left = green_time
    safe_time_left = safe_time
    queue = deque(queue)

    while green_time_left > 0 and queue:
        car_in_crosssection = queue.popleft()
        car_queue = deque(car_in_crosssection)
        while car_queue:
            char = car_queue.popleft()
            green_time_left -= 1
            if green_time_left < 0:
                safe_time_left -= 1
                if safe_time_left < 0:
                    crash = True
                    print("A crash happened!")
                    print(f"{car_in_crosssection} was hit at {char}.")
                    exit()
        passed_cars.append(car_in_crosssection)


green_time = int(input())
safe_time = int(input())
queue = []
passed_cars = []
crash = False

while True:
    car = input()

    if car == "END":
        break
    elif car == "green":
        crossroad()
    else:
        queue.append(car)

if not crash:
    print("Everyone is safe.")
    print(f"{len(passed_cars)} total cars passed the crossroads.")