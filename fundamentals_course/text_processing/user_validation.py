def length_validation(name: str):
    if 3 <= len(name) <= 16:
        return True
    else:
        return False


def content_validation(name: str):
    name = name.lower()
    result = ''
    for i in name:
        if ord(i) > 122:
            result = False
            break
        elif 57 < ord(i) < 97 and i != "_":
            result = False
            break
        elif ord(i) < 48 and i != "-":
            result = False
            break
        else:
            result = True
    return result


usernames = input().split(', ')
for username in usernames:
    if length_validation(username) and content_validation(username):
        print(username)
