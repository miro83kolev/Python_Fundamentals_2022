num = int(input())
is_prime=True

if num>1:
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            is_prime=False
            break
if is_prime:
    print("True")
else:
    print("False")



