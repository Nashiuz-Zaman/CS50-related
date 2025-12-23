def main():
    time = input("What time is it? ").strip()
    convertedTime = convert(time)

    if convertedTime >= 7 and convertedTime <= 8:
        print("breakfast time")
    elif convertedTime >= 12 and convertedTime <= 13:
        print("lunch time")
    elif convertedTime >= 18 and convertedTime <= 19:
        print("dinner time")


def convert(time):
    hrs, mins = time.split(":")
    convertedMins = int(mins) / 60
    return float(int(hrs) + convertedMins)


if __name__ == "__main__":
    main()
