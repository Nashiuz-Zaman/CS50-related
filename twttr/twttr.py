def main():
    vowels = ["a", "e", "i", "o", "u"]
    str_to_change = input("Input: ")
    print(f"Output: {remove_chars(str_to_change, vowels)}")


def remove_chars(str, chars):
    changed_str = str

    for char in chars:
        changed_str = changed_str.replace(char, "")
        changed_str = changed_str.replace(char.upper(), "")

    return changed_str


main()
