# some_text = input()
# split_text=some_text.split(" ")
# reversed_num = 0
# reversed_list = []
#
# for i in range (len(split_text)):
#     number=split_text[i]
#     number=int(number)
#     if number>=0:
#         reversed_num =-abs(number)
#         reversed_list.append(reversed_num)
#     else:
#         reversed_num = abs(number)
#         reversed_list.append(reversed_num)
# print(reversed_list)

some_text=input().split()
inverted_list=[-int(s) for s in some_text]
print(inverted_list)




