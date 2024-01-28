text = input()
new_text = text[0]
for i in text:
    if i != new_text[-1]:
        new_text += i
print(new_text)
