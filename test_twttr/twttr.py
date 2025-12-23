def main():
    str_to_change = input("Input: ")
    print(f"{shorten(str_to_change)}")


def shorten(word):
    vowels = "aeiouAEIOU"

    new_word = []
    for letter in word:
        if letter not in vowels:
            new_word.append(letter)

    return "".join(new_word)


if __name__ == "__main__":
    main()
