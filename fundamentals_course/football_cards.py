card_per_player_string = input()
card_per_player_list = card_per_player_string.split(' ')
cards_team_a = []
cards_team_b = []
for element in card_per_player_list:
    if "A" in element:
        if element not in cards_team_a:
            cards_team_a.append(element)
    elif "B" in element:
        if element not in cards_team_a:
            cards_team_b.append(element)
print(f'Team A - {11 - len(cards_team_a)}; Team B - {11 - len(cards_team_b)}')
if (len(cards_team_a) > 4) or (len(cards_team_b) > 4):
    print('Game was terminated')
