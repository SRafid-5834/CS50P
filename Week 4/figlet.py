# Frank, Ian and Glen’s Letters


from pyfiglet import Figlet
import random
import sys

figlet = Figlet()


def main():

    if len(sys.argv) == 1:
        fig_out(random.choice(figlet.getFonts()))
    elif len(sys.argv) == 3:
        a, b = sys.argv[1], sys.argv[2]
        if (a in ['-f', '--font']) and (b in figlet.getFonts()):
            fig_out(b)
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")




def fig_out(f):
    figlet.setFont(font=f)
    print(f'Ouput:\n{figlet.renderText(input("Input: "))}')


if __name__ == '__main__':
    main()
