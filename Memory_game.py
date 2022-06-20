elements = input().split()

moves = 0
command = input()
while not command == 'end':

    arg = command.split()
    index_1 = int(arg[0])
    index_2 = int(arg[1])
    moves += 1
    if 0 <= index_1 < len(elements) and 0 <= index_2 < len(elements):
        value_1 = elements[index_1]
        value_2 = elements[index_2]
        if value_1 == value_2:
            print(f"Congrats! You have found matching elements - {value_1}!")
            elements.remove(value_1)
            elements.remove(value_2)
        else:
            print('Try again!')
    else:
        print("Invalid input! Adding additional elements to the board")
        middle = int(len(elements) / 2)
        for el in range(moves):
            elements.insert(middle, f"-{str(moves)}a")

    if len(elements) == 0 and len(elements)==1:
        print(f"You have won in {moves} turns!")
        break

    command = input()

if len(elements) != 0:
    print("Sorry you lose :(")
    print(" ".join(elements))