card_per_player_string = input()
card_per_player_list = card_per_player_string.split(' ')
team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
game_termination = False
for element in card_per_player_list:
    if "A" in element:
        if element in team_a:
            team_a.remove(element)
    elif "B" in element:
        if element in team_b:
            team_b.remove(element)
    if (len(team_a) < 7) or (len(team_b) < 7):
        game_termination = True
        break
print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if game_termination:
    print('Game was terminated')
