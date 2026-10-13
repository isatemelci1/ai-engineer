import random


def main():
    level = get_positive_int("Level: ")
    number = random.randint(1, level)

    while True:
        guess = get_positive_int("Guess: ")

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break


def get_positive_int(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            pass
        else:
            if number > 0:
                return number


if __name__ == "__main__":
    main()