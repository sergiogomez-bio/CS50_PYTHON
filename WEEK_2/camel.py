def main():
    CAMEL = input("camelCase:  ")
    conversion(CAMEL)

def conversion(CAMEL):
    compare = CAMEL.lower()
    position = []
    if CAMEL == compare:
        print(f"snake_case: {CAMEL}")

    else:
        for rev in range(len(CAMEL)):
            if CAMEL[rev] != compare[rev]:
                position.append(rev)
        cont=0
        for rev2 in range(len(position)):
                pos = position[rev2]
                pos = pos + cont
                otro = CAMEL[pos]
                CAMEL= CAMEL[:pos] + f"_{otro}" + CAMEL[pos+1:]
                cont = cont + 1

        print(f"snake_case: {CAMEL}")

main()

