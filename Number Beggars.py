nums_string = input().split(", ")
count_beggars=int(input())
counter_of_index=0
final_list = []
temp_sum = 0
nums_string_as_digit = []

for index in range (len(nums_string)):
    nums_string_as_digit.append(int(nums_string[index]))

while counter_of_index<count_beggars:
    for element in range(counter_of_index,len(nums_string_as_digit),count_beggars):
        temp_sum +=nums_string_as_digit[element]
    final_list.append(temp_sum)
    temp_sum=0
    counter_of_index +=1
print(final_list)


