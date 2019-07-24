# filename: tictactoe.py
import random

class Player:
    def __init__(self, name="", turn=1, token="X"):
        self.name = name
        self.turn = turn
        self.token = token

    def assign_player1(self):
        player1 = {}
        player1.update({"name": input("Player 1: What's your first name? ")})
        player1.update({"turn": random.randint(1, 2)})
        player1.update({"token": random.choice(["X", "O"])})
        return player1

    def assign_player2(self, player1):
        player2 = {}
        player2.update({"name": input("Player 2: What's your first name? ")})
        player2.update({"turn": 2 if player1.get("turn") == 1 else 1})
        player2.update({"token": "O" if player1.get("token") == "X" else "X"})
        return player2

player = Player()
player1 = player.assign_player1()
player2 = player.assign_player2(player1)
print(player1)
print(player2)


# class Game:
#     def __init__(self, board=""):
#         self.board = board
#
#     def __repr__(self, board=""):
#         self.board = "\n"
#         for i in range(6):
#             if i % 2==0:
#                 self.board += " " + "|" + " " + "|" + " " + "\n"
#         return self.board



    # def move(self, x, y, player):
    #
    #
    # def calc_winner():
    #
    #
    # def is_full():
    #
    #
    # def is_game_over():




# def main():
#



# board = Game()
#
# print(board.__repr__())
