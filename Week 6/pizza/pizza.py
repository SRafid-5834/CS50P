# Pizza Py

import csv
import sys
from tabulate import tabulate


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1]) as file:
            print(tabulate(csv.DictReader(file), headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist.")


if __name__ == '__main__':
    main()
