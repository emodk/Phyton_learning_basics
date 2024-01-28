text = input()
for i in range(len(text)):
    if text[i] == ":":
        emoticon = ":" + text[i + 1]
        print(emoticon)
