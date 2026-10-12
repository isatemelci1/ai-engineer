VOWELS = "aeiou"

def main():
    text = input("Input: ")
    no_vowels = shorten(text)
    print("Output:", no_vowels)


def shorten(text):
    result = []
    for char in text:
        if char.lower() not in VOWELS:
            result.append(char)
    return "".join(result)

if __name__ == "__main__":
    main()