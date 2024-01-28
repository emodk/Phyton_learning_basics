from collections import deque
food_quantity = int(input())
max_order = 0
queue = deque()
orders = input().split()
for el in orders:
    el = int(el)
    queue.append(el)
    if el > max_order:
        max_order = el
while len(queue) != 0:
    food_order = queue[0]
    if food_order <= food_quantity:
        queue.popleft()
        food_quantity -= food_order
        # if food_order > max_order:
        #     max_order = food_order
    else:
        print(max_order)
        orders_in_string = " ".join(str(el) for el in queue)
        print(f"Orders left: {orders_in_string}")
        exit()
print(max_order)
print("Orders complete")
