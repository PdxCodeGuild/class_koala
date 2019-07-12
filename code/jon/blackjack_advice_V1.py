# blackjack_advice Version 1

card_values = {'a': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 10, 'q': 10, 'k': 10, '0': 0}

def add_cards(a, b, c):
    total = card_values[a] + card_values[b] + card_values[c]
    return total

first_card = input('What is your first card? ').lower()
second_card = input('What is your second card? ').lower()
third_card = input('What is your third card? ').lower()

card_total = add_cards(first_card, second_card, third_card)

if card_total < 17:
    print(f'Total is {card_total}.  You should Hit')
elif card_total >= 17 and card_total < 21:
    print(f'Total is {card_total}.  You should Stay!')
elif card_total == 21:
    print(f'Total is {card_total}.  BlackJack!')
else:
    print(f'Total is {card_total}.  Already Busted!')