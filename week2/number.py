def main():
    x = get_integer()
    print(f"x is {x}")


def get_integer():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            pass  # Ignore the error and prompt again
        else:
            return x


if __name__ == "__main__":
    main()