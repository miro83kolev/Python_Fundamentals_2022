n=int(input())
searched_word=input()
all_words_list = []
searched_word_list = []

for i in range(n):
    current_sentence = input()
    all_words_list.append(current_sentence)
    if searched_word in current_sentence:
        searched_word_list.append(current_sentence)
print(all_words_list)
print(searched_word_list)