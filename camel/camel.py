def main():
    camel_str = input("camelCase: ")
    print(convert_to_snake_case(camel_str))


def convert_to_snake_case(str):
    result_str_list = []

    for char in str:
        result_str_list.append(char) if not char.isupper(
        ) else result_str_list.append("_" + char.lower())

    return "".join(result_str_list)


main()
