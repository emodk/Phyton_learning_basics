init_string = input()
dict_string = {}
for i in init_string:
    if i == " ":
        continue
    else:
        if i not in dict_string.keys():
            dict_string[i] = 1
        else:
            dict_string[i] += 1
for (key, value) in dict_string.items():
    print(f'{key} -> {value}')
