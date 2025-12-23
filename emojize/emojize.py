import emoji


def main():

    emoji_str = input("Input ").strip().lower()
    print(emoji.emojize(f"Output: {emoji_str}", language="alias"))


main()
