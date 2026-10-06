def main():
    while True:
        try:
            fuel = input("Diga cuanta gasolina tiene su tanque: ")
            porcentaje = convert(fuel)
            resultado = gauge(porcentaje)
            print(resultado)
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    primero = fraction[0]
    segundo = fraction[2]
    
    if primero.isdigit() and segundo.isdigit():
        primero = int(primero)
        segundo = int(segundo)
        
        if segundo == 0:
            raise ZeroDivisionError
        if primero > segundo:
            raise ValueError
            
        division = primero / segundo
        porcentaje = round(division * 100)
        return porcentaje
    else:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()