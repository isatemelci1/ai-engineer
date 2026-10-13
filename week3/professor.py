import random

NUM_PROBLEMS = 10
MAX_TRIES = 3
LEVELS = [1, 2, 3]


def main():
    level = get_level()
    score = 0

    for _ in range(NUM_PROBLEMS):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        for _ in range(MAX_TRIES):
            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                continue

            if guess == answer:
                score += 1
                break
            else:
                print("EEE")
        else:
            print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if level in LEVELS:
                return level


def generate_integer(level):
    if level not in LEVELS:
        raise ValueError("Invalid level")

    lower = 0 if level == 1 else 10 ** (level - 1)
    upper = 10 ** level - 1

    return random.randint(lower, upper)


if __name__ == "__main__":
    main()