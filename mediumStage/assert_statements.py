def divisors(num):
    assert num > 0, "Solo se aceptan numeros positivos"
    divisor = [i for i in range(1,num + 1) if num % i == 0]
    return divisor


def run():
    try:               
        num = input("Escriba un numero: ")
        print(divisors(int(num)))
        print("termino mi programa")
    
    except ValueError:
        print("Solo se aceptan numeros")



if __name__ == '__main__':
    run()