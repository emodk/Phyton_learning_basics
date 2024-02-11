number_of_usernames = int(input())
unique_usernames = set()
for _ in range(number_of_usernames):
    unique_usernames.add(input())
for username in unique_usernames:
    print(username)
