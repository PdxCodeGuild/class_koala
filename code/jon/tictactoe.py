class Player():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def name(self, name):



class Game():
    def __init__(self):
        self = self

    def board(self):
        self.cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        print('  %s  |  %s  |  %s  ' %(self.cells[1], self.cells[2], self.cells[3]))
        print('------------------')
        print('  %s  |  %s  |  %s  ' %(self.cells[4], self.cells[5], self.cells[6]))
        print('------------------')
        print('  %s  |  %s  |  %s  ' %(self.cells[7], self.cells[8], self.cells[9]))

start = Game()
start.board()

