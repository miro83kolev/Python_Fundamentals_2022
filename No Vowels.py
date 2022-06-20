# text = input()
# all_vowels = ['a', 'e', 'i','o', 'u','A', 'E', 'I','O', 'U']
# no_vowels =''.join([el for el in text if el not in all_vowels])
# print(no_vowels)

text=input()
vowels=['a', 'e', 'i', 'o', 'u']
print(''.join([el for el in text if el.lower() not in vowels]))
