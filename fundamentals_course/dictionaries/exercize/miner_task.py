resource_dict = {}
while True:
    key, value = input(), input()
    if key == "stop" or value == "stop":
        break
    else:
        value = int(value)
        if key not in resource_dict.keys():
            resource_dict[key] = value
        else:
            resource_dict[key] += value
# print(resource_dict)
for (key, value) in resource_dict.items():
    print(f'{key} -> {value}')
