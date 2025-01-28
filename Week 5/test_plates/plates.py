# plates.py


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # s = s.strip().upper()
    if s.isalnum() and (1 < len(s) < 7) and s[:2].isalpha():
        if len(s) == 2:
            return True
        elif len(s) > 2:
            t = s[2:]
            for i in range(len(t)):
                if t[i].isalpha():
                    pass
                elif t[i].isdigit():
                    if t[i] == '0':
                        return False
                    elif t[i:].isdigit():
                        return True
                    else:
                        return False
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    main()
