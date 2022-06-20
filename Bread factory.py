energy = 100
coins = 100
is_closed=False
events=input().split("|")

for type in events:
    temp_event=type.split("-")
    temp_product = temp_event[0]
    temp_energy = int(temp_event[1])
    temp_coins = int(temp_event[1])
    if temp_product == "rest":
        if energy + temp_energy >100:
            print("You gained 0 energy.")
        else:
            energy +=temp_energy
            print(f"You gained {temp_energy} energy.")
        print(f"Current energy: {energy}.")
    elif temp_product == "order":
        if energy - 30 >= 0:
            print(f"You earned {temp_coins} coins.")
            coins +=temp_coins
            energy -=30
        else:
            energy +=50
            print(f"You had to rest!")
    else:
        if coins-temp_coins >0:
            print(f"You bought {temp_product}.")
            coins -=temp_coins
        else:
            print(f"Closed! Cannot afford {temp_product}.")
            is_closed = True
            break
if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


