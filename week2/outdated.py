from datetime import date

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def convert_date(date_string):
    """Convert a supported date string to YYYY-MM-DD, or return None."""
    try:
        if "/" in date_string:
            month, day, year = map(int, date_string.split("/"))
        else:
            month_day, year = date_string.split(",")
            month_name, day = month_day.strip().split()
            month = MONTHS.index(month_name.title()) + 1
            day = int(day)
            year = int(year.strip())

        parsed_date = date(year, month, day)
        return parsed_date.isoformat()

    except (ValueError, TypeError):
        return None


def main():
    while True:
        try:
            date_string = input("Date: ").strip()
        except EOFError:
            return

        converted_date = convert_date(date_string)

        if converted_date is not None:
            print(converted_date)
            return


if __name__ == "__main__":
    main()