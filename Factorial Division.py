import math
def factorial_devision(num1, num2):
    a=math.factorial(num1)
    b=math.factorial(num2)
    return a/b

number1 = int(input())
number2 = int(input())
result = factorial_devision(number1, number2)
print(f'{result:.2f}')
