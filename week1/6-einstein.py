def main():
    user_mass = int(input("Enter your mass in kilograms: "))
    print(einstein(user_mass))

def einstein(mass):
    c = 300000000  # speed of light in m/s
    return mass * c**2

if __name__ == "__main__":
    main()