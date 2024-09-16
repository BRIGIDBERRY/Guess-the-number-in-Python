from random import randint

def computer_jugada():
   
 #   Genera un numero aleatorio para el ordenador.

  #  Retorno:
   # int: La suposición del ordenador.
  
    pc_numero = randint(1, 100)
    pc_lanzada = f"Elijo el numero: {pc_numero}"
    print (pc_lanzada)
    return pc_numero