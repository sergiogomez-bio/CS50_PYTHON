def main():
    print("Amount Due: 50")
    Coke_Machine()

def Coke_Machine():

    costo = 50

    while True:

        if costo <= 0:
        
            print(f"Change Owed:  {costo}")
            break

        receive = int(input("Insert Coin:  "))
        if receive == 25:
            costo = costo - 25
            print(f"Amount Due: {costo}")

        elif receive == 10:
            costo = costo - 10
            print(f"Amount Due:{costo}")
        
        elif receive == 5:
            costo = costo - 5
            print(f"Amount Due: {costo}")
            
        else: 
            print("money is not correct")

        



main()


    





