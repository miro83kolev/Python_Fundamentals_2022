times = [int(el) for el in input().split()]
finish = len(times)//2
first_car_time = times[0:finish]
second_car_time = times[-1:finish:-1]

first_time = 0
second_time = 0

for current_time in first_car_time:
    first_time +=current_time
    if current_time==0:
        first_time *=0.8

for current_time in second_car_time:
    second_time +=current_time
    if current_time==0:
        second_time *=0.8

if first_time>second_time:
    print(f"The winner is right with total time: {second_time:.1f}")
else:
    print(f"The winner is left with total time: {first_time:.1f}")