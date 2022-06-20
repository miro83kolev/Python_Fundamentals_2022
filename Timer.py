import time

user_start = int(input())
counter=user_start
clock = time.perf_counter()

while True:
    clock_1 = time.perf_counter()
    if clock_1 - clock >1:
        counter -=1
        print(counter)
        if counter <=0:
            print("Stop!")
            break
        clock=clock_1
