import os
import random
import time

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
        return "[{suit} {rank}]".format(suit=suit_dict[self.suit],
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
        # sometimes, dealer does not show one of his initial cards
        if not hidden:
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
        # pops a random card from deck
        return self.cards.pop(random.randrange(0, len(self.cards)))


def hit():
    global bet, bankroll, deck, player_hand
    if player_hand.total_points() <= 21:
        # player can only hit if his hand does not exceed 21 points
        player_hand.add_card(deck.get_card())
        print_game_status()
    if player_hand.total_points() > 21:
        # player is busted if his hand exceeds 21 points!
        bankroll -= bet
        print("Busted! Player lost ${bet}!".format(bet=bet))
        print("Player's balance is ${bankroll}".format(bankroll=bankroll))
        print("---------------------")
        start_new_round()


def stand():
    global bankroll, bet, dealer_hand, player_hand

    dealer_hand.show_all_cards(True)
    # dealer keeps drawing cards until hand reaches 17 points
    while dealer_hand.total_points() < 17:
        time.sleep(2)
        dealer_hand.add_card(deck.get_card())
        os.system('cls' if os.name == 'nt' else 'clear')
        dealer_hand.show_all_cards(True)

    os.system('cls' if os.name == 'nt' else 'clear')
    print_game_status(True)

    if dealer_hand.total_points() > 21:
        bankroll += bet
        print("Dealer busted! Player won ${bet}!".format(bet=bet))      
    elif player_hand.total_points() > dealer_hand.total_points():
        bankroll += bet
        print("Player's hand is better than dealer's! You won ${bet}!".format(bet=bet))
    elif player_hand.total_points() < dealer_hand.total_points():
        bankroll -= bet
        print("Dealer's hand is better than player's! You lost ${bet}!".format(bet=bet))    
    else:
        print("Whoops! That's a tie!")
        
    print("Player's balance is ${bankroll}".format(bankroll=bankroll))
    print("---------------------")
    start_new_round()


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


def print_game_status(can_show_all=False):
    print("---------------------")
    print("Dealer's hand:")
    # dealer only sometimes shows all of his cards
    dealer_hand.show_all_cards(can_show_all)
    print("---------------------")
    print("Player's hand:")
    # player must always show all of his cards
    player_hand.show_all_cards(True)
    print("---------------------")


def exit_game():
    print("----------------------------")
    print("Game over! Hope you had fun!")
    print("Balance: ${bankroll}".format(bankroll=bankroll))
    print("----------------------------")
    exit()


def start_new_round():
    global bet, player_hand, dealer_hand, deck, initial_balance
    if game_is_on and bankroll >= 1:
        bet = 0
        bet = get_bet_input()
        deck = Deck()

        player_hand = Hand()
        dealer_hand = Hand()

        # initially, player and dealer have only two cards in hand
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
                os.system('cls' if os.name == 'nt' else 'clear')
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
