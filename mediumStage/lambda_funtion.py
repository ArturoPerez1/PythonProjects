def run():
    palindromo = lambda string: string == string[::-1]

try:
    print(palindromo(1))
except:
    print("solo puedes introducir strings")


if __name__ == '__main__':
    run()