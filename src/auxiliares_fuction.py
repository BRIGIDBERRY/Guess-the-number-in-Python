from random import randint #uso del modulo randon con funcion randint
def saludo_del_juego():
    """
    uso de print para enviar mensaje de saludo
    """
    print("🤖 HOLA!!! 🤖 jugaremos a adivinar el numero 🎲 suerte 🍀​​​!!")
    
saludo_del_juego()

#generando numero aleatorio
def numero_randon():
    numero_sistem  = randint(1,100)
    return numero_sistem
#print(numero_randon())
# PASOS :
#Generar el número secreto: Lógica para generar el número aleatorio. /
#Verificar las suposiciones: Comparar las suposiciones con el número secreto y dar pistas.