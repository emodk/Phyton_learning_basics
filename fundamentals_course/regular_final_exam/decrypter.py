number_of_messages = int(input())
for i in range(number_of_messages):
    message = input().split(":")
    tag = message[0]
    text = message[1].lstrip()
    pipe_counter = 0
    left_bracket = 0
    right_bracket = 0
    decryption = ""
    for j in text:
        if j == '[':
            left_bracket += 1
        if j == ']':
            right_bracket += 1
        if j == '|':
            pipe_counter += 1
    if len(tag) < 5:
        print("Valid message not found!")
    elif ord(tag[0]) != ord(tag[-1]):
        if ord(tag[0]) != 36 or ord(tag[0]) != 37:
            print("Valid message not found!")
    elif text[-1] != '|':
        print("Valid message not found!")
    elif pipe_counter != 3 or right_bracket != 3 or left_bracket != 3:
        print("Valid message not found!")
    else:
        tag = tag[1:len(tag) - 1]
        text = text.replace('[', '')
        text = text.replace(']', '')
        text = text.replace('|', " ")
        text = text.split()
        for k in text:
            decryption += chr(int(k))
        print(f"{tag}: {decryption}")
