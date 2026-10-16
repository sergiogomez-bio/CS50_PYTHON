import csv
import sys
from tabulate import tabulate

def main ():

    archivo = is_a_file()
    filas = open_file(archivo)
    mod_csv_table(filas)    



def is_a_file():

    try:


        if len(sys.argv) == 1:

            sys.exit("Too few command-line arguments")
    
        elif len(sys.argv) == 2: 

            if sys.argv[1].endswith(".csv"):

                return sys.argv[1]

            else: 

                sys.exit("Not a CSV file")

        elif len(sys.argv)>2:

            sys.exit("Too many command-line arguments")

    except ArithmeticError:

        sys.exit("")



def open_file(archivo):

    try:

        with open(archivo, "r") as csvfile:

            filecito = csv.reader(csvfile)
            filas = list(filecito)
            return filas
        
    except FileNotFoundError:

        sys.exit("File does not exist")

    except TypeError:

        print("")

def mod_csv_table(archivo):

    table = archivo[1:]
    headers = archivo[0]
    print(tabulate(table, headers, tablefmt="grid"))


    ...

if __name__ == "__main__":
    main()