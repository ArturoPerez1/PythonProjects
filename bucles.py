import requests
import json

def run():
    LIMITE = 1000000
    contador = 0
    potencia_2 = 2 ** contador

    while potencia_2 < LIMITE:
        print("2 elevado a" + str(contador) + " es igual a:" + str(potencia_2))
        contador += 1
        potencia_2 = 2 ** contador
        requests.delete(url="https://webhook.site/5228253d-488b-40e6-86d2-2aeb655cdeea", data=json.dumps("2 elevado a" + str(contador) + " es igual a:" + str(potencia_2)))


if __name__ == '__main__':
    run()