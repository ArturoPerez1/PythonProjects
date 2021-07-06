def divisors(num):
    try:
        if num < 0:
            raise ValueError("Solo son aceptados numero positivos")
        divisor = [i for i in range(1,num + 1) if num % i == 0]
        return divisor
    
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:           
        num = int(input("Escriba un numero: "))
        print(divisors(num))
        print("termino mi programa")
    except ValueError:
        print("Debe ingresar un numero")
if __name__ == '__main__':
    run()