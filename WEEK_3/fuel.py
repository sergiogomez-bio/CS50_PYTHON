def main():

    
    verificar_tanque()    

def verificar_tanque():

    
    
    while True:

        fuel = input("Diga cuanta gasolina tiene su tanque:  ")
        
        
        try: 

            primero = fuel[0]
            segundo = fuel[2]
            division=0.0

            if primero.isdigit() and segundo.isdigit():


                primero = float(primero)
                segundo = float(segundo)
                division = primero/segundo

                try:

                    if division == 0.75:

                        print("75%")
                        break

                    elif division == 0.5:

                        print("50%")
                        break

                    elif division == 0.25:

                        print("25%")
                        break
        
                    elif division == 1:

                        print("F")
                        break

                    elif(division == 0):

                        print("E")
                        break


                except ZeroDivisionError:

                    print("")

                except ValueError:

                    print("")

        except IndexError:

            print("")

main()














            


