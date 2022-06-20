group_size = int(input())
days = int(input())
companion_count=group_size
received_coins=0

for current_day in range (1, days+1):
    if current_day % 15 == 0:
        companion_count +=5
    if current_day % 10 == 0:
        companion_count -= 2
    if current_day % 1 == 0:
        received_coins +=50-(2*companion_count)
    if current_day % 3 == 0:
        received_coins -=3*companion_count
    if current_day % 5 == 0:
        received_coins +=20*companion_count
        if current_day % 3 == 0:
            received_coins -= 2*companion_count
final_coins = int(received_coins/companion_count)
print(f'{companion_count} companions received {final_coins} coins each.')


