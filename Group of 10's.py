nums = [int(el) for el in input().split(", ")]
group = 10

while nums:
    nums_group =  []

    for num in nums:
        if num in range(group-10, group+1):
            nums_group.append(num)
    for num in nums_group:
        nums.remove(num)
    print(f" Group of {group}'s: {nums_group}")
    group +=10






