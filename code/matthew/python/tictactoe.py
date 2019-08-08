# filename: tictactoe.py
import random

class Player:
    def __init__(self, name="", turn=1, token="X"):
        self.name = name
        self.turn = turn
        self.token = token

    def assign_player1(self):
        """assigns attributes to Player 1 by accepting name as input, randomly assigning Turn #1 or #2 and randomly assigning their token character for the game"""
        player1 = {}
        player1.update({"name": input("Player 1: What's your first name? ")})
        player1.update({"turn": random.randint(1, 2)})
        player1.update({"token": random.choice(["X", "O"])})
        return player1

    def assign_player2(self, player1):
        """assigns attributes to Player 2 by accepting name as input, then assigning turn and token based on the opposite of that already assigned to Player 1"""
        player2 = {}
        player2.update({"name": input("Player 2: What's your first name? ")})
        player2.update({"turn": 2 if player1.get("turn") == 1 else 1})
        player2.update({"token": "O" if player1.get("token") == "X" else "X"})
        return player2


class Game:
    def __init__(self, board=""):
        self.board = board

    def __repr__(self):
        self.board = ""
        pos = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.board += (pos[0] + "|" + pos[1] + "|" + pos[2] + "\n")
        self.board += (pos[3] + "|" + pos[4] + "|" + pos[5] + "\n")
        self.board += (pos[6] + "|" + pos[7] + "|" + pos[8] + "\n")
        return self.board

    def move(self, board, player, x=0, y=0):
        self.board = board
        self.player = player
        self.x = x
        self.y = y
        if self.y == 0:
            self.board.replace(pos[self.x], "X")
        elif self.y == 1:
            self.board.replace(pos[self.x+3], "X")
        elif self.y == 2:
            self.board.replace(pos[self.x+6], "X")
        return self.board




def main():
    player = Player()
    game = Game()
    board = game.__repr__()
    print("\nLet's play Tic-Tac-Toe!\n")
    player1 = player.assign_player1()
    player2 = player.assign_player2(player1)
    print("\nHere's the board!\n")
    print(board)
    if player1.get("turn") == 1:
        print(player1.get("name") + ", you're up first! Your token will be " + player1.get("token") + "\n")
        player_current = player1
    elif player2.get("turn") == 1:
        print(player2.get("name") + ", you're up first! Your token will be " + player2.get("token") + "\n")
        player_current = player2
    while True:
        print("Note: (x) is horizontal from 0-2, (y) is vertical from 0-2 ")
        x = input("Please select the row (x) to place the next token: ")
        y = input("Please select the column (y): ")
        game.move(board, player_current, x, y)
        print("\n" + board)
        break



main()
