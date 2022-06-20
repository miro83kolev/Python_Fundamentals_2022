quantity = int(input())
days = int(input())
ornament_set = 2
tree_skirt = 5
tree_guirland = 3
tree_lights = 15
christmas_spirit=0
total_cost=0

for days_left in range(1, days+1):
    if days_left%11==0:
        quantity +=2
    if days_left%2==0:
        total_cost += ornament_set*quantity
        christmas_spirit +=5
    if days_left%3==0:
        total_cost +=(tree_skirt+tree_guirland)*quantity
        christmas_spirit +=13
    if days_left%5==0:
        total_cost +=tree_lights*quantity
        christmas_spirit +=17
        if days_left%3==0:
            christmas_spirit +=30
    if days_left%10==0:
        christmas_spirit -=20
        total_cost +=tree_skirt+tree_guirland+tree_lights
if days %10 ==0:
    christmas_spirit -=30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")

