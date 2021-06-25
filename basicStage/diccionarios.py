def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,      
    }

    # numero = mi_diccionario['llave1']
    # print(numero)
    # print( mi_diccionario['llave1'])
    # print( mi_diccionario['llave2'])
    # print( mi_diccionario['llave3'])

    poblacion_paise = {
        'Argentina': 44938712,
        'Venezuela': 3251220,
        'Mexico': 888888888,
    }
    # print(poblacion_paise['Argentina'])
    # print(poblacion_paise['Venezuela'])
    # print(poblacion_paise['llavefinal'])
    
    # iterar con diccionarios
    # for pais in poblacion_paise.keys():
    #     print(pais)

    # for pais in poblacion_paise.values():
    #     print(pais)

    for pais,poblacion in poblacion_paise.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')



if __name__ == '__main__':
    run()