def bank():
    Hello = input("Greeting:")
    if Hello == "hello" or Hello == "Hello":
        print ("$0")
    elif  Hello.startswith("h") or Hello.startswith("H"):
        print("$20")
    else:
        print("100")


bank()





