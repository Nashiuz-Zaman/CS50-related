import random
import sys


def main():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level > 0:
                break

    random_int = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess > 0:
                if guess > random_int:
                    print("Too large!")
                elif guess < random_int:
                    print("Too small!")
                else:
                    sys.exit("Just right!")


main()
