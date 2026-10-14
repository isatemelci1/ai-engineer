def main():
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    avg = average(first_number, second_number)
    sum = total(first_number, second_number)
    diff = difference(first_number, second_number)

    print(f"Average of {first_number:.2f} and {second_number:.2f} is: {avg:.2f}")
    print(f"Total of {first_number:.2f} and {second_number:.2f} is: {sum:.2f}")
    print(f"Difference of {first_number:.2f} and {second_number:.2f} is: {diff:.2f}")


def average(a, b):
    return total(a, b) / 2


def total(a, b):
    return a + b


def difference(a, b):
    return a - b


if __name__ == "__main__":
    main()