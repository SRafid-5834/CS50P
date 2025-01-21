# Math Interpreter

def main():
    user_input = input("Expression: ").strip()
    print(calculator(user_input))


# can be done simpler by using eval()
def calculator(exp):
    x, y, z = exp.split(" ")
    x, z = float(x), float(z)

    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z


if __name__ == "__main__":
    main()
