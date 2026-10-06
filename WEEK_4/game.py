import random

def adivina():

<<<<<<< HEAD
=======
    vector = []
>>>>>>> d242c27 (Corregir estructura y agregar carpeta WEEK_5)

    try: 

        entrada1 = int(input("level:  "))
        verifica = entrada1 % 1

        if verifica > 0 : # aqui verifica que sea entero

<<<<<<< HEAD
            entrada1 = 0
            adivina()

        elif entrada1 < 0: # aqui verifica no sea negativo
            
            entrada1 = 0
=======
            adivina()

        if entrada1 < 0: # aqui verifica no sea negativo

>>>>>>> d242c27 (Corregir estructura y agregar carpeta WEEK_5)
            adivina()

    except ValueError: #aqui verifica que no sea string

<<<<<<< HEAD
        entrada1 = 0
        adivina()
        
=======
        adivina()
>>>>>>> d242c27 (Corregir estructura y agregar carpeta WEEK_5)

    vector = random.randint(0, entrada1)


<<<<<<< HEAD
    return vector, entrada1

def adivina2(vector, entradas):


    print(f"vector:   {vector}")

    while True:

        try: 
        
            entrada1 = int(input("Guess:  "))

            verifica = entrada1 % 1

            if entrada1 == vector:

                print("Just Right")
                break


            elif entrada1 > entradas:

                print("Too Large")

            elif entradas > entrada1:

                print("Too Small")


            elif verifica > 0:

                print("float")

            verifica = entrada1 % 1

        
        except ValueError: # aqui verifica que no sea string
        
            print("String")
        

def main():

    vector, entradas= adivina()
    adivina2(vector, entradas)

main()
=======
    return vector

def adivina2(vector):


    
    
    guess = int(input("Guess:  "))




    
    ...


def main():

    ...
>>>>>>> d242c27 (Corregir estructura y agregar carpeta WEEK_5)


            

            



