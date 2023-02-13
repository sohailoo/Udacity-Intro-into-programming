#!/usr/bin/env python3
import random
moves = ['rock', 'paper', 'scissors']


class Player:
    computer_move = None
    player_move = None

    def move(self):
        return 'rock'

    def learn(self, computer_move, player_move):
        self.player_move = player_move
        self.computer_move = computer_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        play = input("Rock, paper, scissors? ").lower()
        if play in moves:
            print(f'You played {play}.')
        else:
            print("Invalid input! Try again!")
            self.move()
        return play


class ReflectPlayer(Player):
    def move(self):
        if self.player_move is None:
            return random.choice(moves)
        else:
            return self.player_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.moves_size = len(moves)
        self.next_move_index = random.randrange(self.moves_size)

    def move(self):
        next_move = moves[self.next_move_index]
        self.next_move_index = (
            self.next_move_index + 1) % self.moves_size
        return next_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def results(self):
        if self.p1.score > self.p2.score:
            print("\n*** PLAYER ONE WON THE GAME!! *** ")
        elif self.p2.score > self.p1.score:
            print("\n*** PLAYER TWO WON THE GAME!! *** ")
        else:
            print(f"***Its a Tie, both players have a socre of {self.p1.score}"
                  "***")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Opponent played {move2}.")
        if beats(move1, move2):
            print("*** PLAYER ONE WINS! ***")
            self.p1.score += 1
        elif beats(move2, move1):
            print("*** PLAYER TWO WINS! ***")
            self.p2.score += 1
        else:
            print("*** TIE! ***")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Score: Player one {self.p1.score}, Player Two {self.p2.score}")

    def play_game(self):
        while True:
            print("*** Game start! ***")
            rounds_counts = int(input("How many rounds do you "
                                      "want to play ? (Enter a number) "))
            for round in range(rounds_counts):
                print(f"\nRound {round} --")
                self.play_round()
            self.results()
            again = input("Do you wish to play again ? (Yes/No) ").lower()
            if again == "no":
                print("Game over!\n")
                break
            elif again == "yes":
                reset = input("Do you wish to reset the scores ?"
                              " (Yes/No)").lower()
                if reset == "yes":
                    self.p1.score = 0
                    self.p2.score = 0
                else:
                    print("\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
