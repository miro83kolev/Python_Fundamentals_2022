# word = input()
#
# indices = [index for index, character in enumerate(word) if character.isupper()]
#
# print(indices)

word = input()

indices = []
for index, value in enumerate(word):
    if value.isupper():
        indices.append(index)

print(indices)