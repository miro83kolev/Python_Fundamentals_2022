def only_even_numbers (nums):
    even_nums_list=[]
    for index in range(len(nums)):
        current_num=int(nums[index])
        if current_num % 2==0:
            even_nums_list.append(current_num)
    print(even_nums_list)

list_of_nums = input().split()
only_even_numbers(list_of_nums)

