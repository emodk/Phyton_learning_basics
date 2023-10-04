number_string = input()
number_of_beggars = int(input())
number_list = number_string.split(', ')
int_num_list = []
n = 0
for i in number_list:
    n = int(i)
    int_num_list.append(n)
for j in range(number_of_beggars):
    for k in range(len(int_num_list)):