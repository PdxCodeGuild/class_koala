
cardValue = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "none":0}

print("Welcome to Blackjack Advisor.\n I can help you decide to hit or stay.\n")

card1 = input("Please enter your first card. (A/J/Q/K/1-9)\n")
card2 = input("Please enter your second card.\n")
card3 = input("Please enter your third card. If none type 'none'.\n")
total = cardValue[card1] + cardValue[card2] + cardValue[card3]
if total < 17:
    print(f"{total} hit")
elif total >= 17 and total <21:
    print(f"{total} stay")
elif total == 21:
    print(f"{total} Blackjack!")
else:
    print(f"{total} already busted")