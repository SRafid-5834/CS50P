# Fuel Gauge

def main():
    val = round(process_input("Fraction: ") * 100)

    if val <= 1:
        print("E")
    elif val >= 99:
        print("F")
    else:
        print(f'{val}%')


def process_input(prompt):
    while True:
        x = input(prompt).split("/")
        print(int(x[0]) / int(x[1]))
        try:
            if not (int(x[0]) > int(x[1])):
                return int(x[0]) / int(x[1])
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == '__main__':
    main()
