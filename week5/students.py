def main():

    # with open("names.csv") as file:
    #     for line in file:
    #         name, city =line.rstrip().split(",")
    #         print(f"{name} is in {city}")

    # students = []
    # with open("names.csv") as file:
    #     for line in file:
    #         name, city = line.rstrip().split(",")
    #         students.append((name, city))

    # for name, city in students:
    #     print(f"{name} is in {city}")

    students = []
    with open("names.csv") as file:
        for line in file:
            name, city = line.rstrip().split(",")
            # student = {}
            # student["name"] = name
            # student["city"] = city

            student = {"name": name, "city": city}
            students.append(student)

    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['city']}")

#     for student in sorted(students, key=get_name):
#         print(f"{student['name']} is in {student['city']}")


# def get_name(student):
#     return student["name"]


if __name__ == "__main__":
    main()