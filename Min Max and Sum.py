def min_max_sum_list(nums):
    all_nums_list = []
    for index in range(len(nums)):
        current_num=int(nums[index])
        all_nums_list.append(current_num)
    print (f'The minimum number is {min(all_nums_list)}')
    print(f'The maximum number is {max(all_nums_list)}')
    print(f'The sum number is: {sum(all_nums_list)}')

sequence_nums=input().split()
min_max_sum_list(sequence_nums)


