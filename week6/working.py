import re


def main():
    print(convert(input("Hours: ")))


def to_24_hour(hour, minute, period):
    hour = int(hour)
    minute = int(minute) if minute is not None else 0

    if not 1 <= hour <= 12 or not 0 <= minute <= 59:
        raise ValueError

    hour %= 12
    if period == "PM":
        hour += 12

    return f"{hour:02}:{minute:02}"


def convert(s):
    pattern = r"([0-9]{1,2})(?::([0-9]{2}))? (AM|PM) to ([0-9]{1,2})(?::([0-9]{2}))? (AM|PM)"
    match = re.fullmatch(pattern, s)

    if not match:
        raise ValueError

    start_hour, start_min, start_period, end_hour, end_min, end_period = match.groups()

    start = to_24_hour(start_hour, start_min, start_period)
    end = to_24_hour(end_hour, end_min, end_period)

    return f"{start} to {end}"


if __name__ == "__main__":
    main()
