import inflect


def main():
    inflector = inflect.engine()
    names = []

    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            break

        names.append(name.strip())

    print("Adieu, adieu, to", inflector.join(names))


if __name__ == "__main__":
    main()