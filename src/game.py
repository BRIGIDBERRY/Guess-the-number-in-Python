from auxiliares_fuction import numero_randon, verificar_comparison, saludo_iniciar
from player_user import user_jugada
#from player_compute import rango_implentado, computer_jugada, inteligente_rango


def game():
    saludo_iniciar()
    randomn = numero_randon()

    while True:
        user_numbero = user_jugada()
        if randomn == user_numbero:
            print("ganaste")
            break
        else:
            verificar_comparison(user_numbero, randomn)

if __name__ == '__main__':
    game()
