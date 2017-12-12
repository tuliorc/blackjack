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
        elif self.rank == "ace":
            # if the rank is an Ace, points can be either 1 or 11
            self.points = (1, 11)
        else:
            # if the rank is a Queen, King, or Jack, points are equal to 10
            self.points = 10

    def __str__(self):
        if not self.hidden:
            return "[{suit}{rank}] ({points} points)".format(
                suit=suit_dict[self.suit], rank=self.rank, points=self.points)
        return "[???]"


class Hand():
    def __init__(self, cards, type_hand):
        self.cards = []
        self.type_hand = type_hand
        self.value = 0
        self.ace = False # there is no ace in hand
        for card in cards:
            self.add_card(card)

    def add_card(self, card):
        self.cards += [card]
        if card.rank = "ace":
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
    ranks = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
    cards = []
    for suit in suits:
        for rank in ranks:
            cards += [Card(rank, suit)]
    return cards


def get_card_from_deck(deck):
    return deck.pop(random.randrange(0, len(deck)))

def play_round(player, dealer):
    option_input = None
    while not isinstance(option_input, int) or option_input not in [1, 2]:
        try:
            option_input = int(
                input("Type 1 for hitting or 2 for standing: "))
        except:
            continue
        if option_input == 1:
            player.hand.add_card(get_card_from_deck(deck))
            while player.hand.total_points
            is_hand_busted(player):
                print("jogador perdeu!")
                pass
        elif option_input == 2:
            dealer.show_all_cards()
            if not is_hand_busted(dealer):

            pass
        else:
            continue


def is_hand_busted(player):
    if player.isdealer and player.hand.total_points > 17:
        # dealer cannot pass 17 points
        return True
    if not player.isdealer and player.hand.total_points >= 21:
        # human player cannot go over 21 points
        return True
    return False


global deck
deck = generate_deck()
human = Player("Player1", Hand([get_card_from_deck(deck),
                                get_card_from_deck(deck)]))
dealer = Player("PC", Hand([get_card_from_deck(deck),
                            get_card_from_deck(deck)]), True)

human.print_hand()
print("---------------------")
dealer.print_hand()

play_round(human, dealer)

