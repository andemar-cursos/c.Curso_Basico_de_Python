def main():
    mi_diccionario = {
        'llave1': 'Valor1',
        'llave2': 'Valor2',
        'llave3': 'Valor3',
        'llave4': 'Valor4'
    }

    # print(mi_diccionario['llave1'])

    # for llaves in mi_diccionario.keys():
    #     print(llaves)

    # for values in mi_diccionario.values():
    #     print(values)

    for keys, values in mi_diccionario.items():
        print(keys + " <---- key - value ----> " + values)


if __name__ == '__main__':
    main()