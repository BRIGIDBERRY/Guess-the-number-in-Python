def user_jugada():
    # 1.2  bucle que solicita a la jugadora que adivine el número
    """Solicita un número al usuario y lo convierte a entero.

    Returns:
        int: El número convertido, si es válido.
    """
    user_numero = 0
    while not numero_aceptable(user_numero):
        try:
            input_number = input("Ingresa un numero: ")
            user_numero = int(input_number) 
            if not numero_aceptable(user_numero):
                print("numero fuera del rango")
        except ValueError:  # buenas practicas poner el tipo except a usar
            print("  Oooh NO!Solo se aceptan numeros enteros!")

    return user_numero

def numero_aceptable(numero):
    """Pide al usuario un número y verifica si está en el rango de 1 a 100.

    Returns:
        int: El número ingresado por el usuario si es válido.
    """
    return 0 < numero < 101