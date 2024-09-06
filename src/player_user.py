def user_jugada():
  # 1.2  bucle que solicita a la jugadora que adivine el número
  """Solicita un número al usuario y lo convierte a entero.
    
    Returns:
        int: El número convertido, si es válido.
  """
  while True:
            
           try:
            input_number= input(" ➖🤖​ Ingresa un numero  : ")
            user_numero= int(input_number)
            return user_numero
           except ValueError: #buenas practicas poner el tipo except a usar
            print(" ➖❌ Oooh NO!🥴 Solo se aceptan numeros enteros!")


def numeros_aceptables():
    """Pide al usuario un número y verifica si está en el rango de 1 a 100.
    
    Returns:
        int: El número ingresado por el usuario si es válido.
    """
    while True:
     numero_aceptado = user_jugada()
     if numero_aceptado  < 1  or numero_aceptado > 100:
       print(" ➖❌ Numero fuera de rango. Ingresa un numero valido del 1 al 100")
     else:
        print(f" ➖✔️  Numero valido: {numero_aceptado}")
        return numero_aceptado
     
numeros_aceptables() 
 
