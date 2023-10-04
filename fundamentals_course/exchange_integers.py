a = int(input())
b = int(input())
print("Before:")
print(f'a = {a}')
print(f'b = {b}')
old_b = b
b = a
a = old_b
print("After:")
print(f'a = {a}')
print(f'b = {b}')
