# NUMB3RS


import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip.strip()):
        a, b, c, d = ip.split(".")
        return (0 <= int(a) <= 255) and (0 <= int(b) <= 255) and (0 <= int(c) <= 255) and (0 <= int(d) <= 255)
    else:
        return False


if __name__ == "__main__":
    main()
