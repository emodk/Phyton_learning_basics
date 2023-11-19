command = input()
total_quantity = 0
items = {}
while command != "statistics":
    product = command.split(": ")
    key = product[0]
    value = int(product[1])
    if key in items:
        items[key] += value
    else:
        items[key] = value
    command = input()
print("Products in stock:")
for key in items:
    print(f'- {key}: {items[key]}')
    total_quantity += items[key]
print(f'Total Products: {len(items)}')
print(f'Total Quantity: {total_quantity}')
