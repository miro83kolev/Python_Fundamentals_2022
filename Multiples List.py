# factor = int(input())
# count = int(input())
#
# num_list = []
#
# for i in range(1,count+1):
#     i *=factor
#     num_list.append(i)
# print(num_list)
factor = int(input())
count = int(input())
num_list = []

for multiplier in range(1,count+1):
    num_list.append(multiplier*factor)
print(num_list)
