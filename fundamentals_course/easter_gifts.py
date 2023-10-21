gifts_string = input()
gift_list = gifts_string.split(' ')
none_counter = 0
while True:
    command = input()
    if command == "No Money":
        break
    command_list = command.split(' ')
    if ("OutOfStock" in command_list) and (command_list[1] in gift_list):
        none_counter = gift_list.count(command_list[1])
        for i in range(none_counter):
            gift_list.remove(command_list[1])
    elif "Required" in command_list:
        i = int(command_list[2])
        gift_list.insert(i, command_list[1])
    elif "JustInCase" in command_list:
        gift_list[-1] = command_list[1]
print(" ".join(gift_list))
