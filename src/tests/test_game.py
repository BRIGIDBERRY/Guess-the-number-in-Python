import unittest
from unittest.mock import patch
from src.game import game
class TestGameCompute(unittest.TestCase):

    @patch('src.game.numero_randon')
    @patch('src.game.user_jugada') 
    @patch('src.game.computer_jugada')
    @patch('builtins.print')

    def test_game_computer_win(self, mock_print, mock_computer_jugada, mock_user_jugada, mock_numero_randon):
        mock_numero_randon.return_value = 75
        mock_user_jugada.return_value = 25
        mock_computer_jugada.return_value = 75

        game()

        self.assertTrue(mock_print.called)
        self.assertEqual(mock_print.call_count, 1)
    
class TestGameUser(unittest.TestCase):
      @patch('src.game.numero_randon')
      @patch('src.game.user_jugada')       
      @patch('builtins.print')

      def test_game_user_win(self, mock_print, mock_user_jugada, mock_numero_randon):
           mock_numero_randon.return_value = 60
           mock_user_jugada.return_value = 60

           game()

           self.assertTrue(mock_print.called)
           self.assertEqual(mock_print.call_count,1)

if __name__ == '__main__':
    unittest.main()