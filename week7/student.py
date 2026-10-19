class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    #Getter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name

    #Getter
    @property
    def house(self):
        return self._house

    #Setter
    @house.setter
    def house(self, house):
        if house not in ["Harran", "Urfa", "Hoevelaken", "Nijkerk"]:
            raise ValueError("Wrong house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()