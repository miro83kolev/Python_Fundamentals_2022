# numbers_string = input().split(", ")
# new_list = [int(i) for i in numbers_string]
# for i in new_list:
#     if i == 0:
#         new_list.remove(i)
#         new_list.append(i)
# print(new_list)


# for n in numbers_string:
#     current_num=int(n)
#     if current_num == 0:
#         numbers_string.remove(n)
#         numbers_string.append(n)
# new_list =list(map(int, numbers_string))
# print(new_list)

number_string =input().split(",")
new_list = []
for i in number_string:
    current_num = int(i)
    new_list.append(current_num)
for _ in new_list:
    if 0 in new_list:
        new_list.remove(0)
        new_list.append(0)
print(new_list)


