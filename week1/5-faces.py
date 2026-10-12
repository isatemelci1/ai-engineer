def main():
    user_input = input("Enter some words: ")
    print(convert(user_input))

def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

if __name__ == "__main__":
    main()