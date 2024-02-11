from collections import deque
init_string = input()
first_half_string = deque()
second_half_string = list()
for element in range(len(init_string)):
    if element < len(init_string) / 2:
        first_half_string.append(init_string[element])
    else:
        second_half_string.append(init_string[element])
if len(first_half_string) != len(second_half_string):
    print("NO")
    exit()
for _ in range((len(first_half_string) // 2)):
    a = first_half_string.popleft()
    b = first_half_string.popleft()
    c = second_half_string.pop()
    d = second_half_string.pop()
    if a == b and c == d:
        if ord(a) != (ord(c) - 2):
            if ord(a) != (ord(c) - 1):
                print('NO')
                exit()
        if ord(b) != (ord(d) - 2):
            if ord(b) != (ord(d) - 1):
                print('NO')
                exit()
    else:
        if ord(a) != (ord(b) - 2) and ord(a) != (ord(b) - 1):
            if ord(a) != (ord(c) - 2):
                if ord(a) != (ord(c) - 1):
                    print('NO')
                    exit()
            if ord(b) != (ord(d) - 2):
                if ord(b) != (ord(d) - 1):
                    print('NO')
                    exit()
        else:
            if ord(d) != (ord(c) - 2):
                if ord(d) != (ord(c) - 1):
                    print('NO')
                    exit()
if len(first_half_string) != 0:
    a = first_half_string.popleft()
    c = second_half_string.pop()
    if ord(a) != (ord(c) - 2):
        if ord(a) != (ord(c) - 1):
            print('NO')
            exit()
print("YES")
