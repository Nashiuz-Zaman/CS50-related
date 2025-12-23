def main():
    while True:
        try:
            x, y = get_fraction()

            if x <= y:
                find_remaining_fuel_amount(x, y)
                break

        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def get_fraction():
    fractions = input("Fraction: ").strip().split("/")
    x = int(fractions[0])
    y = int(fractions[1])
    return [x, y]


def find_remaining_fuel_amount(n1, n2):
    percentage = round((n1 / n2) * 100)

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


main()
