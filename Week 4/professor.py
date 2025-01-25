# Little Professor

import random


def main():
    score = 0
    lvl = get_level()
    for _ in range(10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        flag = False
        for _ in range(3):
            try:
                answer = int(input(f'{x} + {y} = '))
                if answer == (x + y):
                    score += 1
                    flag = True
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                continue
        if not flag:
            print(f'{x} + {y} = {x + y}')
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: ").strip())
            if n in (1, 2, 3):
                return n
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
