# Just setting up my twttr

# print("Output:", "".join([i for i in user_input if i.lower() not in "aeiou"])) does the same as below
def main():
    user_input = input("Input: ")
    print("Output: ", end="")
    for i in user_input:
        if i.lower() not in "aeiou":
            print(i, end="")
    print()


if __name__ == "__main__":
    main()

