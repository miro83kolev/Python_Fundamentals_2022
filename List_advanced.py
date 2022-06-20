# a = "Hello There!".split()
# print(type(a))

# nums = [-2, 1, 5, 100]
# result = []
# for el in nums:
#     if el > 0:
#         result.append(el**2)
# print (result)
#
# print([el**2 for el in nums if el >0])

# nums=[1, 2, 3, 4, 5, 6]
# print(["even" if el%2==0 else "odd" for el in nums])
# # same as below
# result=[]
# for el in nums:
#     if el%2==0:
#         result.append("even")
#     else:
#         result.append("odd")
# print(result)

# nums=[1, 3, 5, 7]
# # nums.extend([6, 9]) - list in list
# print(nums)

# nums=[1, 3, 5, 7]
# nums.insert(2,6) - inserting 6 under index 2
# print(nums)

# nums=[1, 3, 5, 7]
# nums.clear() - clears all elements in a list
# print(nums)

# nums=[1, 3, 5, 7]
# nums.pop(1) - removes last element if you put an index removes the index
# print(nums)


# nums=[1, 3, 5, 7]
# nums.pop(1) - removes last element if you put an index removes the index
# print(nums)

# nums=[1, 3, 5]
# a, b, c = nums - unpack the exact number of elements, if more or less will give an error
# ==
# a = nums[0]
# b = nums[1]
# c = nums[2]
# # print(nums)

# nums=[1, 3, 5, 7]
# print(nums.count(7)) - finds how many times a number repeats

# nums=[1, 3, 5, 7]
# print(nums.index(3)) - finds a numbers index

# nums.reverse - reverses the list directly and stays modified
# result = reversed(nums)
# print(list(result))

# nums=[1, 3, 5, 7]
# print([int(el) for el in nums]) - list comprehension
# print(list(map(int, nums))) - mapping of a list converted to int

# nums=[1, 3, 5, 7, 8, 10]
# print([int(el) for el in nums if el%2==0]) - list comprehension - newest method
# print(list(filter(lambda x: x%2==0, nums))) - old method using filer, lamba and nums