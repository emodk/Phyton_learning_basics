text = input()
encrypted_text = ""
for i in text:
    ch = ord(i) + 3
    if ch >= 128:
        encrypted_text += chr(127)
    else:
        encrypted_text += chr(ch)
print(encrypted_text)
