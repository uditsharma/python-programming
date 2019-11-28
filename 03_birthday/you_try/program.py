import datetime


def print_header():
    print('-------------------------')
    print('          BIRTHDAY APP')
    print('-------------------------')


def get_birthday_from_user():
    print("Tell us when you were born")
    year = int(input("Year [YYYY]"))
    month = int(input("Month [MM]"))
    date = int(input("Date [DD]"))
    bday = datetime.datetime(year, month, date)
    return bday


def compute_days_between_dates(original_date, now):
    date = datetime.datetime(now.year, original_date.month, original_date.day)
    dt = date - now
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days


def print_birthday_message(days):
    if days > 0:
        print("Your Birthday is in {} days !! ".format(days))
    elif days < 0:
        print("You had your birthday {} ago !!".format(-days))
    else:
        print("Happy Birthday !!")


def main():
    print_header()
    birth_day = get_birthday_from_user()
    now = datetime.datetime.now()
    days = compute_days_between_dates(birth_day, now)
    print_birthday_message(days)


main()
