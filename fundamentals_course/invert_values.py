input_string = input()
list_from_string = input_string.split(" ")
new_list = []
for element in list_from_string:
    number = int(element)*(-1)
    new_list.append(number)
print(new_list)
