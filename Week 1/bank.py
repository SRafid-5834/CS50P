# Home Federal Savings Bank

def main():
    user_input = input("Enter your answer here >> ").lower().strip()
    print(check_greeting(user_input))


def check_greeting(greeting):
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
