CALORIES = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "lime": 20,
    "peach": 60,
    "pear": 100,
    "plums": 70,
    "tangerine": 50,
    "watermelon": 80,
}

def main():
    fruit = input("Item: ").strip().lower()
    calories = CALORIES.get(fruit)
    if calories is not None:
        print(f"Calories: {calories}")

if __name__ == "__main__":
    main()