def main():
    percentage = get_percentage("Fraction: ")
    print(gauge(percentage))


def get_percentage(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            fraction = int(x) / int(y)
        except (ValueError, ZeroDivisionError):
            continue
        if 0 <= fraction <= 1:
            return round(fraction * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()