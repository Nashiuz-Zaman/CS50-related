def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s.isalnum():
        return False
    elif not (s[0].isalpha() and s[1].isalpha()):
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


main()
