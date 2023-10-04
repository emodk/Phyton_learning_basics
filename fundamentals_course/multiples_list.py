number_for_factor = int(input())
number_for_counter = int(input())
my_list = []
element = 0
for i in range(number_for_counter):
    element += number_for_factor
    my_list.append(element)
print(my_list)
