def count_check(left_part, right_part, symbol):
    count = 6
    for i in range(7, 11):
        if (i * symbol) in left_part and (i * symbol) in right_part:
            count += 1
    return count


def ticket_check(ticket):
    winning_symbols = "@#$^"
    if len(ticket) != 20:
        print('invalid ticket')
    elif ticket[0] * 20 == ticket and ticket[0] in winning_symbols:
        print(f"ticket \"{ticket}\" - {int(len(ticket) / 2)}{ticket[0]} Jackpot!")
    else:
        left_part = ticket[0:10]
        right_part = ticket[10:]
        count = 0
        symbol = ''

        if (6 * '@') in left_part and (6 * '@') in right_part:
            symbol = '@'
            count = count_check(left_part, right_part, symbol)
        elif (6 * '#') in left_part and (6 * '#') in right_part:
            symbol = '#'
            count = count_check(left_part, right_part, symbol)
        elif (6 * '$') in left_part and (6 * '$') in right_part:
            symbol = '$'
            count = count_check(left_part, right_part, symbol)
        elif (6 * '^') in left_part and (6 * '^') in right_part:
            symbol = '^'
            count = count_check(left_part, right_part, symbol)
        else:
            print(f'ticket "{ticket}" - no match')

        if count >= 6:
            print(f'ticket "{ticket}" - {count}{symbol}')


def winning_ticket(data):
    for ticket in data:
        ticket_check(ticket)


text = input()
info = [x.strip() for x in text.split(',')]
winning_ticket(info)
