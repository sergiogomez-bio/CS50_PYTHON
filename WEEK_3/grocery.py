def entrada_lista():

    lista=[]

    while True:

        try :

            grocery = input("que desea agregar a la lista:    ")
            grocery = grocery.upper()
            lista.append(grocery)
            compare = lista
            
            
        except EOFError: 

            lista = sorted(list(set(lista)))
            listas = organizar_arreglo(lista, compare)
            for vs in range(len(listas)):
                print(listas[vs])

            break
            
        except ZeroDivisionError:
            
            print("")
            
        except ValueError:
            
            print("")
    
        except TypeError:
    
            print("")

def organizar_arreglo(sinrepetir, repetida):

    completote = []

    for vc in range( len(sinrepetir) ):

        
        cantidad = repetida.count(sinrepetir[vc])
        print(f"count {cantidad}")
        completote.append(f"{cantidad}:  {sinrepetir[vc]}")

    return completote

def main():

    entrada_lista()

main()
