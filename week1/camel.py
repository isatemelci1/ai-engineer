def main():
    camel_case = input("camelCase: ")
    snake_case = get_snake_case(camel_case)
    print("snake_case:", snake_case)

def get_snake_case(camel_case):
    snake_case = []
    for s in camel_case:
        if s.isupper():
            snake_case.append("_")
        snake_case.append(s.lower())
    return "".join(snake_case)

if __name__ == "__main__":
    main()