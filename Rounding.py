nums_list = input().split()
new_list = []

def round_number():
    for i in range(len(nums_list)):
        current_num =round(float(nums_list[i]))
        new_list.append(current_num)
    print(new_list)
round_number()
