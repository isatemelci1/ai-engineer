def main():
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    if get_response(answer):
        print("Yes")
    else:
        print("No")


def get_response(answer):
    match answer.strip().lower():
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False

        
if __name__ == "__main__":
    main()