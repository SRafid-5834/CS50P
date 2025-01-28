# fuel.py

def main():
    print(gauge(convert(input("Fraction: "))))


def convert(fraction):
    while True:
        x, y = fraction.split("/")
        if not x.isdigit() or not y.isdigit():
            raise ValueError("Please input valid numbers.")
        if int(y) == 0:
            raise ZeroDivisionError("Divisor cannot be zero.")
        if int(x) > int(y):
            raise ValueError("Please input valid numbers.")

        return round((int(x) / int(y)) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
