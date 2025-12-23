def main():
    plate = input("Plate: ")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s.isalnum():
        return False
    elif not (s[0].isalpha() and s[1].isalpha()):
        print("Failed alphabetical check")
        return False

    numeric = ""

    for i in range(len(s)):
        if s[i].isdigit():
            numeric = s[i:]
            break

    if len(numeric) >= 1:
        if numeric[0] == "0" or not numeric.isdigit():
            return False

    return True


if __name__ == "__main__":
    main()
