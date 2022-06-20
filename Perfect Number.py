def perfect_number(num1):
    sum=0
    for index in range(1,num1):
        if num1%index==0:
            sum +=index
            sum == num1
    if sum == num1:
        print("We have a perfect number!" )
    else:
        print("It's not so perfect.")

number = int(input())
perfect_number(number)