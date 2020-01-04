import random

class Deck:
    def __init__(self, cards: list):
        self._cards = cards

    def get_cards(self) -> list:
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def put_card(self):
        return self._cards.pop(0)



