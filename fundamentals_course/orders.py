number_of_orders = int(input())
price = 0
total_price = 0
for i in range(1, number_of_orders + 1):
    price_of_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if 0.01 <= price_of_capsule <= 100:
        if 1 <= days <= 31:
            if 1 <= capsules <= 2000:
                price = price_of_capsule * days * capsules
                print(f"The price for the coffee is: ${price:.2f}")
                total_price += price
print(f'Total: ${total_price:.2f}')
