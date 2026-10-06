def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dofloat = float(d)
    return dofloat


def percent_to_float(p):
    dofloat = p
    dofloat = dofloat.replace("%","")
    dofloat = float(dofloat)
    dofloat = dofloat/100
    return dofloat 


main()