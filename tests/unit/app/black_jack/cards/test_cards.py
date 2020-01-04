import unittest

from app.black_jack.cards.cards import Cards, A, Q, J, K, Um, Dois, Tres, Quatro, Cinco, Seis, Sete, Oito, Nove, Dez


class TestCards(unittest.TestCase):
    def test_carta_a_deve_ter_um_nome_valor_igual_a_um_e_ser_uma_carta(self):

        card_A = A()

        self.assertEqual(str(card_A), 'A')
        self.assertEqual(card_A.get_value(), 1)
        self.assertIsInstance(card_A, Cards)

    def test_carta_q_deve_ter_um_nome_valor_igual_a_dez_e_ser_uma_carta(self):

        card_Q = Q()

        self.assertEqual(str(card_Q), 'Q')
        self.assertEqual(card_Q.get_value(), 10)
        self.assertIsInstance(card_Q, Cards)

    def test_carta_j_deve_ter_um_nome_valor_igual_a_dez_e_ser_uma_carta(self):

        card_J = J()

        self.assertEqual(str(card_J), 'J')
        self.assertEqual(card_J.get_value(), 10)
        self.assertIsInstance(card_J, Cards)
    def test_carta_k_deve_ter_um_nome_valor_igual_a_dez_e_ser_uma_carta(self):

        card_K = K()

        self.assertEqual(str(card_K), 'K')
        self.assertEqual(card_K.get_value(), 10)
        self.assertIsInstance(card_K, Cards)

    def test_carta_um_deve_ter_um_nome_valor_igual_um_e_ser_uma_carta(self):

        card_Um = Um()

        self.assertEqual(str(card_Um), '1')
        self.assertEqual(card_Um.get_value(), 1)
        self.assertIsInstance(card_Um, Cards)

    def test_carta_dois_deve_ter_um_nome_valor_igual_dois_e_ser_uma_carta(self):

        card_Dois = Dois()

        self.assertEqual(str(card_Dois), '2')
        self.assertEqual(card_Dois.get_value(), 2)
        self.assertIsInstance(card_Dois, Cards)

    def test_carta_tres_deve_ter_um_nome_valor_igual_tres_e_ser_uma_carta(self):
        card_Tres = Tres()

        self.assertEqual(str(card_Tres), '3')
        self.assertEqual(card_Tres.get_value(), 3)
        self.assertIsInstance(card_Tres, Cards)


    def test_carta_quatro_deve_ter_um_nome_valor_igual_quatro_e_ser_uma_carta(self):
        card_Quatro = Quatro()

        self.assertEqual(str(card_Quatro), '4')
        self.assertEqual(card_Quatro.get_value(), 4)
        self.assertIsInstance(card_Quatro, Cards)

    def test_carta_cinco_deve_ter_um_nome_valor_igual_cinco_e_ser_uma_carta(self):
        card_Cinco = Cinco()

        self.assertEqual(str(card_Cinco), '5')
        self.assertEqual(card_Cinco.get_value(), 5)
        self.assertIsInstance(card_Cinco, Cards)

    def test_carta_seis_deve_ter_um_nome_valor_igual_seis_e_ser_uma_carta(self):
        card_Seis = Seis()

        self.assertEqual(str(card_Seis), '6')
        self.assertEqual(card_Seis.get_value(), 6)
        self.assertIsInstance(card_Seis, Cards)

    def test_carta_sete_deve_ter_um_nome_valor_igual_sete_e_ser_uma_carta(self):
        card_Sete = Sete()

        self.assertEqual(str(card_Sete), '7')
        self.assertEqual(card_Sete.get_value(), 7)
        self.assertIsInstance(card_Sete, Cards)

    def test_carta_oito_deve_ter_um_nome_valor_igual_oito_e_ser_uma_carta(self):
        card_Oito = Oito()

        self.assertEqual(str(card_Oito), '8')
        self.assertEqual(card_Oito.get_value(), 8)
        self.assertIsInstance(card_Oito, Cards)

    def test_carta_nove_deve_ter_um_nome_valor_igual_nove_e_ser_uma_carta(self):
        card_Nove = Nove()

        self.assertEqual(str(card_Nove), '9')
        self.assertEqual(card_Nove.get_value(), 9)
        self.assertIsInstance(card_Nove, Cards)

    def test_carta_dez_deve_ter_um_nome_valor_igual_dez_e_ser_uma_carta(self):
        card_Dez = Dez()

        self.assertEqual(str(card_Dez), '10')
        self.assertEqual(card_Dez.get_value(), 10)
        self.assertIsInstance(card_Dez, Cards)




