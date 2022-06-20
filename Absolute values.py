nums = input().split()
nums_list = []

def absolute_num():
    for i in range(len(nums)):
        current_num = abs(float(nums[i]))
        nums_list.append(current_num)
    print(nums_list)

absolute_num()
