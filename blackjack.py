
class Player():

	def __init__(self, bankroll=1000):
		self.bankroll = bankroll

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


def generate_deck():
	suits = ['club', 'diamond', 'heart', 'spade']
	ranks = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
	cards = []
	for suit in suits:
		for rank in ranks:
			cards += [Card(rank, suit)]
	return cards



deck = generate_deck()

for c in deck:
	print(c)

print(len(deck))