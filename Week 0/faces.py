# Making Faces

def main():
    user_input = answer("Enter your answer here >> ")
    print(convert(user_input))


def convert(sentence):
    return sentence.replace(":)", "🙂").replace(":(", "🙁")


main()
