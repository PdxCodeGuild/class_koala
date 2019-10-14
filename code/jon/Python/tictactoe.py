import os
os.system("clear")

class Board():
    def __init__(self):
        self.box = [' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ']
  
    def display(self):
        print(f'  {self.box[1]}  |  {self.box[2]}  |  {self.box[3]}')
        print('------------------')
        print(f'  {self.box[4]}  |  {self.box[5]}  |  {self.box[6]}')
        print('------------------')
        print(f'  {self.box[7]}  |  {self.box[8]}  |  {self.box[9]}')
        print('\n')

    def update_box(self, box_num, token):
        if self.box[box_num] == " ":
            self.box[box_num] = token

    def is_winner(self, player):
        #check row winner
        if self.box[1] == player and self.box[2] == player and self.box[3] == player:
            return True
        elif self.box[4] == player and self.box[5] == player and self.box[6] == player:
            return True
        elif self.box[7] == player and self.box[8] == player and self.box[9] == player:
            return True
        #check column winner
        if self.box[1] == player and self.box[4] == player and self.box[7] == player:
            return True
        elif self.box[2] == player and self.box[5] == player and self.box[8] == player:
            return True
        elif self.box[3] == player and self.box[6] == player and self.box[9] == player:
            return True
        #check diagonal winner
        if self.box[1] == player and self.box[5] == player and self.box[9] == player:
            return True
        elif self.box[3] == player and self.box[5] == player and self.box[7] == player:
            return True
        return False

    def check_if_tie(self):
        used_box = 0
        for box in self.box:
            if box != " ":
                used_box += 1
        if used_box == 9:
            return True
        else:
            return False


    def reset(self): 
        self.box = [' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ',' ']



board = Board()

def print_header():
    print('Hello!  Welcome to Tic-Tac-Toe!')

def refresh():
    os.system("clear") 

    print_header()

    board.display()


while True:
    refresh()

    #get x input
    x_choice = int(input('X > Please choose box 1 - 9: ' ))

    #update board

    board.update_box(x_choice, "X")

    #refresh screen
    refresh()

    #check if X won
    if board.is_winner("X"):
        print('X Wins')
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again == 'y':
            board.reset()
            continue
        else:
            break
    
    #check if a tie
    if board.check_if_tie():
        print('Tie Game!')
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again == 'y':
            board.reset()
            continue
        else:
            break

    #get O input
    o_choice = int(input('O > Please choose box 1 - 9: ' ))

    #update board

    board.update_box(o_choice, "O")

    #check if O won
    if board.is_winner("O"):
        print('O Wins')
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again == 'y':
            board.reset()
            continue
        else:
            break

    #check if a tie
    if board.check_if_tie():
        print('Tie Game!')
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again == 'y':
            board.reset()
            continue
        else:
            break
