from validator_collection import checkers


def main():
    email_provided = input("What's your email address? ")

    if checkers.is_email(email_provided) == True:
        print("Valid")
    else:
        print("Invalid")


main()
