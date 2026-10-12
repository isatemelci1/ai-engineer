names = ["Alice", "Bob", "Charlie", "Bob", "Eve"]

print("List of names:")
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

print("\nList of names using range:")
for i in range(len(names)):
    print(f"{i + 1}. {names[i]}")