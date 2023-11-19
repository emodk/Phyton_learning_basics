elements = input().split()
food = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i+1]
    food[key] = int(value)
print(food)
