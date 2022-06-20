# people_waiting = int(input())
#
# carriages = input().split()
# queue = []
# capacity = 4
#
# for i in range(len(carriages)):
#     if int(carriages[i]) <= capacity <= people_waiting:
#         people_waiting -= capacity - int(carriages[i])
#         queue.append(capacity)
#
#         if 0 < people_waiting < capacity:
#             queue.append(capacity - (capacity - people_waiting))
#
# string_queue = [str(int) for int in queue]
# if 0 < people_waiting < capacity:
#     print("The lift has empty spots!")
#     print(' '.join(string_queue))
# elif people_waiting > capacity:
#     print(f"There isn't enough space! {people_waiting} people in a queue!")
#     print(' '.join(string_queue))

people = int(input())
all_people = people
wagons = input().split()
max_places = 4
sum_places = sum([int(num) for num in wagons])
empty_places = len(wagons) * max_places - sum_places

for i in range(len(wagons)):
    if int(wagons[i]) < 4 and people >= 4:
        people -= max_places - int(wagons[i])
        wagons[i] = str(max_places)
    elif int(wagons[i]) < 4 and people < 4:
        wagons[i] = str(int(wagons[i]) + people)
        people = 0
        break

if people == 0 and empty_places > all_people:
    print("The lift has empty spots!")
    print(" ".join(wagons))
elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(wagons))
elif empty_places == all_people and people == 0:
    print(" ".join(wagons))
