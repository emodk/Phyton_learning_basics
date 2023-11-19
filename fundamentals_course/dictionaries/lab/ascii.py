list_of_char = input().split(", ")
char_dict ={}
for i in list_of_char:
    if i not in char_dict.keys():
        char_dict[i] = ord(i)
print(char_dict)
