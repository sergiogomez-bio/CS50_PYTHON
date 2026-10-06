import random


def main():

    level = int(input("level:  "))
    level = get_level(level)
    generate_integer(level)


def get_level(level):

    
    try:
        
        verifica = level % 1

        if verifica > 1: # verifica que no sea un float o decimal

            level = int(input("level:  "))
            get_level(level)

        elif 0 < level <= 3: # verifica que no sea un negativo o igual a cero o mayor a 3 

            level = int(input("level:  "))
            get_level(level)
    
    except ValueError: # verifica que no ingrese un string

        level = int(input("level:  "))
        get_level(level)


    return level

def veri_input(numero, texto, contador = 0):

    if contador >= 3:
    
        return True , contador

    try:
        
        textito = texto
        verifica = numero % 1


        if verifica < 1: # verifica que no sea un float o decimal

            numero = int(input(f"{textito}  "))
            veri_input(numero, textito, contador + 1)

        elif numero <= 0: # verifica que no sea un negativo o igual a cero

            numero = int(input(f"{textito}  "))
            veri_input(numero, textito, contador + 1)
    
    except ValueError: # verifica que no ingrese un string

        numero = int(input(f"{textito}  "))
        veri_input(numero, textito, contador + 1)

    return numero, 0



def generate_integer(level):

    vector = random.randrange(0, level)
    Xn = random.randint(vector)
    Yn = random.randint(vector)
    

    return Xn, Yn

def Veri_operation(level):

    contmal = 0
    contbien = 0

    
    while contbien < 10:

        Xn,Yn = generate_integer(level)
        consult = int(input(f"{Xn} + {Yn} = "))
        texto = f"{Xn} + {Yn} = "
        numero, condicion = veri_input(consult, texto)
        if condicion == True:

            result = Xn + Yn
            while numero != result or contmal < 3:
                contmal =+ 1
                if numero != result:
                    print("EEE")
                    consult = int(input(f"{Xn} + {Yn} = "))
                    numero = veri_input(consult, texto)
        
        contbien += 1





        

            

    

if __name__ == "__main__":
    main()