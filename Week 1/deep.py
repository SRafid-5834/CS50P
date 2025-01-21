# Deep Thought

def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    print(answer_to_life(user_input))


def answer_to_life(answer: str):
    match answer:
        case "42" | "forty two" | "forty-two":
            return "Yes"
        case _:
            return "No"


if __name__ == "__main__":
    main()
