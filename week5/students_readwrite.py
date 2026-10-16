import csv
import os

def main():

    name = input("What is your name? ").strip()
    city = input("What city are you in? ").strip()

    if not name or not city:
        print("Name and city cannot be empty.")
        return

    file_exists = os.path.isfile("names.csv")

    with open("names.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "city"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({"name": name, "city": city})

    try:
        students = []
        with open("names.csv") as file:
            reader = csv.DictReader(file)
            students = list(reader)
    except FileNotFoundError:
        print("The file 'names.csv' was not found.")
        return

    for student in sorted(students, key=lambda student: student["city"].lower()):
        print(f"{student['name']} is in {student['city']}")


if __name__ == "__main__":
    main()