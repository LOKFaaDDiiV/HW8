from datetime import *
from collections import defaultdict
import re

users = [
        {"name": "human1", 
        "birthday": datetime(year=1988, month=1, day=26)
        },
        {"name": "human2", 
        "birthday": datetime(year=1998, month=1, day=26)
        },
        {"name": "human3", 
        "birthday": datetime(year=2001, month=1, day=22 )
        }
    ]


def get_birthdays_per_week(list_of_dicts):
    """Колхзная версия"""
    current_date = datetime.now()
    birthdays = defaultdict(list)
    for human in list_of_dicts:
        bd = human["birthday"]
        counter = 0
        while counter < 7:
            check_date = current_date + timedelta(days=counter)
            if check_date.month == bd.month and check_date.day  == bd.day:
                if check_date.weekday() == 5 or check_date.weekday() == 6:
                    if current_date.weekday() != 0:
                        birthdays["Monday"].append(human["name"])
                else:
                    birthdays[check_date.strftime('%A')].append(human["name"])
            counter += 1 
    for i, j in birthdays.items():
        print(i+':', re.sub(r"[\[\]']", "", str(j)))

get_birthdays_per_week(users)
