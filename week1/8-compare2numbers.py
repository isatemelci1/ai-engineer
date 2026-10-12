def main():
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    print(compare_numbers(first_number, second_number))

def compare_numbers(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    elif a < b:
        return f"{a} is less than {b}"
    else:
        return f"{a} is equal to {b}"

main()