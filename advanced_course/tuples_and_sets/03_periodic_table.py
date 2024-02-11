line_numbers = int(input())
set_of_elements = set()
for _ in range(line_numbers):
    el = input().split()
    for i in el:
        set_of_elements.add(i)
for element in set_of_elements:
    print(element)
