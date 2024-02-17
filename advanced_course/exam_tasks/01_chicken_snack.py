from collections import deque
money = [int(el) for el in input().split()]
food_price = deque(int(el) for el in input().split())
eating_counter = 0
while len(money) > 0 and len(food_price) > 0:
    current_portion_money = money.pop()
    current_price = food_price.popleft()
    if current_portion_money > current_price:
        difference = current_portion_money - current_price
        if len(money) > 0:
            next_portion_money = money.pop()
            next_portion_money += difference
        else:
            next_portion_money = difference
        money.append(next_portion_money)
        eating_counter += 1
        continue
    elif current_portion_money == current_price:
        eating_counter += 1
        continue
if eating_counter >= 4:
    print(f"Gluttony of the day! Henry ate {eating_counter} foods.")
elif 1 <= eating_counter < 4:
    if eating_counter == 1:
        print(f"Henry ate: {eating_counter} food.")
    else:
        print(f"Henry ate: {eating_counter} foods.")
else:
    print("Henry remained hungry. He will try next weekend again.")
