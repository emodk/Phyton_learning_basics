tickets_data = input().replace(" ", "")
tickets = tickets_data.split(",")
winning_symbol = ['@', '#', '$', '^']
for ticket in tickets:
    winning_symbol_counter = 0
    lack_counter = 0
    first_half_ticket = ticket[:10]
    if len(ticket) == 20:
        for symbol in winning_symbol:
            if symbol in first_half_ticket:
                while symbol in first_half_ticket:
                    winning_symbol_counter += 1
                    first_half_ticket = first_half_ticket.replace(symbol, '', 1)
                if 6 <= winning_symbol_counter <= 10:
                    for i in range(winning_symbol_counter, 5, -1):
                        winning_combination = symbol * i
                        if (winning_combination in ticket[10:]
                                and winning_combination in ticket[:10]):
                            if i == 10:
                                print(f'ticket "{ticket}" - {i}{symbol} Jackpot!')
                                break
                            elif i < 10:
                                print(f'ticket "{ticket}" - {i}{symbol}')
                                break
                        else:
                            print(f'ticket "{ticket}" - no match')
                else:
                    print(f'ticket "{ticket}" - no match')

            else:
                lack_counter += 1
                if lack_counter == 4:
                    print(f'ticket "{ticket}" - no match')
    else:
        print('invalid ticket')
