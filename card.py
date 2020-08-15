from time import sleep


class Card:

	suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
	value_dict = {
		'1': 'Ace',
		'11': 'Jack',
		'12': 'Queen',
		'13': 'King'
	}

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def get_value(self):
		return self.value

	def get_suit(self):
		return self.suit

	def show(self):
		print(f'[{self.get_value()} of {self.get_suit()}]')


def generate_deck():
	_deck = []

	for suit in Card.suits:
		for i in range(1, 14):
			_deck.append(Card(value=str(i), suit=suit))

	for card in _deck:
		for value in Card.value_dict:
			if card.value == value:
				card.value = Card.value_dict.get(value)

	return _deck


def show(p_deck):
	length = str(len(p_deck))
	print('# PROGRAM START')
	sleep(1)
	print(f'####################')
	print('card.py - Card Deck')
	print(f'####################')
	sleep(1)
	print(f'-------------------')
	sleep(1)
	print(f'DECK GENERATED')
	sleep(1)
	print(f'Number of Cards: {length}')
	sleep(1)
	print(f'-------------------')
	sleep(1)
	for card in p_deck:
		card.show()
		sleep(0.125)
	sleep(1)
	print('--------------------')
	sleep(1)
	print('# PROGRAM ENDED')
	print('PYTHON: Quitting...')
	sleep(1)
	quit()


deck = generate_deck()
show(deck)
