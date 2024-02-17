from collections import deque
expression = deque(input().split())
buffer_queue = deque()
result = 0
for _ in range(len(expression)):
    a = expression.popleft()
    if a != "+" and a != "-" and a != "*" and a != "/":
        a = int(a)
        buffer_queue.append(a)
    else:
        if a == "-":
            result = buffer_queue.popleft()
            for _ in range(len(buffer_queue)):
                result -= buffer_queue.popleft()
            buffer_queue.append(result)
        elif a == "+":
            result = buffer_queue.popleft()
            for _ in range(len(buffer_queue)):
                result += buffer_queue.popleft()
            buffer_queue.append(result)
        elif a == "*":
            result = buffer_queue.popleft()
            for _ in range(len(buffer_queue)):
                result *= buffer_queue.popleft()
            buffer_queue.append(result)
        elif a == "/":
            result = buffer_queue.popleft()
            for _ in range(len(buffer_queue)):
                result //= buffer_queue.popleft()
            buffer_queue.append(result)
print(result)
