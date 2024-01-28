data = input().split()
total_sum = 0
first_string = data[0]
second_string = data[1]
length_diff = abs(len(first_string) - len(second_string))
lower_string_length = min(len(first_string), len(second_string))
for i in range(lower_string_length):
    total_sum += ord(first_string[i]) * ord(second_string[i])
for j in range(-1, -length_diff - 1, -1):
    if len(first_string) < len(second_string):
        total_sum += ord(second_string[j])
    else:
        total_sum += ord(first_string[j])
print(total_sum)
