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
    def __init__(self, cards):
        self.cards = cards

    def add_card(self, card):
        self.cards += [card]

    def total_points(self):
        sum = 0
        for card in self.cards:
            if card.rank is "ace":
                # TODO: sometimes ace equals 11
                sum += 1
            else:
                sum += card.points
        return sum

    def print_cards(self):
        # calls print function for each card in hand
        print(*self.cards, sep="\n")

        # @TODO # print all cards and corresponding points


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


deck = generate_deck()
human = Player("Player1", Hand([get_card_from_deck(deck),
                                get_card_from_deck(deck)]))
dealer = Player("PC", Hand([get_card_from_deck(deck),
                            get_card_from_deck(deck)]), True)

human.print_hand()
print("---------------------")
dealer.print_hand()

option_input = ""
while not isinstance(option_input, int) or option_input not in [1, 2]:
    try:
        option_input = int(input("Type 1 for hitting or 2 for standing!"))
    except:
        continue
    if option_input == 1:
        human.hand.add_card(get_card_from_deck(deck))
    elif option_input == 2:
        pass
    else:
        continue

# @TODO # Rule: dealer must always hit if their sum is below 17
