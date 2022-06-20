number = int(input())
tank=255
capacity=0

for i in range (1, number+1):
    litters = int(input())
    if capacity+litters<=tank:
        capacity +=litters
    else:
        print("Insufficient capacity!")
print(capacity)














