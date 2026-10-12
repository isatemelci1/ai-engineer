from cat import get_positive_int

def main():
    size = get_positive_int()
    print_square(size)


def print_square(size):
    for _ in range(size):
        print("#" * size)

if __name__ == "__main__":
    main()