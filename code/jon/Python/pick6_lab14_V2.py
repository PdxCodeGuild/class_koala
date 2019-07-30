import random

def pick6():
    '''Picks 6 random numbers between 1 and 99'''
    i = 0
    ticket = []
    while i < 6:
        nums = random.randint(1,99)
        ticket.append(nums)
        i += 1
    return ticket

def num_matches(winning, ticket):
    '''Checks to see if there are any matches'''
    matches = 0
    payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
    for i in range(len(ticket)):
        if winning[i] == ticket[i]:
            matches += 1

    if matches > 0:
        print(winning)
        print(ticket)
        print('You won:$ ', payout[matches])
    print('You won a total of: ', )
    return payout[matches]
    
def play_lottery():

    winning_ticket = pick6()
    spent = 0
    balance = 0

    for i in range(100000):
        ticket = pick6()
        spent -= 2
        balance -= 2
        payout = num_matches(winning_ticket, ticket)
        balance += payout
    roi = float((payout - spent)/spent)
    print('Balance: ', balance)
    print('ROI: ', roi)
    

play_lottery()