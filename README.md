# Deck of Cards

This is the *Deck of Cards* exercise from **The Modern Python 3 Bootcamp** Udemy course with instructor Colt Steele.

The exercise focuses on applyng OOP concepts.

There are two classes: a Card class and Deck class.

Each instance of Card has a value and a suit.

Each Deck has all 52 possible instances of card and the following 7 methods:

**1. count** - Returns a count of how many cards remain in the deck.

**2. __repr__** - Should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)

**3. _deal** - Accepts a number and removes at most that many cards from the end of the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".

**4. shuffle** - Will shuffle a full deck of cards. If there are cards missing from the deck, this method should raise a ValueError  with the message "Only full decks can be shuffled". shuffle should return the shuffled deck.

**5. deal_card** - Uses the _deal  method to deal a single card from the deck and return that single card.
deal_hand - accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.

**6. deal_hand** - Accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.