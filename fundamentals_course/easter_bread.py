budget = float(input())
kg_flour_price = float(input())
pack_of_eggs_price = kg_flour_price * 0.75
milk_price = kg_flour_price * 1.25 / 4
one_loave_expenses = kg_flour_price + pack_of_eggs_price + milk_price
colored_eggs_counter = 0
loave_counter = 0
while budget >= one_loave_expenses:
    budget -= one_loave_expenses
    loave_counter += 1
    colored_eggs_counter += 3
    if loave_counter % 3 == 0:
        colored_eggs_counter -= loave_counter - 2
print(f'You made {loave_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs '
      f'and {budget:.2f}BGN left.')
