import os
os.system('clear')

class Player:
    def __init__(self, name, token):
       self.name = name
       self.token = token

    def player_name(self, name, token):
        return name, token

class Game:
    
    def board(self):
        # os.system('clear')
        print('\n##### LET\'S PLAY TIC-TAC-TOE #####\n')
        self.box = [' ', ' 1 ', ' 2 ', '3 ', ' 4 ', ' 5 ','6 ', ' 7 ', ' 8 ','9 ']
        print(f'  {self.box[1]}  |  {self.box[2]}  |  {self.box[3]}')
        print('---------------------')
        print(f'  {self.box[4]}  |  {self.box[5]}  |  {self.box[6]}')
        print('---------------------')
        print(f'  {self.box[7]}  |  {self.box[8]}  |  {self.box[9]}')
        print('\n')

    def move(self, box_num, token):
    #    token = self.box[box_num]
        self.box[box_num] = token


start = Game()

def refresh_screen():
    # os.system('clear')
    start.board()


while True:
    refresh_screen()
    
    print('Hello!  Welcome to Tic-Tac-Toe!')
    player1 = input('Player1, what is your name: ')
    player2 = input ('Player2, what is your name: ')


    p1_choice = int(input('What box do you want (1 - 9)? '))
    start.move(p1_choice, 'X')