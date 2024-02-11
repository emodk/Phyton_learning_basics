numbers = tuple(float(el) for el in input().split())
print(numbers)
num_occurance = {}
for num in numbers:
    if num not in num_occurance:
        num_occurance[num] = 0
    num_occurance[num] += 1
for key, value in num_occurance.items():
    print(f'{key} - {value} times')
