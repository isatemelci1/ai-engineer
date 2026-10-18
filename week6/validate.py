
import re

def main():

    email = input("What's your email? ").strip().lower()

    if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|org|net|nl)$", email, re.IGNORECASE):
        print("valid")
    else:
        print("invalid")

if __name__ == "__main__":
    main()