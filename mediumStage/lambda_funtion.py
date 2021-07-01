def run():
    palindromo = lambda string: string == string[::-1]

    print(palindromo('arepera'))


if __name__ == '__main__':
    run()