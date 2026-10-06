def main():
    plate = input("Plate: ")

    if is_valid(plate):

        print("Valid")

    else:

        print("Invalid")

def is_valid(s):
    
    stringsito=""
    charsito = ""
    otrochar=""

    if len(s) >= 6 and  s.isalnum()==False: # aqui elimina las dos condiciones de longitud y caracteres alfanumericos

        return False

    elif len(s) <= 6 and len(s) >=2 : # aqui valida que cumpla la primer condicion que tenga una longitud menor a 6

        for vc in range(2): # aqui hace un ciclo para recorrer el strinG en sus dos primeros caracteres

            if vc <= 2:

                stringsito = stringsito + s[vc]
                
    
        if stringsito.isalpha(): # aqui revisa si esos dos primeros caracteres son letras

             
            charsito = s[-1]

            if charsito.isalpha(): # aqui revisa si el ultimo caracter es un numero

                return False

            else:

                otrochar=s[2:]

                if otrochar.find("0") == 0: # aqui se revisa si cumple la condicion de que no comience con cero despues de la posicion 1 

                    return False

                else:

                    return True


        else: # si no son letras devuevle falso 
            
          
            return False

main()