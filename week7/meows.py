class Cat:
    MEOWS = 5

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()



def meows(n: int):
    for _ in range(n):
        print("meow")


number: int = int(input("Enter the number of meows: "))
meows(number)