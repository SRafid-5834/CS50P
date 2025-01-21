# Meal Time

def main():
    user_input = input("What time is it? ").strip()
    val = convert(user_input)
    if 7 <= val <= 8:
        print("breakfast time")
    elif 12 <= val <= 13:
        print("lunch time")
    elif 18 <= val <= 19:
        print("dinner time")


# does not account for am and pm
# can be easily done by splitting and adding 12 if pm in time
def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes)/60


if __name__ == "__main__":
    main()
