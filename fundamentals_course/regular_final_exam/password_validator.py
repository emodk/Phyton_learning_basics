def make_upper(passwrd: str, index: int):
    new_passwrd = passwrd[:index] + passwrd[index].upper() + passwrd[index + 1:]
    return new_passwrd


def make_lower(passwrd: str, index: int):
    new_passwrd = passwrd[:index] + passwrd[index].lower() + passwrd[index + 1:]
    return new_passwrd


def insert(passwrd: str, char: str, index: int):
    if 0 <= index <= len(passwrd):
        new_passwrd = passwrd[:index].rstrip() + char + passwrd[index:]
        return new_passwrd
    else:
        return passwrd


def replace(passwrd: str, char: str, value: int):
    if char in passwrd:
        new_char = chr(ord(char) + value)
        new_passwrd = passwrd.replace(char, new_char)
        return new_passwrd
    else:
        return passwrd


password = input()
command = input()
while command != "Complete":
    command = command.split()
    if command[0] == "Make" and command[1] == "Upper":
        char_index = int(command[2])
        password = make_upper(password, char_index)
        print(password)
    elif command[0] == "Make" and command[1] == "Lower":
        char_index = int(command[2])
        password = make_lower(password, char_index)
        print(password)
    elif command[0] == 'Insert':
        char_index = int(command[1])
        ins_char = command[2]
        password = insert(password, ins_char, char_index)
        print(password)
    elif command[0] == "Replace":
        add_value = int(command[2])
        repl_char = command[1]
        password = replace(password, repl_char, add_value)
        print(password)
    elif command[0] == "Validation":
        upper_count = 0
        lower_count = 0
        digit_counter = 0
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        for symbol in password:
            value = ord(symbol)
            if value <= 47 or 58 <= value <= 64 or 91 <= value <= 94 or value == 96 or value >= 123:
                print("Password must consist only of letters, digits and _!")
                break
        for symbol in password:
            value = ord(symbol)
            if 65 <= value <= 90:
                upper_count += 1
        if upper_count == 0:
            print("Password must consist at least one uppercase letter!")
        for symbol in password:
            value = ord(symbol)
            if 97 <= value <= 122:
                lower_count += 1
        if lower_count == 0:
            print("Password must consist at least one lowercase letter!")
        for symbol in password:
            value = ord(symbol)
            if 48 <= value <= 57:
                lower_count += 1
        if lower_count == 0:
            print("Password must consist at least one digit!")
    command = input()
