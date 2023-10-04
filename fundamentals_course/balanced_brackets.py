number_of_lines = int(input())
brackets_string = ''
brackets_are = 'BALANCED'
for i in range(1, number_of_lines + 1):
    char_string = input()
    if char_string == '(' or char_string == ')':
        brackets_string += char_string
# print(brackets_string)
for j in range(0, len(brackets_string), 2):
    if brackets_string[j] != '(' or brackets_string[j+1] != ')':
        brackets_are = 'UNBALANCED'
        break
print(brackets_are)
