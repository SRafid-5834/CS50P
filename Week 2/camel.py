# camelCase

# print("snake_case:", "".join(["_" + i.lower() if i.isupper() else i for i in user_input])) does the same as below
def main():
    user_input = input("camelCase: ")
    print("snake_case: ", end="")
    for i in user_input:
        if i.isupper():
            print(f"_{i.lower()}", end="")
        else:
            print(i, end="")
    print()


if __name__ == "__main__":
    main()
