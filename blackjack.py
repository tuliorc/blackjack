import random
import os

suit_dict = {
    "diamond": "♦",
    "club": "♣",
    "heart": "♥",
    "spade": "♠"
}


class Card:
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
        return "[{suit}{rank}]".format(suit=suit_dict[self.suit],
                                       rank=self.rank)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False # there is no ace in hand

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
        print(*self.cards)

    def show_all_cards(self, hidden=False):
        if hidden:
            initial_card = 1
            print("[???]")
        else:
            initial_card = 0
        for x in range(initial_card, len(self.cards)):
            print(self.cards[x])


class Deck:

    def __init__(self):
        self.suits = ['club', 'diamond', 'heart', 'spade']
        self.ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards += [Card(rank, suit)]

    def get_card(self):
        return self.cards.pop(random.randrange(0, len(self.cards)))


def hit():
    global bet, bankroll, deck, player_hand
    if player_hand.total_points() <= 21:
        player_hand.add_card(deck.get_card())
        print_game_status()
    if player_hand.total_points() > 21:
        bankroll -= bet
        print("---------------------")
        print("Busted! Player lost ${bet}!".format(bet=bet))
        print("Player's balance is ${bankroll}".format(bankroll=bankroll))
        print("---------------------")
        start_new_round()


def stand():
    pass


def get_bet_input():
    global bet, bankroll
    bet = 0
    while bet == 0:
        try:
            bet_input = int(input("How much do you want to bet? "))
            if 1 <= bet_input <= bankroll:
                # clear console for another round
                os.system('cls' if os.name == 'nt' else 'clear')
                return bet_input
            else:
                print("Invalid bet! You only have {amount} of balance"
                      .format(amount=bankroll))
        except ValueError:
            print("Please type in a valid value of bet!")


def get_initial_balance():
    global initial_balance
    initial_balance = 0
    while initial_balance <= 0:
        try:
            initial_balance = int(input("Type in your initial balance: "))
        except ValueError:
            continue
    return initial_balance


def print_game_status():
    print("---------------------")
    print("Dealer's hand:")
    dealer_hand.show_all_cards(True)
    print("---------------------")
    print("Player's hand:")
    player_hand.show_all_cards(False)
    print("---------------------")


def exit_game():
    print("----------------------------")
    print("Game over! Hope you had fun!")
    print("Balance: ${bankroll}".format(bankroll=bankroll))
    print("----------------------------")
    exit()


def start_new_round():
    global bet, player_hand, dealer_hand, deck, initial_balance
    if game_is_on and 1 <= bankroll <= initial_balance:
        bet = 0
        bet = get_bet_input()
        deck = Deck()

        player_hand = Hand()
        dealer_hand = Hand()

        player_hand.add_card(deck.get_card())
        player_hand.add_card(deck.get_card())
        dealer_hand.add_card(deck.get_card())
        dealer_hand.add_card(deck.get_card())

        print_game_status()

        option_input = None
        while option_input not in ['s', 'h', 'q']:
            try:
                option_input = str(input("Type 'h' for hitting, "
                                         "'s' for standing "
                                         "or 'q' for quitting: "))
            except ValueError:
                continue
            if option_input == 'q':
                exit_game()
                return
            else:
                if option_input == 'h':
                    hit()
                if option_input == 's':
                    stand()
                option_input = None
                continue

    else:
        exit_game()

bankroll = initial_balance = get_initial_balance()
player_hand, dealer_hand = None, None
game_is_on = True
bet = 0
start_new_round()
