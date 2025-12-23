def main():
    x, y, z = input("Expression: ").split(" ")

    if y == "+":
        print(convert_to_float(int(x) + int(z)))
    elif y == "-":
        print(convert_to_float(int(x) - int(z)))
    elif y == "/":
        print(convert_to_float(int(x) / int(z)))
    else:
        print(convert_to_float(int(x) * int(z)))


def convert_to_float(str):
    return round(float(str), 1)


main()
