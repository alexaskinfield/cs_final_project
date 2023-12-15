#def swedish_game(new_string):
#    new_string = ""
#    for letter in new_string:
#        if letter in ['a', 'e', 'i', 'o', 'u']:
#            new_string += letter
#        else:
#            new_string += letter
#            if ord('a') < - ord(letter) <= ord('e'):
#                if ord(letter) - ord('a') <= ('e') - ord(letter):
#                    new_string += 'a'
#                else:
#                    new_string += 'e'
#            elif ord('e') < ord(letter) < ord('i'):
#                if ord(letter) - ord('e') <= ord('i') - ord(letter):
#                    new_string += 'e'
#                else:
#                    new_string += 'i'
#            elif ord('i') < ord(letter) < ord('o'):
#               if ord(letter) - ord('i') <= ord('o') - ord(letter):
#                    new_string += 'i'
#                else:
#                    new_string += 'o'
#swedish_game(new_string)

#dic1 = {
#    '1': 'one',
#    '2': 'two',
#    '3': 'three'
#}

#dic2 = {
#    'one': '1',
#    'two': '2',
#    'three': '3'
#}

#dic3 = {}

#for key1 in dic1:
#    dic3[key1] = dic1[key1]

#for key2 in dic2:
#    dic3[key2] = dic2[key2]

#print(dic3)

def evaluate_hand(cards):
    card_values = {'A': 4, 'K': 3, 'Q': 2, 'J': 1}

    suit_info = {'C': {'length': 0, 'points': 0},
                 'D': {'length': 0, 'points': 0},
                 'H': {'length': 0, 'points': 0},
                 'S': {'length': 0, 'points': 0}}

    for card in cards:
        value, suit = card[:-1], card[-1]
        points = card_values.get(value, 0)

        suit_info[suit]['length'] += 1
        suit_info[suit]['points'] += points

    print("Cards Dealt points")
    for suit, info in suit_info.items():
        cards_in_suit = [card[:-1] for card in cards if card[-1] == suit]
        print(f"{suit} {' '.join(cards_in_suit)} {info['points']}")

    total_points = sum(info['points'] for info in suit_info.values())
    print(f"Total {total_points}")


# Sample session 1
cards_input_1 = input("Enter cards: ").upper()
evaluate_hand(cards_input_1)

# Sample session 2
cards_input_2 = input("Enter cards: ").upper()
evaluate_hand(cards_input_2)






