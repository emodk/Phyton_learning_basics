integer_numbers_string = input()
amount_of_numbers_to_remove = int(input())
number_list = integer_numbers_string.split()
for i in range(len(number_list)):
    number_list[i] = int(number_list[i])
for j in range(amount_of_numbers_to_remove):
    number_list.remove(min(number_list))
# print(number_list)
# number_list.sort(reverse=True)
# del number_list[-1:-amount_of_numbers_to_remove - 1:-1]
for k in range(len(number_list)):
    number_list[k] = str(number_list[k])
print(', '.join(number_list))
