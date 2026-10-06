def main():
    time = input("¿Que hora es?")
    convert(time)


def convert(time):
    pos = time.find(":")
    hora = float(time[:pos])
    minutos = float(time[pos+1:])
    flomin = minutos/60

    if 7<=hora<=8:
        print("Breakfast Time")

    elif 12<=hora<=13:
        print("Meal Time")

    elif 18<=hora<=19:
        print("Dinner Time")

    else:

        print("no comas engordas")

if __name__ == "__main__":
    main()


def main():
    counts = {}
    words = get_words("address.txt")

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            Counts[word] = 1

save_counts(counts)