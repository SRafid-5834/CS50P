# Playback Speed

def main():
    user_input = answer("Enter your answer here >> ")
    print(change_space(user_input))


def change_space(sentence):
    return sentence.replace(" ", "...")


main()
