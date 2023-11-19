number_of_commands = int(input())
parking_dict = {}
for i in range(number_of_commands):
    command = input().split()
    username = command[1]
    if command[0] == "register":
        license_number = command[2]
        if username not in parking_dict.keys():
            parking_dict[username] = license_number
            print(f"{username} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_dict[username]}")
    if command[0] == "unregister":
        if username not in parking_dict.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_dict[username]
for key in parking_dict.keys():
    print(f"{key} => {parking_dict[key]}")
