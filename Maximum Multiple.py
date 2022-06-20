divisor = int(input())
boundary = int(input())
largest_num = 0

for number in range (divisor, boundary+1):
    if number%divisor==0 and number<=boundary and number>0:
        largest_num=number
print(largest_num)
