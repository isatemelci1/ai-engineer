import random
import sys
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # Validate command-line arguments
    if len(sys.argv) == 1:
        font = random.choice(fonts)

    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")

        if sys.argv[2] not in fonts:
            sys.exit("Invalid font")

        font = sys.argv[2]

    else:
        sys.exit("Usage: python3 figlet.py [-f FONT]")

    # Set font and print text
    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()