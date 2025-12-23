import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r"<iframe[ \"\w\=]*?src=\"(?:https?://(?:www\.)?youtube\.com/embed/(\w+))\"[ \"\w\=]*?></iframe>"

    match = re.search(regex, s)
    if not match:
        return None
    else:
        return f"https://youtu.be/{match.group(1)}"


if __name__ == "__main__":
    main()
