
from datetime import date, datetime
import sys
import inflect
import re


def main():
    birth_date = input("Date of Birth: ").strip()
    date_info_list = validate_date(birth_date)

    if date_info_list == None:
        sys.exit("Invalid Date")

    date_obj = get_birth_date_obj(date_info_list)

    mins = calculate_minutes(date_obj)
    p = inflect.engine()
    print(p.number_to_words(mins, andword="").capitalize() + ' minutes')


def get_birth_date_obj(list):
    return datetime(int(list[0]), int(list[1]), int(list[2]), 0, 0, 0)


def validate_date(date_str):
    if re.search(r"\d{4}-\d{2}-\d{2}", date_str):
        year, month, day = date_str.split('-')
        return [year, month, day]


def calculate_minutes(birth_date):
    year, month, day = str(date.today()).split('-')
    today = datetime(int(year), int(month), int(day), 0, 0, 0)
    time_delta = today - birth_date

    return time_delta.days * 24 * 60


if __name__ == "__main__":
    main()
