def palindrome_integers(nums):
    new_list=[]
    for index in range (len(nums)):
        number=int(nums[index])
        new_list.append(number)
        for i in range (len(new_list)):
            num_as_string = str(new_list[i])
        if num_as_string == num_as_string[::-1]:
            print("True")
        else:
            print("False")

list_of_numbers = input().split(", ")
palindrome_integers(list_of_numbers)