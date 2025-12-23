def main():
    input_str = input("Please provide your input: ")
    converted_str = convert(input_str)
    print(converted_str)


def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")


main()
