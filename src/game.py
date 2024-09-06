from auxiliares_fuction import numero_randon, verificar_comparison
from player_user import user_jugada, numeros_aceptables
from player_compute import rango_implentado, computer_jugada, inteligente_rango

def game():
    
    randomn= numero_randon()
    
    while True:
     user_numbero = user_jugada()
     if randomn == user_numbero:
       print("ganaste")
       break
     else :verificar_comparison (user_numbero, randomn)

game()

