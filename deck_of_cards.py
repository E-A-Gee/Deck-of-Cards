from random import shuffle
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return "{} of {}".format(self.value,self.suit)

class Deck:
    def __init__(self):
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(value, suit) for suit in suits for value in values]
    def count(self):
        return len(self.cards)
    def __repr__(self):
        return "Deck of {} cards".format(self.count())
    def _deal(self, num):
        if self.count == 0:
            raise ValueError("All cards have been dealt")
        amt_to_rmv = min([self.count(), num])
        cards_dealt = self.cards[-amt_to_rmv:]
        self.cards = self.cards[:-amt_to_rmv]
        return cards_dealt
    def deal_card(self):
        return self._deal(1)[0]
    def deal_hand(self, num):
        return self._deal(num)
    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self.cards






