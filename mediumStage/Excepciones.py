def palindromo(string):
    try:
        if len(string) == 0:
            raise ValueError("No se aceptan string vacios")
        palindromo = lambda string: string == string[::-1]
        return palindromo
    
    except ValueError as ve:
        print(ve)
        return False 


try:
   print(palindromo(""))
except TypeError:
    print("solo puedes introducir strings")

