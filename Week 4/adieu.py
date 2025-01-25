# Adieu, Adieu

import inflect


def main():
    name_list = []
    while True:
        try:
            user_input = input("Name: ").strip().title()
            name_list.append(user_input)
        except EOFError:
            print("Adieu, adieu, to", inflect.engine().join(name_list))
            break


if __name__ == '__main__':
    main()
