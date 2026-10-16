import sys

def main():
    name = input("What is your name? ").strip()

    if not name:
        sys.exit("Name cannot be empty.")

    with open("names.txt", "a") as file:
        file.write(f"{name}\n")

    names = []
    with open("names.txt", "r") as file:
        for line in file:
            names.append(line.rstrip())

    for person in sorted(names, key=str.lower, reverse=True):
        print(f"Hello, {person}")


if __name__ == "__main__":
    main()