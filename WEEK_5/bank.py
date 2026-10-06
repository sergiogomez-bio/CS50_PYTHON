def main():
    greeting = input("Greeting:")
    dev = value(greeting)
    print(dev)


def value(greeting):
    
    if greeting == "hello" or greeting == "Hello":

        return "$0"
    
    elif  greeting.startswith("h") or greeting.startswith("H"):

        return "$20"

    else:
        return "$100" 


if __name__ == "__main__":
    main()