def main():
    percentage = get_percentage("Fraction: ")
    print(gauge(percentage))


def get_percentage(prompt):
    while True:
        try:
            percentage = convert(input(prompt))
        except (ValueError, ZeroDivisionError):
            continue
        else:
            return percentage


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if x < 0 or y < 0:
        raise ValueError("X and Y must be non-negative")
    if y == 0:
        raise ZeroDivisionError("Y cannot be zero")
    if x > y:
        raise ValueError("X cannot be greater than Y")

    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()