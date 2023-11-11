cards_list = input().split(', ')
actions = int(input())

def add(add_card):
    if add_card in cards_list:
        print('Card is already in the deck')
    else:
        cards_list.append(add_card)
        print("Card successfully added")
def remove(removed_card):
    if removed_card not in cards_list:
        print('Card not found')
    else:
        cards_list.remove(remove_card)
        print("Card successfully removed")


def remove_card(from_index):
    if 0 <= from_index <= len(cards_list):
        cards_list.pop(from_index)
        print("Card successfully removed")
    else:
        print('Index out of range')

def insert_card(card_index, card):
    if 0 <= card_index <= len(cards_list):
        if card in cards_list:
            print('Card is already added')
        else:
            cards_list.insert(card_index, card)
            print("Card successfully added")
    else:
        print('Index out of range')

for i in range(1, actions + 1):
    command_list = input().split(', ')
    if command_list[0] == 'Add':
        add(command_list[1])
    elif command_list[0] == 'Remove':
        remove(command_list[1])
    elif command_list[0] == 'Remove At':
        remove_card(int(command_list[1]))
    elif command_list[0] == 'Insert':
        insert_card(int(command_list[1]), command_list[2])
print(", ".join(cards_list))
