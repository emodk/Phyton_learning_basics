quantity_matt_dict = {"shards": 0, "fragments": 0, "motes": 0}
win = False
item_1 = "shards"
item_2 = "fragments"
item_3 = "motes"
while True:
    quantity_matt_pair = input().split()
    for i in range(0, len(quantity_matt_pair), 2):
        # print(quantity_matt_pair)
        value = int(quantity_matt_pair[i])
        key = quantity_matt_pair[i + 1].lower()
        if key in quantity_matt_dict.keys():
            quantity_matt_dict[key] += value
        else:
            quantity_matt_dict[key] = value
        if key == item_1 and quantity_matt_dict[item_1] >= 250:
            print("Shadowmourne obtained!")
            quantity_matt_dict["shards"] -= 250
            win = True
            break
        elif key == item_2 and quantity_matt_dict[item_2] >= 250:
            print("Valanyr obtained!")
            quantity_matt_dict[item_2] -= 250
            win = True
            break
        elif key == item_3 and quantity_matt_dict[item_3] >= 250:
            print("Dragonwrath obtained!")
            quantity_matt_dict[item_3] -= 250
            win = True
            break
    if win:
        break
print(f'{item_1}: {quantity_matt_dict[item_1]}')
print(f'{item_2}: {quantity_matt_dict[item_2]}')
print(f'{item_3}: {quantity_matt_dict[item_3]}')
for (key, value) in quantity_matt_dict.items():
    if key != item_1 and key != item_2 and key != item_3:
        print(f'{key}: {value}')
