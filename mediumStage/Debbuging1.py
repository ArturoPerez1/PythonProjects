def elevarCuadrado(num_user):
    try:
        if num_user < 0:
            raise ValueError("Solo se aceptan números positivos")
        
        num_user = num_user**2
        return num_user
    except ValueError as ve:
        print(ve)
        return False
        
    
def run():
    try:
        num_user = float(input("Ingrese un número: "))
        num_user = round(num_user,2)
        print(elevarCuadrado(num_user))

    except ValueError:
            print("Solo se aceptan numeros")


if __name__ == '__main__':
    run()