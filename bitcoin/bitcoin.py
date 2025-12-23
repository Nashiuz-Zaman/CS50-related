import sys
import requests


def main():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        else:
            bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    except requests.RequestException:
        sys.exit("Error")
    else:
        converted_usd = res["bpi"]["USD"]["rate_float"] * bitcoins
        print(f"${converted_usd:,.4f}")


main()
