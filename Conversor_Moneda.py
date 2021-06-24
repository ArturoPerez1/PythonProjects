import os
import time

def conversor_moneda_dolar(tipo_moneda, valor_dolar):
    recibir_tipo = input("Ingrese la cantidad de " + tipo_moneda + " tienes: ")
    convertir_tipo = float(recibir_tipo)
    cantidad_dolar =  convertir_tipo / valor_dolar
    cantidad_dolar = round(cantidad_dolar, 2)
    cantidad_dolar = str(cantidad_dolar)
    print("Tienes: " + cantidad_dolar +"$")



def conversor_dolar_moneda(tipo_moneda, valor_dolar):
    recibir_dolar = input("Ingrese la cantidad de Dolares tienes: ")
    convertir_dolar = float(recibir_dolar)
    cantidad_moneda = convertir_dolar * valor_dolar
    cantidad_moneda = round(cantidad_moneda, 2)
    cantidad_moneda = str(cantidad_moneda)
    print("Tienes: " + cantidad_moneda + tipo_moneda)



menu = """

            MENU DE OPCIONES  
        ========================
            1:Convertir de bolivar a dolar
            2:Convertir de dolar a bolivar
            3:Convertir de peso a dolar
            4:Convertir de dolar a peso
            5: Salir
            Elija una opcion: """

recibir = int(input(menu))
time.sleep(0.5)
os.system("clear")

  
if recibir == 1:
    conversor_moneda_dolar("Bolivares", 3150000)
     

    
elif recibir == 2:
    conversor_dolar_moneda(" Bolivares", 3150000)
        
elif recibir == 3:
    conversor_moneda_dolar("Pesos", 3500)   


elif recibir == 4:
    conversor_dolar_moneda(" Pesos", 3500)
   
else:
    print("Muchas gracias por usar el programa")

        


