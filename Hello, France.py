items = input().split("|")
budget = float(input())
train_ticket = 150
profit = 0
money = 0

for item in range(len(items)):
    next_item = items[item].split("->")
    current_item = next_item[0]
    current_price = next_item[1]
    current_price= float(current_price)
    if current_item=="Clothes" and current_price >50:
        continue
    if current_item == "Shoes" and current_price > 35:
        continue
    if current_item == "Accessories" and current_price > 20.50:
        continue
    if budget<current_price:
        continue
    budget -=current_price
    print(f'{current_price*1.4:.2f}', end=" ")
    profit += current_price*0.4
    money += current_price*1.4
print()
print(f"Profit: {profit:.2f}")
if (money+budget)>train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")





