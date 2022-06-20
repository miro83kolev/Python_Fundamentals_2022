lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shied_price = float(input())
armor_price = float(input())
needed_money=0
shield_count = 0

for each_lost_fight in range (1, lost_fight_count+1):
    if each_lost_fight % 2 == 0:
        needed_money +=helmet_price
    if each_lost_fight % 3 == 0:
        needed_money += sword_price
    if each_lost_fight % 2 == 0 and each_lost_fight % 3==0:
        needed_money +=shied_price
        shield_count +=1
    if shield_count % 2 == 0 and shield_count>0:
        needed_money +=armor_price
        shield_count =0

print(f"Gladiator expenses: {needed_money:.2f} aureus")





