def main():
    greeting = input("Greeting: ").strip().lower()
    print(f"${value(greeting)}")


def value(greeting):
    lower_greeting = greeting.lower()

    if lower_greeting.startswith('hello'):
        return 0
    elif lower_greeting.startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
