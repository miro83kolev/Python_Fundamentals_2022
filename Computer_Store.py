command= input()
price_without_tax=0
tax=0
sum_tax=0
total_price=0

while command !="regular" and command !="special":
    price=float(command)
    if price<=0:
        print("Invalid price!")

        command=input()
    else:
        price_without_tax +=price
        tax = 0.2*price
        sum_tax +=tax
        total_price +=price*1.2

        command=input()

if total_price ==0:
    print("Invalid order!")
elif command == "special":
    total_price *=0.9
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_tax}$")
    print(f"Taxes: {sum_tax:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
elif command == "regular":
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_tax}$")
    print(f"Taxes: {sum_tax:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")














