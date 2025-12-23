import random


def main():
    problems = []
    level = get_level()
    for i in range(10):
        n1 = generate_integer(level)
        n2 = generate_integer(level)
        solution = n1 + n2

        problems.append({"n1": n1, "n2": n2, "solution": solution})

    # keep track of score initializing it as 0
    score = 0

    # loop through problems list
    for problem in problems:
        # for each problem 3 tries are allowed
        for i in range(3):
            try:
                # if input equals to solution then increase score by 1 and break out of the loop
                if problem["solution"] == int(
                    input(f"{problem["n1"]} + {problem['n2']} = ")
                ):
                    score += 1
                    break
                # if input is not equal and this is the last try then print the correct answer and break otherwise give another chance
                else:
                    raise ValueError
            except ValueError:
                if i == 2:
                    print(f"{problem["n1"]} + {problem["n2"]
                                               } = {problem["solution"]}")
                    break
                else:
                    print("EEE")
                    pass

    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
