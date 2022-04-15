menu = """
Bienvenido al conversor de monedas 😗
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = int(input("Ingresa los COP que quieres convertir a Dolares"))
    valor_dolar = 3760
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares")
elif opcion == 2:
    pesos = int(input("Ingresa los ARS que quieres convertir a Dolares"))
    valor_dolar = 113.98
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares")
elif opcion == 3:
    pesos = int(input("Ingresa los MXP que quieres convertir a Dolares"))
    valor_dolar = 19.97
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares")
else:
    print("Elige alguna opcion entre 1 y 3")
