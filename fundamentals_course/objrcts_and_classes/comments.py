class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


# Test code

comment = Comment('Emil', 'The best movie!')
print(comment.username)
print(comment.content)
print(comment.likes)
reader_name = input()
comment.username = reader_name
likes_input = input("Do you agree (Y/N): ",)
likes_input.upper()
if likes_input == 'Y':
    comment.likes += 1
elif likes_input != 'N':
    print('Incorrect answer!')
    exit()
print(comment.username)
print(comment.content)
print(comment.likes)
