
import random

class Player():

	def __init__(self, hand, bankroll=1000):
		self.bankroll = bankroll
		self.hand = hand

	def add_to_bankroll(self, amount):
		self.bankroll += amount

	def subtract_from_bankroll(self, amount):
		self.bankroll -= amount

class Card():
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		if type(self.rank) == int:
			# if the rank is a numeric value, points will correspond to it
			self.points = self.rank
		elif self.rank == "ace":
			# if the rank is an Ace, points can be either 1 or 11
			self.points = (1, 11)
		else:
			# if the rank is a Queen, King, or Jack, points are equal to 10
			self.points = 10

	def __str__(self):
		return "Suit: {suit}, Rank: {rank}, Points: {points}".format(
					suit=self.suit, rank=self.rank, points=self.points)


class Hand():
	def __init__(self, cards):
		self.cards = cards

	def add_card(self, card):
		self.cards += card

	def total_points(self):
		sum = 0
		for card in self.cards:
			if card.rank is "ace":
				#TODO: sometimes ace equals 11
				sum += 1
			else:
				sum += card.points
		return sum

	def __str__(self):
		return "O total é de {total}".format(total=self.total_points())
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
player_hand = Hand([get_card_from_deck(deck), get_card_from_deck(deck)])
dealer_hand = Hand([get_card_from_deck(deck), get_card_from_deck(deck)])

print(player_hand)
print(dealer_hand)

# @TODO # Rule: dealer must always hit if their sum is below 17