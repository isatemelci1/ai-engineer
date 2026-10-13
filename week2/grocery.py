def main():
    grocery_list = {}

    while True:
        try:
            item = input().lower()
        except EOFError:
            break

        grocery_list[item] = grocery_list.get(item, 0) + 1

    print()
    for food in sorted(grocery_list):
        print(f"{grocery_list[food]} {food.upper()}")


if __name__ == "__main__":
    main()