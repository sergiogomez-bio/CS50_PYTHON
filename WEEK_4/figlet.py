import sys
from pyfiglet import Figlet
import random


# entrada1 = sys.argv[0]
# entrada2 = sys.argv[1]
# entrada3 = sys.argv[2]
figlet = Figlet()
listado = figlet.getFonts()

if len(sys.argv) == 1:

    
    listadoran = random.choice(listado)
    printcito = input("Input: ")
    newfiglet = Figlet(font=listadoran)
    print(newfiglet.renderText(printcito))

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):

    

    if sys.argv[2] in listado:

        printcito = input("Input: ")
        newfiglet = Figlet(sys.argv[2])
        print(newfiglet.renderText(printcito))

    else:

        print("Invalid usage")
        sys.exit()

else:

    print("Invalid usage")
    sys.exit()





