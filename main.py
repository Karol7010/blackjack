import random

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
    def hit(self, cards_in_deck):
        i = random.randint(0,len(cards_in_deck))
        card_drawed = cards_in_deck[i]
        cards_in_deck.remove(card_drawed)
        self.cards.append(card_drawed)
        return card_drawed
    def start(self, cards_in_deck):
        self.hit(cards_in_deck)
        self.hit(cards_in_deck)
    def calc_score(self):
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

    def __repr__(self):
        return self.name

class croupier(player):
    def __init__(self, name):
        super().__init__(name)
    def my_turn(self):
        pass

class bot(player):
    def __init__(self, name):
        super().__init__(name)
        self.name
    def my_turn(self):
        pass

def game(nb_of_bots):
    deck1 = deck()
    deck1.new_deck()
    player_1 = player(input(f"Input name for player: "))
    croupier_0 = croupier('croupier_0')
    players = [croupier_0, player_1]
    for i in range(nb_of_bots):
        temp = 'bot_'+str(i)
        globals()[temp] = player(temp)
        players.append(globals()[temp])
    print("===============================================\nStart of the game, drawing two cards: ")
    for i in players:
        i.start(deck1.cards)
    print(player_1.cards)
    print(f"Croupier draws two cards, one of which is: \n{croupier_0.cards}")
    print("===============================================\nCurrent score:")
    for i in players:
        i.calc_score()
        print(f"*{i.name}: {i.score}")
    menu_1 = ''
    print("===============================================")
    while True:
        winners = []
        for i in players:       #checking if anyone won
            if i.score == 21:
                winners.append(i.name)
            elif i.score>21:
                pass    #tu skończyłem



        if len(winners)>0:
            return winners
        menu_1 = input("What would you like to do:\n*hit\nstand (end game)")
        match menu_1:
            case 'hit':
                player_1.hit(deck1.cards)
            case 'stand':
                continue
            case 'exit':
                continue
            case _:
                print("Unknown command, please type 'hit', 'stand', or 'exit':")


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