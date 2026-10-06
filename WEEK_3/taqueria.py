taqueria = {     "Baja Taco"       : 4.25,
                 "Burrito"         : 7.50,
                 "Bowl"            : 8.50,
                 "Nachos"          : 11.00,
                 "Quesadilla"      : 8.50,
                 "Super Burrito"   : 8.50,
                 "Super Quesadilla": 9.50,
                 "Taco"            : 3.00,
                 "Tortilla Salad"  : 8.00   }

def find_taco(taqueria):

    cumulo = 0.0

    while True:

        

        try:

            pedido = input("Que desea ordenar:   ")
            pedido = sensibilidad_mayusculas_minusculas(pedido)
            cumulo = cumulo + taqueria.get(pedido)
            print(f"Total:  {cumulo}")


        except EOFError:

            print("")
            

        except ZeroDivisionError:
        
            print("")
        
        except ValueError:
        
            print("")

        except TypeError:

            print("")



def sensibilidad_mayusculas_minusculas(palabra):

    palabra = palabra.lower()
    posicion = palabra.find(" ")
    
    if posicion == -1:
    
        corregida = palabra[0].upper() + palabra[1:]
    
    elif posicion >= 0: 
    
        corregida = palabra[0].upper() + palabra[1:posicion] + " " + palabra[posicion+1].upper()  + palabra[posicion+2:]

    return corregida



def main():

    find_taco(taqueria)

main()
