number_of_lines = int(input())
odd_set = set()
even_set = set()
ascii_sum = 0
for i in range(number_of_lines):
    name = input()
    for letter in name:
        ascii_sum += ord(letter)
    result = ascii_sum // (i + 1)
    if (result % 2) == 0:
        even_set.add(result)
    else:
        odd_set.add(result)
    ascii_sum = 0
sum_even_set = sum(even_set)
sum_odd_set = sum(odd_set)
if sum_odd_set == sum_even_set:
    set_as_str = str(odd_set.union(even_set))
    print(set_as_str[1:len(set_as_str) - 1])
elif sum_odd_set > sum_even_set:
    set_as_str = str(odd_set.difference(even_set))
    print(set_as_str[1:len(set_as_str) - 1])
else:
    set_as_str = str(odd_set.symmetric_difference(even_set))
    print(set_as_str[1:len(set_as_str) - 1])
