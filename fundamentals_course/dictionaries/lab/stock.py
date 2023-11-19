items = input().split()
stock = {}
for i in range(0, len(items), 2):
    key = items[i]
    value = items[i+1]
    stock[key] = int(value)
items_for_check = input().split()
for product in items_for_check:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
