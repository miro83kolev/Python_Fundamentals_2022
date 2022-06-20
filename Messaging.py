# numbers = input().split()
# text = input()  # This is some message for you
# message = ""
#
# for i in range(len(numbers)):
#     sum_of_digits = sum(map(int, numbers[i]))
#
#     if sum_of_digits > len((text)):
#         while sum_of_digits >= len(text):
#             sum_of_digits -= len(text)
#             if sum_of_digits <= len(text):
#                 message += text[sum_of_digits]
#
#     else:
#         message += text[sum_of_digits]
#
#     text = text[:sum_of_digits] + text[sum_of_digits + 1:]
#
# print(message)

numbers = input().split(' ')
sequence = list(input())
message = []

for num in numbers:
    digits_sum = 0
    for digit in num:
        digits_sum += int(digit)
    char_index = digits_sum % len(sequence)
    message.append(sequence[char_index])
    sequence.pop(char_index)

print(''.join(message))











