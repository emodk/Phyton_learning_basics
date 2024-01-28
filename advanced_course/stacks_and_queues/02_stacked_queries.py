query_stack = []
number_of_entries = int(input())
min_stack = []
max_stack = []
rev_query_stack = []
for _ in range(number_of_entries):
    command = [int(el) for el in input().split()]
    if command[0] == 1:
        num1 = command[1]
        if len(query_stack) == 0:
            min_stack.append(num1)
            max_stack.append(num1)
        else:
            if num1 > max_stack[-1]:
                max_stack.append(num1)
            elif num1 < min_stack[-1]:
                min_stack.append(num1)
        query_stack.append(command[1])
    elif command[0] == 2:
        if len(query_stack) > 0:
            num1 = query_stack.pop()
            if num1 == max_stack[-1]:
                max_stack.pop()
            if num1 == min_stack[-1]:
                min_stack.pop()
    elif command[0] == 3:
        if len(max_stack) > 0:
            print(max_stack[-1])
    elif command[0] == 4:
        if len(min_stack) > 0:
            print(min_stack[-1])
for _ in range(len(query_stack)):
    rev_query_stack.append(query_stack.pop())
print(", ".join([str(el) for el in rev_query_stack]))
