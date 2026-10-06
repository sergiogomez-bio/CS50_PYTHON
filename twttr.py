def main():
    texto = input("INPUT: ")


def shorten(word):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    resultado = "".join([char for char in word if char not in vocales])
    return resultado

if __name__ == "__main__":
    main()