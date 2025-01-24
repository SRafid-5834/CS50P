# Outdated

def main():
    print(get_input("Date: "))


def get_input(prompt):
    while True:
        try:
            user_input = input(prompt).strip()
            if len(user_input.split("/")) > 1:
                if not user_input.split("/")[0].isalpha():
                    temp = validate_1(user_input)
                    if not temp:
                        continue
                    else:
                        return temp
                else:
                    continue
            elif len(user_input.split(" ")) > 1:
                if user_input.split(" ")[0].isalpha() and ("," in user_input):
                    temp = validate_2(user_input.lower().title())
                    if not temp:
                        continue
                    else:
                        return temp
                else:
                    continue
        except ValueError:
            continue


def validate_1(date):
    l = date.split("/")
    if (0 < int(l[0]) < 13) and (0 < int(l[1]) < 32) and (0 < int(l[2])):
        return f'{l[2]:0>4}-{l[0]:0>2}-{l[1]:0>2}'
    else:
        return False


def validate_2(date):
    months = [
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
        "December"
    ]
    l = date.split(" ")

    if (l[0] in months) and (0 < int(l[1][:-1]) < 32) and (0 < int(l[2])):
        return f'{l[2]:0>4}-{months.index(l[0])+1:0>2}-{l[1][:-1]:0>2}'
    else:
        return False


if __name__ == '__main__':
    main()