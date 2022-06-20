key = int(input())
number = int(input())

for index in range(1, number+1):
    character=ord(input())
    new_character = character+key
    word=chr(new_character)
    print(f'{word}', end="")
