def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        starts_with_two_letters(s) and 
        has_valid_length(s) and
        has_valid_numbers(s) and
        has_no_punctuation(s)
    )


def starts_with_two_letters(s):
    return s[0:2].isalpha()


def has_valid_length(s):
    return 2 <= len(s) <= 6


def has_valid_numbers(s):
    found_digit = False
    for char in s:
        if char.isdigit():
            if not found_digit and char == "0":
                return False
            found_digit = True
        elif found_digit:
            return False
    return True


def has_no_punctuation(s):
    return s.isalnum()


if __name__ == "__main__":
    main()