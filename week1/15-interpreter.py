def main():
    expression = input("Expression: ")

    try:
        x, y, z = expression.split(" ")
    except ValueError:
        print("Invalid format. Use spaces, like: 1 + 1")
        return

    try:
        result = calculate(x, y, z)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Both operands must be numbers.")
    else:
        if result is None:
            print("Invalid operator. Use +, -, * or /.")
        else:
            print(f"{result:.1f}")


def calculate(x, y, z):
    x = float(x)
    z = float(z)

    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z
    else:
        return None


if __name__ == "__main__":
    main()