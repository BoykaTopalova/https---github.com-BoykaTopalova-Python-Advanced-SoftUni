list_cars = []
while True:
    command = input().split(", ")
    direction = command[0]
    if direction == "IN":
        car_number = command[1]
        if car_number not in list_cars:
            list_cars.append(car_number)
    elif direction == "OUT":
        car_number = command[1]
        if car_number in list_cars:
            list_cars.remove(car_number)
    if direction == "END":
        break
if len(list_cars) == 0:
    print("Parking Lot is Empty")
else:
    for item in list_cars:
        print(item)
