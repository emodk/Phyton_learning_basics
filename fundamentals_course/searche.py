number_of_lines = int(input())
key_word = input()
general_string_list = []
key_word_string_list = []
for i in range(number_of_lines):
    current_string = input()
    general_string_list.append(current_string)
    if key_word in current_string:
        key_word_string_list.append(current_string)
print(general_string_list)
print(key_word_string_list)
