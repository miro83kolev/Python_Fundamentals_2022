numbers_str = input().split()
elem=""

numbers = []

for num in numbers_str:
    numbers.append(int(num))

remover = int(input())

for _ in range(remover):
    numbers.remove(min(numbers))
    list_to_string= ', '.join(str(elem) for elem in numbers)
print(list_to_string)












