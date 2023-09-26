pattern_character_number = int(input())
for i in range(pattern_character_number + 1):
    print("* " * i)
for j in range(pattern_character_number - 1, 0, -1):
    print("* " * j)
