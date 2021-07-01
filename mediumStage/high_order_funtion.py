def saludo(func):
    func()


def hola():
    print("!!Hola!!")


def adios():
    print("!!Adios!!")


def run():
    saludo(hola)
    saludo(adios)


if __name__ == '__main__':
    run()