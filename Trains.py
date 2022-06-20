number_of_wagons = int(input())
train_wagons=[0]*number_of_wagons
command = input()

while not command == "End":
    data = command.split()
    if data[0] == "add":
        train_wagons[-1] +=int(data[1])
    elif data[0]== "insert":
        index = int(data[1])
        num_people = int(data[2])
        train_wagons[index] +=num_people
    elif data[0]== "leave":
        index = int(data[1])
        num_people = int(data[2])
        train_wagons[index] -= num_people

    command = input()

print(train_wagons)