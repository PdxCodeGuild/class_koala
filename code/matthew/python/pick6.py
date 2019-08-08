# filename: pick6.py
import random

# generates six random numbers between 1 - 99, stores all of them in a list and then returns said list
def pick6():
    random_num_list = []
    for num in range(6):
        random_num_list.append(random.randint(1, 99))
    return random_num_list

# for the length of the list, compares the equal indices of the two lists - if same, increases matches by 1, then moves to the next index position - returns total matches
def num_matches(winning_numbers, ticket):
    matches = 0
    index = 0
    for i in range(len(winning_numbers)):
        if winning_numbers[i] == ticket[i]:
            matches += 1
        index += 1
    return matches

print("") # adds a blank line separator to program
tickets_to_test = int(input("How many lottery tickets would you like to purchase? ")) # determines number of for loops

winning_numbers = pick6() # creates the winning ticket
zero_tupling = (0, 0, 0, 0, 0, 0, 0, 0, 0)
# ^ packs and unpacks tuple to set all balances of below to zero:
single_matches, double_matches, triple_matches, quadruple_matches, quintuple_matches, sextuple_matches, balance, tickets_purchased, earnings = zero_tupling

for loops in range(tickets_to_test): # cycles through x number of times
    balance -= 2 # subtracts cost of ticket - $2.00
    tickets_purchased += 1 # increased tickets purchased by one
    ticket = pick6() # generates a customer ticket
    total_matches = num_matches(winning_numbers, ticket) # stores number of matches

    # compares ticket matches - based on result, increases balance, increases earnings and tallies total number of each match set
    if total_matches == 1:
        balance += 4
        earnings += 4
        single_matches += 1
    elif total_matches == 2:
        balance += 7
        earnings += 7
        double_matches += 1
    elif total_matches == 3:
        balance += 100
        earnings += 100
        triple_matches += 1
    elif total_matches == 4:
        balance += 50000
        earnings += 50000
        quadruple_matches += 1
    elif total_matches == 5:
        balance += 1000000
        earnings += 1000000
        quintuple_matches += 1
    elif total_matches == 6:
        balance += 25000000
        earnings += 25000000
        sextuple_matches += 1

expenses = tickets_purchased * 2 # total expenditures
roi = (earnings - expenses) / expenses # calculates ROI

print(f"\n***** Match Results *****\nTickets with one match: {single_matches}\nTickets with two matches: {double_matches}\nTickets with three matches: {triple_matches}\nTickets with four matches: {quadruple_matches}\nTickets with five matches: {quintuple_matches}\nTickets with six matches: {sextuple_matches}")

print(f"\n***** Final Results *****\nNumber of Tickets Purchased: {tickets_purchased}\nAmount Won: ${earnings}\nAmount Spent: ${expenses}\nReturn on Investment: {roi}\nFinal Balance: ${balance}\n")
