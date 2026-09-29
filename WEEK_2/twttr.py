vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
texto = input("INPUT: ")
resultado = "".join([char for char in texto if char not in vocales])
print(resultado)


