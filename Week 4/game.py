# Guessing Game

import random


def main():
    while True:
        try:
            n = int(input("Level: ").strip())
            if n < 1:
                continue
            else:
                break
        except ValueError:
            pass


    g = random.randint(1, n)
    while True:
        try:
            guess = int(input("Guess: ").strip())
            if guess < 1:
                continue
            else:
                if guess < g:
                    print("Too small!")
                elif guess > g:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        except ValueError:
            pass


if __name__ == '__main__':
    main()
