import random
import os
import time


def imprimirBarras(longitud_string):
    new_lista = []
    for i in range(longitud_string):
        new_lista.append("_")
    return new_lista

# Function for transform a file in list
def convertir_lista():
    lista_aux = []
    with open("/home/wjoseperez/Documents/Arturo_Proyectos/ArturoPython/archivos/data.txt", "r", encoding="utf-8") as file:
        for line in file:
            lista_aux.append(str(line))

    return lista_aux


# Function for switch and compare string 
def comparar_remplazar(lista_barra,lista_aux):
    indice_letra = 0
    no_mach = False
    print('\n')
    user_input = input("introduzca una letra: ")
    for letra in range(len(lista_aux)):
        os.system("clear")
        if user_input == lista_aux[letra]:
            indice_letra = letra
            lista_barra[indice_letra] = lista_barra[indice_letra].replace("_",user_input)
        else:
            no_mach = True
    return no_mach


#function main
def run():
    # var declaration and add value
    iterador = 1
    lista_principal = convertir_lista()
    lista_barras = []
    lista_random = random.randint(0,len(lista_principal))
    lista_aux = lista_principal[lista_random].strip()
    longitud_string = len(lista_aux)
    
    #rules of the game
    print("Tienes diez intentos para acertar en la palabra", end=" ")
    print("si se terminan tus intentos estarás muerto", end=" ")
    print("he iniciarás de nuevo")
    time.sleep(7)
    os.system("clear")

    # call to functions
    lista_barra = imprimirBarras(longitud_string)

    #attempts loop
    while iterador < 10:      
        no_mach = comparar_remplazar(lista_barra,lista_aux)
        for letra1 in range(len(lista_barra)):
            string = str(lista_barra)
            string = string.replace("[",'')
            string = string.replace(",",'')
            string = string.replace("]",'')
            string = string.replace("'",'')
            string = string.replace(" ","")
            string = string.strip()
            print(lista_barra[letra1], end=" ")

        if string == lista_aux:
            break
        
        if no_mach == False and iterador >= 0:
            iterador -= 1
            
        if no_mach == True:
            no_mach = False
            iterador += 1
          
    if iterador == 10:
        print('\n')
        print("Haz muerto ahorcado la palabra era")
        for letra1 in range(len(lista_barra)):
            print(lista_aux[letra1], end=" ")
    else:
        print('\n')
        print("Haz ganado")

    print('\n')

if __name__ == '__main__':
    run()