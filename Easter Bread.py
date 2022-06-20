budget = float(input())
flour_price = float(input())
price_one_pack_eggs = flour_price*0.75
milk_price_per_easter_bread = flour_price*1.25/4
one_easter_bread_price = flour_price+price_one_pack_eggs+milk_price_per_easter_bread
coloured_eggs=0
easter_bread_loaf=0

while budget-one_easter_bread_price>0:
    budget-=one_easter_bread_price
    easter_bread_loaf +=1
    coloured_eggs +=3
    if easter_bread_loaf %3 == 0:
        coloured_eggs -= easter_bread_loaf-2
print(f'You made {easter_bread_loaf} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.')



