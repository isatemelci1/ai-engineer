def main():
    number = int(input("Enter a number: "))
    if is_even(number):
        print("Even.")
    else:
        print("Odd.")


def is_even(n):
    return n % 2 == 0


if __name__ == "__main__":
    main()