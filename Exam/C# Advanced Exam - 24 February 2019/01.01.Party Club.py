capacity = int(input())
halls_reservations = input().split()
reservation_sum = 0
hall = []
reservations = []
while halls_reservations:
    if halls_reservations[-1].isdigit():
        if hall:
            reservations.append(halls_reservations.pop())
            reservation_sum += int(reservations[-1])
            if reservation_sum > capacity:
                next_hall_reservation = int(reservations.pop())
                reservation_sum -= next_hall_reservation
                print(f'{hall.pop(0)} -> {", ".join(map(str, reservations))}')
                if hall:
                    reservations = [next_hall_reservation]
                    reservation_sum = next_hall_reservation
                else:
                    reservations = []
                    reservation_sum = 0
        else:
            halls_reservations.pop()
    elif halls_reservations[-1].isalpha():
        hall.append(halls_reservations.pop())