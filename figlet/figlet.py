from pyfiglet import Figlet
import sys
import random


def main():
    arg_len = len(sys.argv)

    # if 1 arg provided
    if arg_len == 1:
        figlet, font_list = init_and_get_font_list()

        # get a random font
        random_font = random.choice(font_list)
        figlet.setFont(font=random_font)

        str = input("Input: ")
        print(f"Output: \n {figlet.renderText(str)}")

    # if 3 args provided
    elif arg_len == 3:
        figlet, font_list = init_and_get_font_list()
        first_arg = sys.argv[1]
        font_name = sys.argv[2]
        # print(font_name not in font_list)
        # sys.exit()

        # check 1st arg
        if first_arg != '-f' and first_arg != '--font':
            exit_with_message()
        # check if font is valid
        elif font_name not in font_list:
            exit_with_message()
        else:
            figlet.setFont(font=font_name)
            str = input("Input: ")
            print(f"Output: \n {figlet.renderText(str)}")
    else:
        exit_with_message()


def init_and_get_font_list():
    figlet = Figlet()
    font_list = figlet.getFonts()

    return [figlet, font_list]


def exit_with_message():
    sys.exit("Invalid usage")


main()
