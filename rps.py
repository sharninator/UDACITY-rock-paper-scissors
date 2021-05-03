#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
import emoji

moves = ['rock', 'paper', 'scissors']

#what beats what function
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

"""The Player class is the parent class for all of the Players
in this game"""

#general Player class plays rock only
class Player:
    my_move= None
    their_move= None
    
    def move(self):
        return 'rock'
    
    def learn(self, my_move, their_move):
        pass

#random player makes mandom choice moves
class Random(Player):

    def move(self):
        return random.choice(moves)

#human player - human input!
class Human(Player):
    
    def move(self):
      human_move=  input("Enter your move:\nrock, paper or scissors? ")
      return human_move

# # reflect player - plays your previous move
class Reflect(Player):

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move
    
    def learn(self, my_move, their_move):
        self.their_move

#cycle player - cycles through the moves
class Cycle(Player):
    def move(self):

#game glass
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score=0
        self.p2_score=0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            self.p1_score +=1
            print(f"***PLAYER 1 WINS!*** \nSCORE IS: P1= {self.p1_score} P2= {self.p2_score}\n")

        elif beats(move2, move1):
            self.p2_score +=1
            print(f"***PLAYER 2 WINS!*** \nSCORE IS: P1= {self.p1_score} P2= {self.p2_score}\n")

        else:
            print(f"***TIE GAME!*** \nSCORE IS: P1= {self.p1_score} P2= {self.p2_score}\n")

    def play_game(self):
        print("Game start!\n")
        for round in range(1,4):
            print(f"Round {round}:")
            self.play_round()
        print(f"Game over! \nFinal score:P1= {self.p1_score} P2= {self.p2_score}")

# i assume this runs the program?
# if __name__ == '__main__':
#     player_choice= [Random(), Player()]
#     game = Game(Human(), random.choice(player_choice))
#     game.play_game()

# game that will play random v rock. 
# if __name__ == '__main__':
#     game = Game(Random(), Player())
#     game.play_game()

# game that will play 2 random
# if __name__ == '__main__':
#     game = Game(Random(), Random())
#     game.play_game()

human player and Random
if __name__ == '__main__':
    game = Game(Human(), Reflect())
    game.play_game()