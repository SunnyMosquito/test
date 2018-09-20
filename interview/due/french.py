import collections
from random import shuffle

Card = collections.namedtuple('Card', ['rank', 'suit', 'order'])

class FrenchDeck(object):
	ranks = [str(n) for n in range(3, 11)] + list('JQKA2')
	suits = 'diamonds clubs hearts spades'.split()
	suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

	def __init__(self):
		self._cards = [Card(rank, suit, 
							self.ranks.index(rank) * len(self.suit_values) + self.suit_values[suit]) 
							for suit in self.suits
							for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]

	def __setitem__(self, position, card):
		self._cards[position] = card

deck = FrenchDeck()

# suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# def spades_high(card):
# 	rank_value = FrenchDeck.ranks.index(card.rank)
# 	return rank_value * len(suit_values) + suit_values[card.suit]

# for card in sorted(deck, key=lambda card:card.order):
# 	print(card)

# print(deck[0], deck[13])
# print(deck[0].rank > deck[13].rank)
# shuffle(deck)
# print(len(deck))
# for i in deck:
# 	print(i)

# print(deck[3])

class Double(object):
	def __init__(self, cards):
		self._cards = cards
		self._cards.sort(key=lambda card:card.order)

	def __lt__(self, other):
		return self._cards[0].order < other._cards[0].order

	def __getitem__(self, position):
		return self._cards[position]

l1 = Double([deck[0],deck[13]])
for i in l1:
	print(i)

l2 = Double([deck[13],deck[26]])
for i in l2:
	print(i)

print(l1 > l2)
