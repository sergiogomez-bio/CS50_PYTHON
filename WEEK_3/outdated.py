
def corregir_fecha():

    meses = {

    "January"  : 1,
    "February" : 2,
    "March"    : 3,
    "April"    : 4,
    "May"      : 5,
    "June"     : 6,
    "July"     : 7,
    "August"   : 8,
    "September": 9,
    "October"  : 10,
    "November" : 11,
    "December" : 12 }

    posiciones = []

    while True:

        try: 

            fecha = input("Date:  ")


            if fecha.count("/") == 2:
                
                anio = fecha[-4:]
                
                
                for vc in range(len(fecha)):

                    
                    if fecha[vc] == "/":

                        posiciones.append(vc)

                if posiciones[0] == 1:

                    mes = "0" + fecha[0]

                else: 

                    mes = fecha[0:1]

                if posiciones[1] == 3:

                    dia = "0" + fecha[2]

                else:

                    dia = fecha[3:4]

                
                print(f"{anio}-{mes}-{dia}")



            elif fecha.count(" ") >=2:

                anio = fecha[-4:]
                #print(anio)
                pos = []
                for vc in range(len(fecha)):

                    if fecha[vc] == " ":
                        
                        pos.append(vc)

                if pos[0] == 2:

                    dia = fecha[0:1]

                else:

                    dia = fecha[0]
                 
                mes = fecha[:pos[0]]
                dia = fecha[pos[0]+1:pos[1]-1]

                print(f"{anio}-{meses.get(mes)}-{dia}")
                break
            

        except EOFError: 
        
            break
                    
        except ZeroDivisionError:
                    
            print("")
                    
        except ValueError:
                    
            print("")
            
        except TypeError:
            
            print("")


    

def main():

    corregir_fecha()

main()
