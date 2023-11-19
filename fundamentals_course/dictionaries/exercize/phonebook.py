phonebook = {}
while True:
    contact = input()
    if "-" not in contact:
        break
    else:
        contact = contact.split('-')
        phonebook[contact[0]] = contact[1]
number_of_people_search = int(contact)
for i in range(number_of_people_search):
    person = input()
    if person not in phonebook.keys():
        print(f'Contact {person} does not exist.')
    else:
        phone = phonebook[person]
        print(f'{person} -> {phone}')
