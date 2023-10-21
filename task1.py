from datetime import datetime, date, timedelta
from collections import defaultdict
import calendar


def get_birthdays_per_week(users: list[dict]):
    upcoming_birthdays = defaultdict(list)
    for user in users:
        birthday: date = user["birthday"].date()

        # Determine the user's next birthday
        today = datetime.today().date()

        try:
            next_birthday = birthday.replace(year=today.year)

            if next_birthday <= today:
                next_birthday = next_birthday.replace(
                    year=next_birthday.year + 1)
        except ValueError:
            # Handle the 29 February problem. For simplicity ignore such users
            continue

        # Determine the date to congratulate (move to Monday if the birthday is on a weekend)
        date_to_congratulate = next_birthday

        if date_to_congratulate.weekday() in {5, 6}:
            days_until_monday = 7 - next_birthday.weekday()
            date_to_congratulate = date_to_congratulate + \
                timedelta(days=days_until_monday)

        # Skip if the date to congratulate is more than 7 days away
        if (date_to_congratulate - today).days > 7:
            continue

        # Add a record to the collection
        weekday_to_congratulate = date_to_congratulate.weekday()
        upcoming_birthdays[weekday_to_congratulate].append(user["name"])

    # Print next week's birthdays
    for weekday, day_name in zip(range(0, 7), calendar.day_name):
        if weekday not in upcoming_birthdays:
            continue

        user_names = ", ".join(upcoming_birthdays[weekday])
        print(f"{day_name}: {user_names}")
