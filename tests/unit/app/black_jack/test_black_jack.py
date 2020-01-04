import unittest

from unittest.mock import patch

from app.black_jack.black_jack import BlackJack
from app.black_jack.deck.deck import Deck


class TestBlackJack(unittest.TestCase):

    @patch('app.black_jack.black_jack.input')
    @patch('app.black_jack.black_jack.print')
    @patch.object(Deck, 'shuffle')
    def test_should_be_start_on_blackjack(self, mock_shuffle, mock_print, mock_input):


        black_jack = BlackJack()

        black_jack.start()

        self.assertTrue(mock_shuffle.called)
        self.assertTrue(mock_print.called)
        self.assertTrue(mock_input.called)


