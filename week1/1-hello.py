print("Hello, World!")

# ask user input for name
name = input("Enter your name: ")

# Remove white spaces from the name
name = name.strip()

# Capitalize the first letter of the name
name = name.capitalize()

# capitalize the first letter of each word in the name
name = name.title()

# ask user input for city
city = input("Enter your city: ").strip().title()

# print a personalized greeting
print("Hello, " + name + " from " + city + "!")

print("Hello,", name)

print("Hello, ", end="")
print(name)

print("Hello,", name, sep='***')

print(f"Hello, {name} from {city}!")