key_number = int(input())
number_of_lines = int(input())
decrypted_string = ""
for i in range(1, number_of_lines + 1):
    character = input()
    character_value = ord(character)
    decrypted_value = character_value + key_number
    decrypted_character = chr(decrypted_value)
    decrypted_string += decrypted_character
print(decrypted_string)
