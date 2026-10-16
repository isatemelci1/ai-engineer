import csv

def main():

    try:
        students = []
        with open("names.csv") as file:
        # reader = csv.reader(file)
        # for name, city in reader:
        #     students.append({"name": name, "city": city})
            reader = csv.DictReader(file)
            students = list(reader)
        # for row in reader:
        #     students.append({"name": row["name"], "city": row["city"]})
    except FileNotFoundError:
        print("The file 'names.csv' was not found.")
        return

    for student in sorted(students, key=lambda student: student["city"].lower()):
        print(f"{student['name']} is in {student['city']}")


if __name__ == "__main__":
    main()