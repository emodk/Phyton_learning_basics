text = tuple(el for el in input())
symbol_dict = {}
for symbol in text:
    if symbol not in symbol_dict:
        symbol_dict[symbol] = 0
    symbol_dict[symbol] += 1
sorted_sym_dict = dict(sorted(symbol_dict.items()))
for key, value in sorted_sym_dict.items():
    print(f"{key}: {value} time/s")
