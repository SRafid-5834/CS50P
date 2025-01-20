# Einstein

def main():
    user_input = int(answer("m: "))
    print(f"E: {energy(user_input)}")


def energy(mass):
    return mass * (300000000 * 300000000)


main()
