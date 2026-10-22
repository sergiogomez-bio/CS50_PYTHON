
import csv
import sys


def main():
  before, after = is_a_file()
  file = open_file(before)
  organiza_data(file, after)


def is_a_file():
  # Ajustado para que cuente bien los 3 argumentos (script + entrada + salida)
  if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
  elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
  return sys.argv[1], sys.argv[2]


def open_file(archivo):
  try:
    with open(archivo, "r") as csvfile:
      filecito = csv.DictReader(csvfile)
      filas = list(filecito)
      return filas

  except FileNotFoundError:
    # Mensaje exacto que exige check50 cuando el archivo no existe
    sys.exit(f"Could not read {sys.argv[1]}")


def create_file(file):
  column = ["first", "last", "house"]

  # Lo abri sin with para que no se cierre antes de tiempo y devolvemos ambos
  archivo = open(file, "w", newline="")
  escritor = csv.DictWriter(archivo, column)
  escritor.writeheader()
  return archivo, escritor


def organiza_data(file, after):
  # Recibi el archivo abierto y el escritor de tu función
  archivo, escritor = create_file(after)

  for filita in file:
    nombres = filita["name"]
    apellido, nombre = nombres.split(", ")
    casita = filita["house"]

    # Arreglado: DictWriter exige un diccionario, no variables sueltas
    escritor.writerow({"first": nombre, "last": apellido, "house": casita})

  # Cierro el archivo al terminar
  archivo.close()
  return escritor


if __name__ == "__main__":
  main()