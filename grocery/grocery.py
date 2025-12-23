def main():
    items = {}
    add_items(items)

    sorted_keys = sorted(items)

    for key in sorted_keys:
        print(f"{items[key]} {key}")


def add_items(items):
    while True:
        try:
            item_name = input("").upper()

            if item_name not in items:
                items[item_name] = 1
            else:
                items[item_name] += 1

        except KeyError:
            pass
        except EOFError:
            print()
            break


main()
