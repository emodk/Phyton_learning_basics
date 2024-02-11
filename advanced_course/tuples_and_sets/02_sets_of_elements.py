n, m = input().split()
n = int(n)
m = int(m)
first_set = set()
second_set = set()
for _ in range(n):
    first_set.add(int(input()))
for _ in range(m):
    second_set.add(int(input()))
unique_set = first_set & second_set
for el in unique_set:
    print(el)
