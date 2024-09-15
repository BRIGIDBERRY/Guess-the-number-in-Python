import unittest
from unittest.mock import patch
from src.player_user import user_jugada

class TestValidoInput(unittest.TestCase ):
    @patch('src.player_user.input')
    def test_user_jugada_input(self, mock_input):
        mock_input.return_value = '12'
        resultado = user_jugada()
        self.assertEqual(resultado,12)

class TestInvalidoInput(unittest.TestCase):
    @patch('src.player_user.input')
    @patch('builtins.print')
    def test_user_jugada_input(self, mock_input, mock_print):
        mock_input.return_value = 'mundo'
        user_jugada()
        mock_print.assert_called_with("Ingresa un numero: ")
     

     