menu = """
Bienvenido al conversor de monedas 😗
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """

def calculo(pesos, valor_dolar):
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    return dolares

opcion = int(input(menu))

if opcion == 1:
    pesos = int(input("Ingresa los COP que quieres convertir a Dolares "))
    valor_dolar = 3760
    print("Tienes $" + calculo(pesos, valor_dolar) + " Dolares")
elif opcion == 2:
    pesos = int(input("Ingresa los ARS que quieres convertir a Dolares "))
    valor_dolar = 113.98
    print("Tienes $" + calculo(pesos, valor_dolar) + " Dolares")
elif opcion == 3:
    pesos = int(input("Ingresa los MXP que quieres convertir a Dolares "))
    valor_dolar = 19.97
    print("Tienes $" + calculo(pesos, valor_dolar) + " Dolares")
else:
    print("Elige alguna opcion entre 1 y 3")



