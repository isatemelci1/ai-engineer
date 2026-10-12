def main():
    number = get_positive_int()
    for _ in range(number):
        print("meow")


def get_positive_int():
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Please enter a valid number.")
        else:
            if number > 0:
                return number
            print("Please enter a positive integer greater than 0.")

if __name__ == "__main__":
    main()