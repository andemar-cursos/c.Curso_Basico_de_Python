
def main():
    potentiate = 0
    base = 2
    LIMITE = 1000
    resultant = 0

    while resultant <= LIMITE:
        print(resultant)
        resultant = pow(base, potentiate)
        potentiate += 1


if __name__ == '__main__':
    main()
