import os
import sys

from PIL import Image, ImageOps


VALID_EXTENSIONS = [".jpg", ".jpeg", ".png"]
SHIRT = os.path.join(os.path.dirname(__file__), "shirt.png")


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input output")

    input_extension = os.path.splitext(sys.argv[1])[1].lower()
    output_extension = os.path.splitext(sys.argv[2])[1].lower()

    if input_extension not in VALID_EXTENSIONS or output_extension not in VALID_EXTENSIONS:
        sys.exit("Invalid file extension")

    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(sys.argv[1]) as photo:
            with Image.open(SHIRT) as shirt:
                photo = ImageOps.fit(photo, shirt.size)
                photo.paste(shirt, shirt)
                photo.save(sys.argv[2])

    except FileNotFoundError as e:
        sys.exit(f"Could not open {e.filename}")


if __name__ == "__main__":
    main()