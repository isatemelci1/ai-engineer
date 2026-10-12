def main():
    number = get_positive_int()
    for _ in range(number):
        print("meow")


def get_positive_int():
    while True:
        number = int(input("Number: "))
        if number > 0:
            return number


if __name__ == "__main__":
    main()