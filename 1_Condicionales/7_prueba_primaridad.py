def es_primo(numero):
    if numero == 1:
        return False
    for i in range(2, (numero // 2)+1):
        if numero % i == 0:
            return False
        else:
            continue

    return True


def main():
    primo = int(input("Escribe un numero: "))

    if es_primo(primo):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == '__main__':
    main()
