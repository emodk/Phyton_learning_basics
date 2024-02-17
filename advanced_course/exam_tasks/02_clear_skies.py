space_dimension = int(input())
space = []
jet_row = 0
jet_col = 0
armor = 300
enemy_counter = 0
for i in range(space_dimension):
    space.append([])
    row = input()
    col = 0
    for j in row:
        space[i].append(j)
        col += 1
        if j == "J":
            jet_row = i
            jet_col = col - 1
        elif j == "E":
            enemy_counter += 1
while armor > 0 and enemy_counter > 0:
    command = input()
    new_row = 0
    new_col = 0
    if command == "up":
        new_row = jet_row - 1
        new_col = jet_col
    elif command == "down":
        new_row = jet_row + 1
        new_col = jet_col
    elif command == "right":
        new_row = jet_row
        new_col = jet_col + 1
    elif command == "left":
        new_row = jet_row
        new_col = jet_col - 1
    space_condition = space[new_row][new_col]
    if space_condition == "R":
        armor = 300
    elif space_condition == "E":
        enemy_counter -= 1
        if enemy_counter > 0:
            armor -= 100
    space[new_row][new_col] = "J"
    space[jet_row][jet_col] = "-"
    jet_row = new_row
    jet_col = new_col
if enemy_counter == 0:
    print("Mission accomplished, you neutralized the aerial threat!")
elif armor == 0:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jet_row}, {jet_col}]!")
for i in range(space_dimension):
    print("".join(space[i]))
