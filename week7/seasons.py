
import sys
from datetime import date

import inflect


def minutes_between(birth, today):
    delta = today - birth
    return delta.days * 24 * 60


def minutes_in_words(minutes):
    engine = inflect.engine()
    words = engine.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"


def main():
    birth_string = input("Date of Birth: ")

    try:
        birth = date.fromisoformat(birth_string)
        if birth.isoformat() != birth_string:
            raise ValueError
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()

    if birth > today:
        sys.exit("Date of birth cannot be in the future")

    minutes = minutes_between(birth, today)
    print(minutes_in_words(minutes))


if __name__ == "__main__":
    main()
