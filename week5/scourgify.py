import csv
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Both filenames must end in .csv")

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            rows = list(reader)

    except FileNotFoundError as e:
        sys.exit(f"Could not open {e.filename}")

    for row in rows:
        if "," not in row["name"]:
            sys.exit(f"Invalid name: {row['name']}")

        last, first = row["name"].split(",", 1)
        row["first"] = first.strip()
        row["last"] = last.strip()

    try:
        with open(sys.argv[2], "w", newline="") as output:
            writer = csv.DictWriter(
                output,
                fieldnames=["first", "last", "house"]
            )
            writer.writeheader()

            for row in rows:
                writer.writerow({
                    "first": row["first"],
                    "last": row["last"],
                    "house": row["house"]
                })

    except FileNotFoundError as e:
        sys.exit(f"Could not open {e.filename}")


if __name__ == "__main__":
    main()