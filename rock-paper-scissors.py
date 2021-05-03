# This is a game of Rock, Paper, Scissors that took me forever to make.

import random

moves = ["rock", "paper", "scissors"]


# Parent Class - Player
class Player:
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


# Beats function to determine what move beats what
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Random Choice Player
class Random(Player):
    def move(self):
        return random.choice(moves)


# Human Player
class Human(Player):
    def move(self):
        human_move = input("Enter your move:\n").lower()
        while human_move not in moves:
            human_move = input("Incorrect value, \
                         please enter rock, paper or scissors:\n").lower()
        else:
            return human_move


# Reflect Player
class Reflect(Player):
    def __init__(self):
        Player.__init__(self)
        self.learned_move = None

    def move(self):
        if self.learned_move is None:
            return random.choice(moves)
        return self.learned_move

    def learn(self, my_move, their_move):
        self.learned_move = their_move


# Cycle Player
class Cycle(Player):
    def __init__(self):
        Player.__init__(self)
        self.counter = 0

    def move(self):
        round_move = moves[self.counter]
        if self.counter >= 2:
            self.counter = 0
        else:
            self.counter += 1
        return round_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2):
            self.p1_score += 1
            print(f"\n***PLAYER 1 WINS!*** \
                \nSCORE IS: P1= {self.p1_score}\
                P2= {self.p2_score}\n")

        elif beats(move2, move1):
            self.p2_score += 1
            print(f"\n***PLAYER 2 WINS!*** \
                \nSCORE IS: P1= {self.p1_score}\
                 P2= {self.p2_score}\n")

        else:
            print(f"\n***TIE GAME!*** \
                \nSCORE IS: P1= {self.p1_score} P2= {self.p2_score}\n")

    def play_game(self):
        print("WELCOME TO ROCK, PAPER, SCISSORS!\
            \n\nTo play, type your move and hit the ENTER key")
        for round in range(1, 6):
            print(f"\nRound {round}!")
            self.play_round()
        if self.p1_score > self.p2_score:
            print(f"***PLAYER 1 WINS!***\
                \nFinal score:P1= {self.p1_score} P2= {self.p2_score}")
        elif self.p1_score == self.p2_score:
            print("***TIE GAME - NO ONE WINS!***")
        else:
            print(f"***PLAYER 2 WINS!***\
                \nFinal score:P1= {self.p1_score} P2= {self.p2_score}")


# Play the game!
if __name__ == '__main__':
    player_choice = [Player(), Random(), Reflect(), Cycle()]
    game = Game(Human(), random.choice(player_choice))
    game.play_game()
