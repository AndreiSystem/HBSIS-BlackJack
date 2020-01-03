import unittest

from app.classes.cartas import Cartas


class TestCartas(unittest.TestCase):
    def setUp(self) -> None:
        self.deck = Cartas()

    def test_deck_should_be_13_unit(self):
        cartas = self.deck.get_cartas()

        self.assertEqual(13, len(cartas))

    def test_deck_should_one_card_return(self):

        card = self.deck.retirar_carta()

        self.assertEqual(1, len(card))

    def test_should_be_saved_one_card_in_deck(self):
        carta = self.deck.retirar_carta()

        self.deck.salvar_cartas(carta)

        cartas_salvas = self.deck.get_cartas_salvas()
        self.assertEqual(len(cartas_salvas), 1)

    def test_should_be_return_saved_letter_and_return_none(self):
        carta = self.deck.retirar_carta()

        self.deck.salvar_cartas(carta)


        self.assertIsNone(self.deck.retornar_cartas_salvas())

    def test_shuffle_deck_and_return_none(self):

        carta_lista = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]

        embalharar = self.deck.embaralhar()

        cartas_nova_lista = self.deck.get_cartas()

        self.assertIsNone(embalharar)

        self.assertNotEqual(cartas_nova_lista, carta_lista)











