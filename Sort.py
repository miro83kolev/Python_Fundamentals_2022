def sorted_list(nums):
    new_sorted_list=[]
    for index in range(len(nums)):
        current_num=int(nums[index])
        new_sorted_list.append(current_num)
    print(sorted(new_sorted_list))

numbers_list = input().split()
sorted_list(numbers_list)