def write():
    names = ["Arturo","pedro","Facundo","Andrea"]
    with open("/home/wjoseperez/Documents/Arturo_Proyectos/ArturoPython/archivos/names.txt","w", encoding="utf-8") as file:
        for name in names:
            file.write(name)
            file.write("\n")


def read():
    number = []
    with open("/home/wjoseperez/Documents/Arturo_Proyectos/ArturoPython/archivos/number.txt","r",encoding ="utf-8") as file:
        for line in file:
            number.append(int(line))
    print(number)    


def run():
   read()

if __name__ == '__main__':
    run() 