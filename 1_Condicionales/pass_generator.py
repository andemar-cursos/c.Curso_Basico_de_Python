import random

def pass_generator():
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symbo = ['!', '#', '$', '&', '/', '(', ')']
    numbe = ['1', '2', '3', '4', '5', '6', '7']

    characters = upper + lower + symbo + numbe

    passw = []

    for i in range(15):
        caracter_random = random.choice(characters)
        passw.append(caracter_random)

    # Allow convert list to string
    return "".join(passw)

def main():
    passw = pass_generator()
    print("Tu nueva pass es " + passw)


if __name__ == '__main__':
    main()