def main():
    while True:
        try:
            result = get_date(months)
            if result != False:
                break

        except ValueError:
            pass

    year, month, day = result
    print(f"{year}-{month:02}-{day:02}")


def get_date(list_of_months):

    date = input("Date: ")
    date_list = date.split("/")

    # check if the date string is of first type
    if len(date_list) == 3:
        month = int(date_list[0])
        day = int(date_list[1])
        year = int(date_list[2])

        if month <= 12 and day <= 31:
            return [year, month, day]
        else:
            return False

    # check if the date string is of second type
    else:
        date_list = date.split(" ")

        if len(date_list) == 3:
            month = date_list[0]

            if "," not in date_list[1]:
                return False
            day = int(date_list[1].replace(",", ""))
            year = int(date_list[2])

            if day <= 31 and list_of_months.index(month) <= 11:
                return [year, list_of_months.index(month) + 1, day]

            else:
                return False
        else:
            return False


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

main()
