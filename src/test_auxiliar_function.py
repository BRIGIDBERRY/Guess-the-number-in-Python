import unittest
from unittest.mock import patch
from auxiliar_function import comparando_pista

class TestComparandoPistasBaja(unittest.TestCase):
    @patch('builtins.print')
    def test_comparando_pista(self, mock_print):
        jugada  = 10
        randonumber = 30
        comparando_pista(jugada, randonumber)
        mock_print.assert_called_with("Pista el numero es mayor")

class TestComparandoPistaAlta(unittest.TestCase):
    @patch('builtins.print')
    def test_comparando_pista(self, mock_print):
        jugada = 31
        randonumber = 11
        comparando_pista(jugada,randonumber)
        mock_print.assert_called_with("Pista el numero es menor")

