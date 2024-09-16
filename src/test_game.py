import unittest
from unittest.mock import patch
from game import game

class TestGame(unittest.TestCase):

    @patch('game.numero_randon')
    @patch('game.user_jugada')
    @patch('game.computer_jugada')
    #@patch('builtins.print')
    @patch('builtins.input')
    
    def test_game_computer_win(self, mock_input, mock_computer_jugada, mock_user_jugada, mock_numero_randon):
        """ Test dónde gana la computadora al adivinar el número correctamente """
        mock_numero_randon.return_value = 8
        mock_user_jugada.return_value = 5
        mock_computer_jugada.return_value = 8
        mock_input.return_value = "test"

        game()

        self.assertTrue(mock_print.called)
        self.assertEqual(mock_print.call_count, 3)
        #self.assertIn(5, usuario_lista)
        #self.assertIn(8, pc_lista)

    @patch('game.numero_randon')
    @patch('game.user_jugada')
    @patch('builtins.print')

    def test_game_user_win(self, mock_print, mock_user_jugada, mock_numero_randon):
        """ Test where the user wins by guessing the number correctly """
        mock_numero_randon.return_value = 20
        mock_user_jugada.return_value = 20

        game()

        self.assertTrue(mock_print.called)
        self.assertEqual(mock_print.call_count, 2)
        #self.assertIn(20, usuario_lista)

    @patch('game.numero_randon')
    @patch('game.user_jugada')
    @patch('game.computer_jugada')
    @patch('builtins.print')

    def test_multiple_turns(self, mock_print, mock_computer_jugada, mock_user_jugada, mock_numero_randon):
        """ Test en la que tanto el usuario como la computadora toman varios turnos antes de ganar """
        mock_numero_randon.return_value = 10
        mock_user_jugada.side_effect = [21, 18, 10]  # Simula tiros  user
        mock_computer_jugada.side_effect = [1, 2, 3]  # Simula tiros computer

        game()

        self.assertEqual(mock_print.call_count, 6)  # 3 turnos pero 6 print
        #self.assertIn(15, usuario_lista)
       
   
    @patch('game.numero_randon')
    @patch('game.user_jugada')
    @patch('game.computer_jugada')
    @patch('builtins.print')

    def test_invalid_user_input(self, mock_print, mock_computer_jugada, mock_user_jugada, mock_numero_randon):
        """ rueba para manejar entradas de usuario no válidas (no enteras o fuera de límites) """
        mock_numero_randon.return_value = 15
        mock_user_jugada.side_effect = ValueError("Input inválido")  # Simula un input invalido osea no numero o float

       