import sys

def main():

    archivo=is_a_file()
    file=open_file(archivo)
    #print(file)
    valor = read_file(file)
    print(valor)


def is_a_file():

    try:


        if len(sys.argv) == 1:

            sys.exit("Too few command-line arguments")
    
        elif len(sys.argv) == 2: 

            if sys.argv[1].endswith(".py"):

                return sys.argv[1]

            else: 

                sys.exit("Not a Python file")

        elif len(sys.argv)>2:

            sys.exit("Too many command-line arguments")

    except ArithmeticError:

        print("")

def open_file(archivo):

    try:

        with open(archivo, "r") as file:

            filecito = file.read()
            return filecito

    except FileNotFoundError:

        print("")

    except TypeError:

        print("")

        
 
    

def read_file(file): 

    countnumeral = 0
    countcod = 0
    arreglote = []
    arreglito = ""


    try:
    
        for vc in range(len(file)):

            if file[vc] == "\n":

            
                arreglote.append(arreglito)
                print(arreglito)
                arreglito = ""

    
            arreglito = arreglito + file[vc]


        for vc2 in range (len(arreglote)):

            if arreglote[vc2].startswith("#"):

                countnumeral = countnumeral + 1

            elif len(arreglote[vc2]) < 3 :

                countcod = countcod + 1


        return len(arreglote)-countcod-countnumeral

    except TypeError:

        print("")

if __name__ == "__main__":
    main()