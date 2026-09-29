MATH = input("Expression:")



def CALCULADORA(MATH):

    if MATH.find("+") >= 0:

        pos = MATH.find("+")

        # EXTRAYENDO LA DATA DE ANTES DEL MAS 
        MATHANTES = MATH[:pos]
        MATHANTES = float(MATHANTES)

        # EXTREYENDO LA DATA POSTERIOR
        MATHPOST = MATH[pos+1:]
        MATHPOST = float(MATHPOST)

        print(MATHANTES + MATHPOST)

    elif MATH.find("/") >= 0:

        pos = MATH.find("/")
        
        # EXTRAYENDO LA DATA DE ANTES DEL MAS 
        MATHANTES = MATH[:pos]
        MATHANTES = float(MATHANTES)
        
        # EXTREYENDO LA DATA POSTERIOR
        MATHPOST = MATH[pos+1:]
        MATHPOST = float(MATHPOST)

        print(MATHANTES/MATHPOST)

    elif MATH.find("*") >= 0:
    
        pos = MATH.find("*")
            
        # EXTRAYENDO LA DATA DE ANTES DEL MAS 
        MATHANTES = MATH[:pos]
        MATHANTES = float(MATHANTES)
            
        # EXTREYENDO LA DATA POSTERIOR
        MATHPOST = MATH[pos+1:]
        MATHPOST = float(MATHPOST)

        print(MATHANTES*MATHPOST)

    elif MATH.find("-") >= 0:
        
        pos = MATH.find("-")
                
        # EXTRAYENDO LA DATA DE ANTES DEL MAS 
        MATHANTES = MATH[:pos]
        MATHANTES = float(MATHANTES)
                
        # EXTREYENDO LA DATA POSTERIOR
        MATHPOST = MATH[pos+1:]
        MATHPOST = float(MATHPOST)

        print(MATHANTES-MATHPOST)

    else:

        print("que operación es esta")

CALCULADORA(MATH)