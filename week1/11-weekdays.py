def main():
    day = input("Enter a day: ")
    if get_day_type(day) != None:
        print(get_day_type(day))
    else:
        print("Invalid day.")

def get_day_type(day):
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday."
        case "saturday" | "sunday":
            return "Weekend."
        case _:
            return None


if __name__ == "__main__":
    main()