number = int(input())
is_balanced=True
has_open_bracket=False

for num in range(number):
    word = input()
    if word != '(' and word != ')':
        continue
    is_open_bracket = word == '('

    if has_open_bracket == is_open_bracket:
        is_balanced=False
        break
    has_open_bracket=is_open_bracket

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")


