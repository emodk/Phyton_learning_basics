number_string = input()
number_of_beggars = int(input())
list_from_number_string = number_string.split(', ')
int_num_list = []
beggar_result_list = []
for i in list_from_number_string:
    n = int(i)
    int_num_list.append(n)
for j in range(1, number_of_beggars + 1):
    beggar_list = list()
    for k in range(j - 1, len(int_num_list), number_of_beggars):
        beggar_list.append(int_num_list[k])
    beggar_result = sum(beggar_list)
    beggar_result_list.append(beggar_result)
print(beggar_result_list)
