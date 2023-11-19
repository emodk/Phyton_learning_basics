word_sequence = input()
word_list = word_sequence.lower().split()
# word_list = word_lower.split()
word_dict = {}
# final_list = []
value = 0
for word in word_list:
    if word not in word_dict.keys():
        word_dict[word] = 1
    else:
        word_dict[word] += 1
# print(word_dict)
for key, value in word_dict.items():
    if value % 2 != 0:
        print(key, end=' ')
#        final_list.append(key)
# print(" ".join(final_list))
