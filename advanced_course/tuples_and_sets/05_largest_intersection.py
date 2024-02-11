number_of_lines = int(input())
intersection_length = 0
longest_intersection = []
for _ in range(number_of_lines):
    set_1 = set()
    set_2 = set()
    first_pair, second_pair = input().split("-")
    first_pair_data = tuple(first_pair.split(","))
    second_pair_data = tuple(second_pair.split(","))
    first_start = int(first_pair_data[0])
    first_stop = int(first_pair_data[1])
    second_start = int(second_pair_data[0])
    second_stop = int(second_pair_data[1])
    for i in range(first_start, first_stop + 1):
        set_1.add(i)
    for j in range(second_start, second_stop + 1):
        set_2.add(j)
    intersection_set = set_1.intersection(set_2)
#    print(intersection_set)
    if intersection_length < len(intersection_set):
        intersection_length = len(intersection_set)
        longest_intersection = list(intersection_set)
print(f"Longest intersection is {longest_intersection} with length {intersection_length}")
