import random
import os

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
        return card_drawed

    def my_turn(self):
        menu_1 = input("What would you like to do, hit or stand?\n")



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
    def my_turn(self):
        pass

def scoreboard(players):
    print(f"SCOREBOARD:")
    for i in players:
        print(f"*{i.name} has {i.score} points")
def game(nb_of_bots):
    deck1 = deck()
    deck1.new_deck()
    player_1 = player('player_1')
    croupier_0 = croupier('croupier_0')
    players = [croupier_0, player_1]
    print("START OF THE GAME")
    for guy in players:
        guy.start(deck1.cards)
    while True:




if __name__ == "__main__":
    menu = ''
    bots = 0
    while menu not in ['1', '2', 'exit']:
        menu = str(input(f"1 - Start game\n2 - Add bot player\n exit\n*{bots} bots\nChoose: "))
        match menu:
            case '1':
                game(bots)
            case '2':
                bots += 1
            case 'exit':
                continue
            case _:
                print("Unknown command, please type '1', '2', or 'exit':")
        menu = ''