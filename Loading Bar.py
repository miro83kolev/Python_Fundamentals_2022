def loading_bar(num):
    ready=("%"*int(num/10))
    remain=("."*int(10-num/10))
    loading_bar = ready+remain
    return loading_bar

number = int(input())
if number==100:
    print(f'100% Complete!\n[{loading_bar(number)}]')
else:
    print(f'{number}% [{loading_bar(number)}]\nStill loading...')