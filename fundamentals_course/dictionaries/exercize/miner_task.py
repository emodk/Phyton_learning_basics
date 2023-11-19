resource_dict = {}
a = input()
while a != "stop":
    b = input()
    if b == "stop":
        break
    b = int(b)
    if a not in resource_dict.keys():
        resource_dict[a] = b
    else:
        resource_dict[a] += b
    a = input()
for (key, value) in resource_dict.items():
    print(f'{key} -> {value}')
