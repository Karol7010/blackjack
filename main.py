import random
import os
import time

class card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
    def __repr__(self):
        return (str(self.value) + "_" + str(self.color))



class deck:
    def __init__(self):
        self.cards = []

    def new_deck(self, jokers = False):
        for i in ['hearts','diamonds','spades','clubs']:
            for j in ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']:
                card_name = i+str(j)
                card_name = card(j, i)
                self.cards.append(card_name)
        if jokers:
            joker = card('joker', 'joker')
            self.cards.append(joker)
            self.cards.append(joker)

    def __sub__(self, other):
        self.cards.remove(other)


class player():
    def __init__(self, name):
        self.cards = []
        self.score = 0
        self.name = name
        self.loser = False
        self.stand = False
    def start(self, cards_in_deck):
        self.hit(cards_in_deck)
        self.hit(cards_in_deck)
        self.calc_score()
        print(f"You've drawned your first two cards: {self.cards}, you have {self.score} points")
    def calc_score(self):
        self.score = 0
        for i in self.cards:
            if type(i.value) == type(8):
                self.score += i.value
            if i.value in ['jack', 'queen', 'king']:
                self.score += 10
            if i.value == 'ace':
                temp = self.score
                if temp + 10 > 21:
                    self.score += 1
                else:
                    self.score += 10
    def hit(self, cards_in_deck):
        i = random.randint(0,len(cards_in_deck))
        card_drawed = cards_in_deck[i]
        cards_in_deck.remove(card_drawed)
        self.cards.append(card_drawed)

    def my_turn(self, deck_1):
        menu_1 = input("What would you like to do, hit or stand?\n") if not self.stand else 'stand'
        match menu_1:
            case 'hit':
                self.hit(deck_1)
                self.calc_score()
                print(f"You've drawned: {self.cards[-1]}, You currently have: {self.score}")
                # time.sleep(2)
                if self.score > 21:
                    print("Your score is higher than 21, You've lost :c")
                    self.loser = True
            case 'stand':
                print("You've passed your turn.")
                self.stand = True
            case _:
                print("Unknown command, please type 'hit' or 'stand':")



    def __repr__(self):
        return self.name

class croupier(player):
    def __init__(self, name):
        super().__init__(name)

    def start(self, cards_in_deck):
        self.hit(cards_in_deck)
        self.hit(cards_in_deck)
        self.calc_score()
        print(f"The croupier draws two cards, one of which is: {self.cards[0]}")
    def my_turn(self, deck_1):
        if self.score <= 16:
            print(f"Croupier has {self.score}, he draws a card...")
            time.sleep(2)
            self.hit(deck_1)
            self.calc_score()
            print(f"Croupiers cards: {self.cards}")
            if self.score == 21:
                print("Croupier has exactly 21 points!")
                self.stand = True
            if self.score > 21:
                print(f"Croupier has {self.score} points, he has lost the game")
                self.stand = True
        else:
            print(f"Croupier has {self.score} points, he doesn't draw a card")
            self.stand = True

class bot(player):
    def __init__(self, name):
        super().__init__(name)

    def start(self, cards_in_deck):
        self.hit(cards_in_deck)
        self.hit(cards_in_deck)
        self.calc_score()
        print(f"{self.name} draws two cards: {self.cards}")
    def my_turn(self, deck_1):
        rand = random.randint(14, 18)
        if self.score <= rand:
            print(f"{self.name} has {self.score}, he draws a card...")
            time.sleep(2)
            self.hit(deck_1)
            self.calc_score()
            print(f"{self.name}'s cards: {self.cards}")
            if self.score == 21:
                print(f"{self.name} has exactly 21 points!")
                self.stand = True
            if self.score > 21:
                print(f"{self.name} has {self.score} points, he has lost the game")
                self.stand = True
        else:
            print(f"{self.name} has {self.score} points, he doesn't draw a card")
            self.stand = True

def scoreboard(players):
    print(f"SCOREBOARD:")
    for i in players:
        print(f"*{i.name} has {i.score} points")
def game(nb_of_bots):
    deck1 = deck()
    deck1.new_deck()
    player_1 = player('player_1')
    croupier_0 = croupier('croupier_0')
    players = [player_1, croupier_0]
    for i in range(nb_of_bots):
        bot_name = "bot_" + str(i)
        players.append(bot(bot_name))
    print("START OF THE GAME")
    for guy in players:
        time.sleep(2)
        guy.start(deck1.cards)
    end_of_game = False
    while not end_of_game:
        for guy in players:
            time.sleep(2)
            guy.my_turn(deck1.cards)
            if guy.loser:
                end_of_game = True
                break
        scoreboard(players)
        if all([i.stand for i in players]):
            end_of_game = True
    time.sleep(2)
    for guy in players:
        if guy.score > 21:
            players.remove(guy)
    winner = max(players, key=lambda x: x.score)
    print(f"{winner} has won the game with {winner.score} points!")
    time.sleep(2)



if __name__ == "__main__":
    menu = ''
    bots = 0
    while menu not in ['1', '2', 'exit']:
        menu = str(input(f"1 - Start game\n2 - Add bot player\n3 - Remove bot player\n exit\n*{bots} bots\nChoose: "))
        match menu:
            case '1':
                game(bots)
            case '2':
                if bots <= 5:
                    bots += 1
            case '3':
                if bots >= 1:
                    bots -= 1
            case 'exit':
                continue
            case _:
                print("Unknown command, please type '1', '2', '3' or 'exit':")
        menu = ''