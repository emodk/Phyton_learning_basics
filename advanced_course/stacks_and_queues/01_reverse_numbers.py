stack_of_integers = [int(el) for el in input().split()]
reversed_stack = []
for _ in range(len(stack_of_integers)):
    reversed_stack.append(stack_of_integers.pop())
print(" ".join([str(el) for el in reversed_stack]))
