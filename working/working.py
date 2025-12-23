import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^((?:[1-9]|1[0-2])(?:\:[0-5][0-9])? (?:AM|PM)) to ((?:[1-9]|1[0-2])(?:\:[0-5][0-9])? (?:AM|PM))$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError

    start_time = convert_to_24hrformat(match.group(1))
    end_time = convert_to_24hrformat(match.group(2))

    return f"{start_time} to {end_time}"


def convert_to_24hrformat(time):
    actual_time, period = time.split(" ")
    h, m = (actual_time.split(":") + ["00"])[:2]

    h = int(h)
    if period == "AM":
        h = 0 if h == 12 else h
    else:
        h = h if h == 12 else h + 12

    return f"{h:02}:{m}"


if __name__ == "__main__":
    main()
