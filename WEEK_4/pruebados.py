import random

def main():

    operaciones = 0
    resultado = 0
    level = 0
    level = get_level(level)
    while operaciones < 10:

        X, Y = generate_integer(level)
        #print(f"x: {X}")
        #print(f"y: {Y}")
        suma = get_suma(X, Y, cont=0)
        #print(f"suma : {suma}")
        resultado = resultado + suma
        operaciones = operaciones + 1
        print(operaciones)


    print(f"este es tu resultado {resultado}")

def get_suma(X, Y, cont=0):

    level = int(input(f"{X} + {Y} = "))
    resultado = X + Y
    
    try:

        if cont > 3: 
        
            print(f" este es el resultado {resultado}")
            return 0

        verifica = resultado % 1
    
        if verifica >= 1: # verifica que no sea un float o decimal
    
            # level = int(input(f"{X} + {Y} = "))
            #print("1")
            return get_suma(X, Y, cont+1)
    
        elif level < 0: # verifica que no sea un negativo
    
            # level = int(input(f"{X} + {Y} = "))
            #print("2")
            return get_suma(X, Y, cont+1)

        elif level != resultado:

            # level = int(input(f"{X} + {Y} = "))
            #print("3")
            return get_suma(X, Y, cont+1)

        elif level == resultado:

            return 1

        
    except ValueError: # verifica que no ingrese un string
    
        level = int(input(f"{X} + {Y} = "))
        print("5")
        return get_suma(X, Y, cont+1)

    
def get_level(level):

    level = int(input("Level: "))

    try:

        verifica = level % 1
        print(verifica)

        if verifica >= 1: # verifica que no sea un float o decimal

            level = int(input("level:  "))
            get_level(level)

        elif 0 > level >= 3: # verifica que sea menor a 3

            level = int(input("level:  "))
            get_level(level)

    
    except ValueError: # verifica que no ingrese un string

        level = int(input("level:  "))
        get_level(level)


    return level

def generate_integer(level):

    
    if level == 1:

        vector = 10

    elif level == 2: 

        vector = 100

    elif level == 3:

        vector = 1000

    Xn = random.randrange(0, vector)
    Yn = random.randrange(0, vector)

    return Xn, Yn

if __name__ == "__main__":
    main()