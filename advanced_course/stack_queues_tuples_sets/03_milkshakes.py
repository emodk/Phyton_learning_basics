from collections import deque
chocolate = [int(el) for el in input().split(", ")]
milk = deque(int(el) for el in input().split(", "))
milkshakes_counter = 0
while len(chocolate) > 0 and len(milk) > 0:
    choco = chocolate.pop()
    milk_cup = milk.popleft()
    if choco <= 0:
        milk.appendleft(milk_cup)
        continue
    elif milk_cup <= 0:
        chocolate.append(choco)
        continue
    else:
        if choco == milk_cup:
            milkshakes_counter += 1
            if milkshakes_counter == 5:
                print("Great! You made all the chocolate milkshakes needed!")
                break
            else:
                continue
        else:
            milk.append(milk_cup)
            choco -= 5
            chocolate.append(choco)
if milkshakes_counter < 5:
    print("Not enough milkshakes.")
if len(chocolate) > 0:
    chocolate = ", ".join(str(el) for el in chocolate)
    print(f"Chocolate: {chocolate}")
else:
    print("Chocolate: empty")
if len(milk) > 0:
    milk = ", ".join(str(el) for el in milk)
    print(f"Milk: {milk}")
else:
    print("Milk: empty")
