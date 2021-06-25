import os
import time

def llenar_lista(lista):  
    introducir = int(input("escriba un numero: "))
    lista.append(introducir)
    print(lista)

   
def borrar_Pares(lista):
    contador = 0
    while contador < len(lista):
        almacen = lista[contador]
        if almacen % 2 == 0:
            lista.pop(contador)
        
        elif almacen % 2 == 1:
            contador += 1

def borrar_impares(lista):
    contador = 0
    while contador < len(lista):
        almacen = lista[contador]
        if almacen % 2 == 1:
            lista.pop(contador)
        
        elif almacen % 2 == 0:
            contador += 1

def borrar_primos(lista):
    contador = 0
    entrada = 0
    while contador < len(lista):
        entrada = 0
        almacen = lista[contador]
        for i in range(1,almacen + 1):
            if almacen % i == 0:
                entrada += 1
       
        if entrada == 2:
            lista.pop(contador)

        
        if entrada != 2:        
            contador += 1
 


def run():
    lista = []
    contador = 0
    opcion = 0
    while opcion !=5:
        menu = """
        "  Menu    interactivo  "
            1: Llenar lista
            2: Borrar pares
            3: Borrar impares
            4: Borrar primos
            5: Salir
            Opcion: """
        opcion = int(input(menu))
        time.sleep(0.2)
        os.system('clear')

        if opcion == 1:
            llenar_lista(lista)

        if opcion == 2:
            borrar_Pares(lista)
            print("Tu lista es: " + str(lista))
        
        if opcion == 3:
            borrar_impares(lista)
            print("Tu lista es: " + str(lista))
        
        if opcion == 4:            
            borrar_primos(lista)
            print("Tu lista es: " + str(lista))
        
        if opcion == 5:
            print("Gracias por usar el programa")
        
        if opcion > 5 or opcion < 1:
            print("opcion invalida") 
            time.sleep(0.8)
            os.system('clear')



if __name__ == '__main__':
    run()