import unittest
from unittest.mock import Mock, patch, MagicMock

from app.black_jack.deck.deck import Deck


class TestDeck(unittest.TestCase):
    def test_deck_must_return_three_cards(self):

        cards = [Mock(), Mock(), Mock()]

        deck = Deck(cards)

        self.assertEqual(len(deck.get_cards()), 3)

    @patch('app.black_jack.deck.deck.random')
    def test_shuffle_deck(self, random_mock):
        cards = [
            Mock(),
            Mock(),
            Mock()
        ]
        random_mock.shuffle = MagicMock()
        deck = Deck(cards)

        deck.shuffle()

        random_mock.shuffle.assert_called_once_with(cards)

    def test_deck_should_return_one_card(self):
        cards = [
            'A',
            'Q',
            'J'
        ]

        deck = Deck(cards)

        one_card = deck.put_card()

        self.assertEqual(len(deck.get_cards()),2)
        self.assertEqual(len(one_card), 1)



