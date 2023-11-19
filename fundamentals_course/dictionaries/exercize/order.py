product_dict = {}
command = input()
while command != "buy":
    command = command.split()
    # print(command)
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if product not in product_dict.keys():
        product_dict[product] = {"price": price, "quantity": quantity}
    else:
        product_dict[product]["quantity"] += quantity
        product_dict[product]["price"] = price
    command = input()
for product in product_dict.keys():
    total_price = product_dict[product]["quantity"] * product_dict[product]["price"]
    print(f'{product} -> {total_price:.2f}')
