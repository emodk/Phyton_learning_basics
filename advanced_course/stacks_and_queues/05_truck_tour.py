from collections import deque
number_of_pumps = int(input())
pump_parameter_deque = deque()
possible_first_pump_deque = deque()
consumption_per_kilometer = 1
balance = 0
for pump_index in range(number_of_pumps):
    litters, kilometers = input().split()
    litters = int(litters)
    kilometers = int(kilometers)
    pump_parameter = litters - kilometers * consumption_per_kilometer
    if pump_parameter > 0:
        possible_first_pump_deque.append(pump_index)
    pump_parameter_deque.append(pump_parameter)
for _ in range(len(possible_first_pump_deque)):
    current_pump_parameter_queue = pump_parameter_deque.copy()
    start_pump_index = possible_first_pump_deque.popleft()
    for _ in range(start_pump_index):
        current_pump_parameter_queue.append(current_pump_parameter_queue.popleft())
    for current_start_pump in range(number_of_pumps):
        balance += current_pump_parameter_queue.popleft()
        if balance < 0:
            break
    if balance >= 0:
        print(start_pump_index)
        exit()
    balance = 0
print("No starting pump available to ensure tour finishing.")
