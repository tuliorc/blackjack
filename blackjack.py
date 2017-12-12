import random

suit_dict = {
    "diamond": "♦",
    "club": "♣",
    "heart": "♥",
    "spade": "♠"
}


class Player():
    def __init__(self, name, hand, isdealer=False, bankroll=1000):
        self.bankroll = bankroll
        self.name = name
        self.hand = hand
        self.isdealer = isdealer
        if isdealer:
            hand.cards[0].hidden = True

    def add_to_bankroll(self, amount):
        self.bankroll += amount

    def subtract_from_bankroll(self, amount):
        self.bankroll -= amount

    def print_hand(self):
        print("{name}'s hand: ".format(name=self.name))
        self.hand.print_cards()

    def print_bankroll(self):
        print("{name}'s money: {bankroll}".format(name=self.name, 
                                                    bankroll=self.bankroll))

    def show_all_cards(self):
        for card in self.hand.cards:
            card.hidden = False

class Card():
    def __init__(self, rank, suit, hidden=False):
        self.rank = rank
        self.suit = suit
        self.hidden = hidden

        if isinstance(self.rank, int):
            # if the rank is a numeric value, points will correspond to it
            self.points = self.rank
        elif self.rank == "A":
            # if the rank is an Ace, points can be either 1 or 11
            self.points = 1
        else:
            # if the rank is a Queen, King, or Jack, points are equal to 10
            self.points = 10

    def __str__(self):
        if not self.hidden:
            return "[{suit}{rank}]".format(suit=suit_dict[self.suit], 
                                           rank=self.rank)
        return "[???]"


class Hand():
    def __init__(self, cards):
        self.cards = []
        self.value = 0
        self.ace = False # there is no ace in hand
        for card in cards:
            self.add_card(card)

    def add_card(self, card):
        self.cards += [card]
        if card.rank == "A":
            self.ace = True
        self.value += card.points

    def total_points(self):
        # makes ace an 11 if it does not bust the hand
        if self.ace and self.value < 12:
            return self.value + 10
        return self.value
 
    def print_cards(self):
        # calls print function for each card in hand
        print(*self.cards, sep="\n")


def generate_deck():
    suits = ['club', 'diamond', 'heart', 'spade']
    ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
    cards = []
    for suit in suits:
        for rank in ranks:
            cards += [Card(rank, suit)]
    return cards


def get_card_from_deck():
    return deck.pop(random.randrange(0, len(deck)))

def hit():
    if human.hand.total_points() <= 21:
        human.hand.add_card(get_card_from_deck())
    if human.hand.total_points() > 21:
        human.subtract_from_bankroll(bet)

def stand():
    dealer.show_all_cards()
    while dealer.hand.total_points() < 17:
        dealer.hand.add_card(get_card_from_deck())
        if dealer.hand.total_points() >= 21:
            return "dealer lost"

def get_bet_input():
    try:
        bet_input = int(input("How much do you want to bet?"))
        if 0 < bet_input < human.bankroll:
            return bet
        return None
    except:
        return None


global deck, game_is_on, human, dealer
deck = generate_deck()
human = Player("Player1", Hand([get_card_from_deck(),
                                get_card_from_deck()]))
dealer = Player("PC", Hand([get_card_from_deck(),
                            get_card_from_deck()]), True)


game_is_on = True
while game_is_on and human.bankroll > 0:
    human.print_hand()
    human.print_bankroll()
    print("---------------------")
    dealer.print_hand()
    option_input, bet_input = None, None
    while option_input not in ['s', 'h', 'q']:
        try:
            option_input = str(input("Type 'h' for hitting, " + \
                                 "'s' for standing or 'q' for quitting: "))
        except:
            continue
        if option_input == 'q':
            game_is_on = False
            break
        else:
            bet = get_bet_input()
            if not bet:
                continue
            else:
                if option_input == 'h':
                    hit(bet)
                if option_input == 's':
                    stand(bet)
    else:
        continue

else:
    print("----------------------------")
    print("Game over! Hope you had fun!")
    print(human.print_bankroll())
    print("----------------------------")