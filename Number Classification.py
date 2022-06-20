numbers = input().split(", ")
positive = [int(num) for num in numbers if int(num) >= 0]
negative = [int(num) for num in numbers if int(num) <0]
even = [int(num) for num in numbers if int(num) % 2 == 0]
odd = [int(num) for num in numbers if int(num) % 2 != 0]

print(f'Positive: {", ".join(map(str, positive))}')
print(f'Negative: {", ".join(map(str, negative))}')
print(f'Even: {", ".join(map(str, even))}')
print(f'Odd: {", ".join(map(str, odd))}')
