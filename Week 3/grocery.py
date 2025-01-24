# Grocery List

def main():
    d = {}
    while True:
        try:
            item = input().upper()
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        except KeyError:
            pass
        except EOFError:
            break

    for i in sorted(d):
        print(f'{d[i]} {i}')


if __name__ == '__main__':
    main()
