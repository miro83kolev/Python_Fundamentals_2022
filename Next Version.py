version = [int(el) for el in input().split(".")]
version[-1] +=1
for current_index in range(len(version)-1, -1, -1):
    if version[current_index]>9:
        version[current_index] = 0
        if current_index-1>=0:
            version[current_index-1] +=1
print(".".join(str(el) for el in version))