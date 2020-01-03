import unittest
from unittest.mock import patch

from app.classes.cartas import Cartas
from app.funcoes.funcao_continuar import continuar
from app.funcoes.funcao_start import BlackJack



class TestStart(unittest.TestCase):

    @patch('app.funcoes.funcao_start.continuar')
    @patch.object(Cartas, 'get_cartas')
    @patch.object(Cartas, 'retornar_cartas_salvas')
    @patch.object(Cartas, 'salvar_cartas')
    @patch.object(Cartas, 'retirar_carta')
    @patch.object(Cartas, 'embaralhar')
    @patch('app.funcoes.funcao_start.print')

    def test_start(
            self,
            print_mock,
            embaralhar_mock,
            retirar_carta_mock,
            salvar_cartas_mock,
            retornar_cartas_salvas_mock,
            get_cartas_mock,
            continuar_mock,
    ):
        # Arrange
        continuar_mock.return_value = False
        jogo = BlackJack()

        # Action
        jogo.jogo_start()

        # Assertions
        continuar_mock.assert_called_once()

    def setUp(self) -> None:
        self.black_jack = BlackJack()




