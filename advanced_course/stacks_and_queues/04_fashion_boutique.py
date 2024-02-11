clothes_stack = [int(clothe) for clothe in input().split()]
rack_capacity = int(input())
left_capacity = rack_capacity
rack_counter = 1
num_clothes = len(clothes_stack)
for _ in range(num_clothes):
    if left_capacity >= clothes_stack[-1]:
        left_capacity -= clothes_stack.pop()
    else:
        rack_counter += 1
        left_capacity = rack_capacity
        left_capacity -= clothes_stack.pop()
print(rack_counter)
