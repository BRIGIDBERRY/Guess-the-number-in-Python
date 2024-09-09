from auxiliares_fuction import numero_randon, comparando_pista, saludo_iniciar, lista, fin_game
from player_user import user_jugada
from player_compute import computer_jugada

usuario_lista = []
pc_lista = []

def game():
    saludo_iniciar()
    randomn = numero_randon()

    while True:
        print(" ES TU TURNO ")
        user_numero = user_jugada()
        listaparausuario = lista(user_numero, usuario_lista)
        if randomn == user_numero:
            fin_game('Usuario', listaparausuario )
            #print("➖🎊​​ FELICIDADES ADIVINASTE EL NUMERO 🥳 !!")
            break
        else:
            comparando_pista(user_numero, randomn)
        
        print("  TURNO DE LA PC ")
        pc_numero = computer_jugada()
        listapara_pc = lista(pc_numero,pc_lista)

        if pc_numero == randomn:
            fin_game('Sistema',listapara_pc)
            break
        else:
            comparando_pista(pc_numero,randomn)


if __name__ == '__main__':
    game()
