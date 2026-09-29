import inflect



def whileand():

    cumulo = []

    while True:

        print("1")
        detecta = input("name: ")
        cumulo.append(detecta)
        if detecta == "":

            return cumulo
            break



def llamarinflect(cumulo):

    if cumulo[0] != "":

        cumulito = cumulo[:len(cumulo)-1]
        p = inflect.engine()
        imprimir = p.join(cumulito)
        print(f"imprimir:  {imprimir}")


    if len(cumulo) == 1:

        if cumulo[0] == "":

            print("2")
            print("no escribiste nada")

        else: 

            print("3")
            print("Adieu, adieu, to {cumulo[0]}")

    else:

        print("4")
        print(f"Adieu, adieu, to {imprimir}")
    


def main():

    cumulo = whileand()
    llamarinflect(cumulo)



try: 

    main()


except EOFError:

    print("")

except ZeroDivisionError:
        
    print("")
        
except ValueError:
        
    print("")

except TypeError:

    print("")