# Seasons of Love

from datetime import date
import inflect
import sys


def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid birthdate.")

    total_mins = calc_mins(date.today(), birth_date)
    p = inflect.engine()
    print(f"{p.number_to_words(total_mins, andword='').capitalize()} minutes")


def calc_mins(today, birth):
    return (today - birth).days * 24 * 60


if __name__ == "__main__":
    main()
