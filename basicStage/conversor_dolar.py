print("     CONVERSOR DE MONEDAS      ")
dolares = input("Ingrese la cantidad de Dolares tienes: ")
dolares = float(dolares)
valor_dolar = 3125000
bolivares = dolares * valor_dolar
bolivares = round(bolivares, 2)
bolivares = str(bolivares)
print("Tienes: " + bolivares +"bs")
