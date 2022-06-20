nums = [int(el) for el in input().split()]
factor = int(input())
happiness = [el*factor for el in nums]
threshold = sum(happiness)/len(happiness)

happy_employees=[el for el in happiness if el >= threshold]
sad_employees=[el for el in happiness if el < threshold]

if len(sad_employees) > len(happiness)/2:
    print(f'Score: {len(happy_employees)}/{len(happiness)}. Employees are not happy!')
else:
    print(f'Score: {len(happy_employees)}/{len(happiness)}. Employees are happy!')

