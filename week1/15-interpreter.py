def main():
    expression = input("Expression: ")

    x, y, z = expression.split(" ")

    result = calculate(x, y, z)

    if result is not None:
        print(f"{result:.1f}")
    else:
        print("Invalid operation or division by zero.")


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
        if z == 0:
            return None
        else:
            return x / z
    else:
        return None


if __name__ == "__main__":
    main()