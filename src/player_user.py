def user_jugada():
    while True:
            
           try:
            input_number= input("Ingresa un numero : ")
            user_jugada = int(input_number)
            return user_jugada
           except :
            print(" ❌ Oooh NO!🥴 Solo se aceptan numeros enteros!")

user_jugada()
def numeros_aceptables():
    """_summary_

    Returns:
        _type_: _description_
    """
    while True:
     numero_aceptado = user_jugada()
     if numero_aceptado < 1 or numero_aceptado > 100:
       print("❌ Numero fuera de rango. Ingresa un numero valido del 1 al 100")
     else:
        print(f"✔️ Numero valido: {numero_aceptado}")
        return numero_aceptado
     
numeros_aceptables()

