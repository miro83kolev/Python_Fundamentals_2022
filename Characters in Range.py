def char_string (char1, char2):
    for i in range(ord(char1)+1, ord(char2)):
        print(chr(i), end= ' ')

char_one = input()
char_two = input()
char_string(char_one, char_two)
