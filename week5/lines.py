import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1]) as file:
            count = 0

            for line in file:
                if is_code_line(line):
                    count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count)


def is_code_line(line):
    line = line.lstrip()
    return line != "" and not line.startswith("#")


if __name__ == "__main__":
    main()