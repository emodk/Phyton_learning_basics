cards_string = input()
number_of_shuffles = int(input())
cards_list = cards_string.split(' ')
for i in range(number_of_shuffles):
    buffer_list = list([' '] * len(cards_list))
    buffer_list[0] = cards_list[0]
    buffer_list[-1] = cards_list[-1]
    for j in range(1, (len(cards_list) // 2)):
        buffer_list[2 * j] = cards_list[j]
    for k in range(-2, -len(cards_list) // 2 - 1, -1):
        buffer_list[2 * k + 1] = cards_list[k]
    cards_list = buffer_list
print(cards_list)
