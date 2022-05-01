def main():
    # for contador in range(1000):
    #     print(contador)
# ---------------------------------------------
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     else:
    #         print(contador)
# ---------------------------------------------
    # for i in range(10000):
    #     if i == 1234:
    #         break
    #     else:
    #         print(i)
    # ---------------------------------------------
    # texto = input("Escribe algun texto ").lower()
    #
    # for caracter in texto:
    #     if caracter == 'a':
    #         break
    #
    #     print(caracter.upper())
    # ---------------------------------------------
    # Los decimales no se imprimen y al 50 se hace break
    i = 1
    while i <= 100:
        if i % 10 == 0:
            i += 1
            continue
        elif i >= 50:
            break
        else:
            print(i)
            i += 1

if __name__ == '__main__':
    main()
