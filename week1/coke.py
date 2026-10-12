VALID_COINS = [25, 10, 5]
PRICE = 50


def main():
    amount_due = PRICE

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin in VALID_COINS:
            amount_due -= coin

    print(f"Change Owed: {-amount_due}")


if __name__ == "__main__":
    main()