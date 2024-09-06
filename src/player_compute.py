from random import randint
   
def rango_implentado(): 
    
    """[,] lista con dos valores ,rango de numeros ha adividar para la pc
    """

    return[1, 100]

def computer_jugada(rango):
    """rango de numero aleatorio creado para la pc
    """    
    pc_numero = randint(rango[0], rango[1])
    print(f" ➖💻​ Elijo el numero: {pc_numero}")
    return pc_numero

def inteligente_rango(rango, guess_pc, pista_menor):
    if pista_menor:
        rango[1] = guess_pc - 1
    else:
        rango[0] = guess_pc + 1
    return rango

# Inicializa el rango APARTIR DE AQUI IMPLEMENTARLO PARA ARCHIVO GAME DONDE PONDRE UN PRINT(NUMERO SECRETO ES MENOR ) SII PARA PISTA_MENOR = TRUE O PRINT(NUMERO SECRETO ES MAYOY ) SI PISTA_MENOR ES FALSE
#rango = rango_implentado()

# Realiza una jugada de la computadora
#guess_pc = computer_jugada(rango)

# Simula una pista: por ejemplo, el número secreto es menor
#pista_menor = False

# Actualiza el rango basado en la pista
#rango_actualizado = inteligente_rango(rango, guess_pc, pista_menor)

#print(f"Nuevo rango después de la pista: {rango_actualizado}")







"""from random import randint

def computer_jugada():
   
    Genera un numero aleatorio para el ordenador.

    Retorno:
    int: La suposición del ordenador.
  
    pc_numero = randint(1, 100)
    print(f" ➖💻​ Elijo el numero: {pc_numero}")
    return pc_numero
computer_jugada() 
#PASOS: """
#NUMERO ALEATORIO PARA EL COMPUTADOR
#INTEGRAR EN EL JUEGO EL NUMERO DEL COMPUTADOR A SU TURNO