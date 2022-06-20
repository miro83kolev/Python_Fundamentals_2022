def sum_of_all(num):
    odd_sum=0
    even_sum=0
    for index in range(len(num)):
        current_num= int(num[index])
        if current_num % 2==0:
            even_sum += current_num
        else:
            odd_sum +=current_num
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')

number=input()
sum_of_all(number)