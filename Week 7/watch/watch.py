# Watch on YouTube

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if x := re.search(r'^<iframe.*src="https?://(?:www\.)?youtube\.com/embed/([^"]+)".*', s):
        return f'https://youtu.be/{x.group(1)}'
    else:
        return None


if __name__ == "__main__":
    main()
