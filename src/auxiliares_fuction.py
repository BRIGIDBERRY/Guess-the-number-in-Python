from random import randint #uso del modulo randon con funcion randint

def saludo_iniciar_juego():
    """
    uso de print para enviar mensaje de saludo
    """
    print("➖🤖 HOLA!!! 🤖 jugaremos a Adivinar el numero 🎲 ")
    print ("➖🤖 tienes adivinar entre numeros del 1 al 100 suerte 🍀​​​!!")
    
saludo_iniciar_juego()

#  1.1 generando numero aleatorio
def numero_randon():
    numero_oculto  = randint(1,100)
    return numero_oculto
#1.3 verificar :comparar suposicion
def verificar_comparison(jugador_guess, numero_oculto):
    """
    compara la suposicion del jugador con el numero arrojado por el sistema

    parametros: 
    jugador_guess(int): suposicion de los jugadores
    numero_oculto(int): numero que arroja el sistema
    """
    if jugador_guess < numero_oculto:   
        print ("➖🔎 Pista el numero es mayor 🤫​ ")  
    elif jugador_guess > numero_oculto:   
        print ("➖🔎 Pista el numero es menor 🤫​ ") 
    else:
        print("➖🎊​​ FELICIDADES ADIVINASTE EL NUMERO 🥳 !!")

verificar_comparison(jugador_guess=2, numero_oculto=5)

def registro_lista(numero_oculto, registrar_lista):
    """_summary_

    Args:
        numero_oculto (_type_): _description_
        registrar_lista (_type_): _description_

    Returns:
        _type_: _description_
    """    
    registrar_lista.append(numero_oculto)
    return registrar_lista
