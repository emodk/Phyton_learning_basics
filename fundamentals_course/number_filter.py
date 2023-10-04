number_of_lines = int(input())
my_list = []
for i in range(number_of_lines):
    current_number = int(input())
    my_list.append(current_number)
command = input()
if command == 'even':
    for j in range(len(my_list) - 1, -1, -1):
        if my_list[j] % 2 != 0:
            my_list.remove(my_list[j])
    print(my_list)
elif command == 'odd':
    for j in range(len(my_list) - 1, -1, -1):
        if my_list[j] % 2 == 0:
            my_list.remove(my_list[j])
    print(my_list)
elif command == 'positive':
    for j in range(len(my_list) - 1, -1, -1):
        if my_list[j] < 0:
            my_list.remove(my_list[j])
    print(my_list)
elif command == 'negative':
    for j in range(len(my_list) - 1, -1, -1):
        if my_list[j] >= 0:
            my_list.remove(my_list[j])
    print(my_list)
