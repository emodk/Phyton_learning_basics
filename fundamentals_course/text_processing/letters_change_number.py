text = input().split()
total_result = 0
for i in text:
    result = 0
    first_letter = i[0]
    last_letter = i[-1]
    i = i.replace(first_letter, '')
    i = i.replace(last_letter, '')
    number = int(i)
    if first_letter.isupper():
        result = number / (ord(first_letter) - 64)
    else:
        result = number * (ord(first_letter) - 96)
    if last_letter.isupper():
        result -= (ord(last_letter) - 64)
    else:
        result += (ord(last_letter) - 96)
    total_result += result
print(f"{total_result:.2f}")
