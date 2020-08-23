from const import suits, numbers, combinations


def check_combinations(cards):

    cards.sort(key=lambda x: int(x), reverse=True)
    numbers_player_main = [card.number for card in cards]
    suits_player = [card.suit for card in cards]

    flush_royal = check_flush_royal(cards)
    if flush_royal:
        return flush_royal

    straight_flush = check_straight_flush(cards)
    if straight_flush:
        return straight_flush

    four = check_four(cards, list(numbers_player_main))
    if four:
        return four

    full_house = check_full_house(cards, list(numbers_player_main))
    if full_house:
        return full_house

    flush = check_flush(cards, suits_player)
    if flush:
        return flush

    straight = check_straight(cards, list(numbers_player_main))
    if straight:
        return straight

    three = check_three(cards, list(numbers_player_main))
    if three:
        return three

    two_pairs = check_two_pairs(cards, list(numbers_player_main))
    if two_pairs:
        return two_pairs

    pair = check_pair(cards,list(numbers_player_main))
    if pair:
        return pair

    return {'combination_name': 'no combination',
            'cards_for_combination': cards[:5]}


# Check Flush Royal
def check_flush_royal(cards):

    for x in suits.values():
        if all([any([x == card.suit and y == card.number for card in cards]) for y in numbers[-5:]]):
            return {'combination_name': 'flush_royal',
                    'cards_for_combination': [[card for card in cards if x == card.suit and y == card.number][0]
                                              for y in numbers[-5:]]}


# Check Straight Flush
def check_straight_flush(cards):

    for x in suits.values():
        for i in range(len(numbers) - 4):
            if all([any([x == card.suit and y == card.number for card in cards]) for y in numbers[i:i + 5]]):
                return {'combination_name': 'straight_flush',
                        'cards_for_combination': [[card for card in cards if x == card.suit and y == card.number][0]
                                                  for y in numbers[i:i + 5]][::-1]}


# Check Four
def check_four(cards, numbers_player):
    for x in reversed(numbers):
        if 4 == numbers_player.count(x):
            return {'combination_name': 'four',
                    'cards_for_combination': [cards[i] for i in range(len(numbers_player))
                                              if numbers_player[i] == x]}


# Check Full House
def check_full_house(cards, numbers_player):

    three = False
    two = False
    data1 = []
    data2 = []

    for x in numbers:
        if 3 == numbers_player.count(x):
            three = True
            data1 = [card for card in cards if card.number == x][:3]

            numbers_player.remove(x)
        elif 2 == numbers_player.count(x):
            two = True
            data2 = [card for card in cards if card.number == x][:3]
            numbers_player.remove(x)

    if two and three:
        return {'combination_name': 'full_house',
                'cards_for_combination': data1 + data2}


# Check Flush
def check_flush(cards, suits_player):
    for x in suits.values():
        if 5 == suits_player.count(x):
            return {'combination_name': 'flush',
                    'cards_for_combination': [cards[i] for i in range(len(suits_player))
                                              if suits_player[i] == x]}


# Check Straight
def check_straight(cards, numbers_player):

    for i in range(len(numbers), 4, -1):
        if all([y in numbers_player for y in numbers[i - 5:i]]):

            return {'combination_name': 'straight',
                    'cards_for_combination': [[card for card in cards if card.number == y][0]
                                              for y in numbers[i - 5:i]][::-1]}


# Check Three
def check_three(cards, numbers_player):
    for x in reversed(numbers):
        if 3 == numbers_player.count(x):
            return {'combination_name': 'three',
                    'cards_for_combination': [cards[i] for i in range(len(numbers_player)) if numbers_player[i] == x]}


# Check Two Pairs
def check_two_pairs(cards, numbers_player):

    two = False
    two1 = False
    data1 = []
    data2 = []

    for x in reversed(numbers):
        if 2 == numbers_player.count(x):
            if two and two1:
                return {'combination_name': 'two_pairs',
                        'cards_for_combination': data1 + data2}
            elif two:
                two1 = True
                data2 = [card for card in cards if card.number == x]
            else:
                two = True
                data1 = [card for card in cards if card.number == x]

            numbers_player.remove(x)

    if two and two1:
        return {'combination_name': 'two_pairs',
                'cards_for_combination': data1 + data2}


# Check Pair
def check_pair(cards, numbers_player):
    for x in reversed(numbers):
        if 2 == numbers_player.count(x):
            return {'combination_name': 'pair',
                    'cards_for_combination': [cards[i] for i in range(len(numbers_player)) if numbers_player[i] == x]}


# Change Winner
def change_winner(one_player, two_player):
    if combinations[one_player['combination_name']] > combinations[two_player['combination_name']]:
        return f'FIRST PLAYER WIN WITH {one_player["combination_name"]} {one_player["cards_for_combination"]}'
    elif combinations[one_player['combination_name']] < combinations[two_player['combination_name']]:
        return f'SECOND PLAYER WIN WITH {two_player["combination_name"]} {two_player["cards_for_combination"]}'
    else:
        for i in range(len(one_player["cards_for_combination"])):
            if one_player["cards_for_combination"][i] > two_player["cards_for_combination"][i]:
                return f'FIRST PLAYER WIN WITH {one_player["combination_name"]}' \
                       f' {one_player["cards_for_combination"]} BECOUSE IMPORTANT CARD'
            elif one_player["cards_for_combination"][i] < two_player["cards_for_combination"][i]:
                return f'SECOND PLAYER WIN WITH {two_player["combination_name"]}' \
                       f' {two_player["cards_for_combination"]} BECOUSE IMPORTANT CARD'
        return 'DRAW'
