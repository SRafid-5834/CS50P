# twttr.py

def main():
    print(f'Output: {shorten(input("Input: "))}')


def shorten(word):
    return ''.join(i for i in word if i.lower() not in 'aeiou')
    # s = ''
    # for i in word:
    #     if i.lower() not in "aeiou":
    #         s += i
    # return s


if __name__ == "__main__":
    main()
