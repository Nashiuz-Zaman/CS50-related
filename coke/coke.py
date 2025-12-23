def main():
    paid = 0

    while paid < 50:
        print(f"Amount Due: {50 - paid}")
        amount_given = int(input("Insert Coin: "))

        if amount_given == 25 or amount_given == 10 or amount_given == 5:
            paid = paid + amount_given

    print(f"Change Owed: {paid - 50}")


main()
