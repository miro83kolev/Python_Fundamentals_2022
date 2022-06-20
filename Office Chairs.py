number = int(input())
needed_chairs = 0
count_free_seats = 0
room = 1


for chair in range(1,number+1):
    current_chair = input().split()
    chair_to_seat = current_chair[0]
    visitor = int(current_chair[1])
    if len(chair_to_seat) > visitor:
        free_seats = len(chair_to_seat) - visitor
        count_free_seats +=free_seats
    elif len(chair_to_seat) < visitor:
        needed_chairs = abs(len(chair_to_seat)-visitor)
        count_free_seats -=needed_chairs
        print(f'{needed_chairs} more chairs needed in room {room}')
    room +=1

if count_free_seats >=0:
    print(f"Game On, {count_free_seats} free chairs left")









