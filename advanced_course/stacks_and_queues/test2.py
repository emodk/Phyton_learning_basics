text = tuple(el for el in input())
symbol_dict = {}
for symbol in text:
    if symbol not in symbol_dict:
        symbol_dict[symbol] = 0
    symbol_dict[symbol] += 1
print(symbol_dict)
print(sorted(symbol_dict.values()))
sorted_sym_dict = dict(sorted(symbol_dict.items()))
print(sorted_sym_dict)
