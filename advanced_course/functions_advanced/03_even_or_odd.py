def even_odd(*args):
    filtered = []
    new_arg = [el for el in args]
    command = new_arg.pop()
    if command == "odd":
        for el in new_arg:
            if el % 2 != 0:
                filtered.append(el)
    elif command == "even":
        for el in new_arg:
            if el % 2 == 0:
                filtered.append(el)
    return filtered


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
