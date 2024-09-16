from random import randint #uso del modulo randon con funcion randint

def saludo_iniciar():
    """
    uso de print para enviar mensaje de saludo
    """
    print("HOLA!!!jugaremos a Adivinar el numero ")
    print("tienes adivinar entre numeros del 1 al 100 suerte !")
    
#saludo_iniciar()

#  1.1 generando numero aleatorio
def numero_randon():
    numero_oculto  = randint(1,100)
    return numero_oculto

#1.3 verificar :comparar suposicion
def comparando_pista(jugador_guess, numero_oculto):
    """
    compara la suposicion del jugador con el numero arrojado por el sistema

    parametros: 
    jugador_guess(int): suposicion de los jugadores
    numero_oculto(int): numero que arroja el sistema
    """
    if jugador_guess < numero_oculto:   
        print ("Pista el numero es mayor")  
    elif jugador_guess > numero_oculto:   
        print ("Pista el numero es menor") 
    

#verificar_comparison(jugador_guess=2, numero_oculto=5)
def lista(numero_oculto, listade_intentos):
    """_summary_

    Args:
        numero_oculto: numero RANDOM
        listade_intentos: se iran anadiendo los input--intentos

    Returns:
        list: lista de intentos realizados antes de ganar
    """    
    listade_intentos.append(numero_oculto)
    return listade_intentos

def fin_game(ganador, listade_intentos):
    """_summary_

    Args:
        ganador (_type_): _description_
        listade_intentos (_type_): _description_
    """    
    print(f"Bravo!! {ganador} haz adivinado el numero")
    print(f" Hiciste {len(listade_intentos)} intentos, estas son tus jugadas : {listade_intentos} ​")

def volver_jugar(gameFunction):
    """ Preguntamos si quieren volver a jugar """
    preguntaInput = input("Quieres volver a jugar !!? (Si/No): ").lower()

    while preguntaInput not in ('si', 'no'):
        print("Ingresa una respuesta correcta (Si/No)")
        preguntaInput = input("Quieres volver a jugar !!? (Si/No): ").lower()

    if preguntaInput == 'si':
        gameFunction()
    else:
        print("Gracias por Jugar!")