# CS50 P-Shirt

from PIL import Image, ImageOps
import os.path
import sys


def main():
    check_input()

    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as img:
            img = ImageOps.fit(img, shirt.size)
            img.paste(shirt, shirt)
            img.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


def check_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file_1, file_1_type = sys.argv[1], os.path.splitext(sys.argv[1])[1]
    file_2, file_2_type = sys.argv[2], os.path.splitext(sys.argv[2])[1]
    types = (".jpg", ".jpeg", ".png")

    if file_1_type not in types:
        sys.exit("Invalid input")
    elif file_2_type not in types:
        sys.exit("Invalid output")
    elif file_1_type != file_2_type:
        sys.exit("Input and output have different extensions")



if __name__ == '__main__':
    main()
