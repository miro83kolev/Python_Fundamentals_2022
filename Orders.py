orders = int(input())
daily_price=0
total_price=0

for each_order in range(1, orders+1):
    capsule_price = float(input())
    days = float(input())
    capsule_count = float(input())
    daily_price = capsule_price * days * capsule_count
    print(f'The price for the coffee is: ${daily_price:.2f}')
    total_price += daily_price

print(f"Total: ${total_price:.2f}")
