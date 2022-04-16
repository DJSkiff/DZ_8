from datetime import date, datetime, timedelta
from unittest import result

users = [
    {
        "name": "Bill",
        "birthday": "1998-02-13"
    },
    {
        "name": "Giil",
        "birthday": "1999-02-12"
    },
    {
        "name": "Till",
        "birthday": "2000-02-15"
    },
    {"name": "Billi",
        "birthday": "1998-03-08"
     },
    {"name": "Billii",
        "birthday": "1998-02-10"
     }
]


def convert_day(str_date: str) -> date:
    current_year = datetime.now().year
    d = datetime.strptime(str_date, '%Y-%m-%d')
    return datetime(current_year, d.month, d.day).date()


def get_birthdays_per_week(users):

    end_week = datetime.today().date() + timedelta(7)
    end_list = []
    resul = {}
    # print(end_week)
    for user in users:
        current_date_birt = convert_day(user.get('birthday'))
        if current_date_birt >= datetime.today().date() and current_date_birt <= end_week:
            end_list.append(user)
    for user in end_list:
        key = convert_day(user.get('birthday')).strftime('%A')
        if key in ('Sunday', 'Saturday'):
            key = 'Monday'
        if resul.get(key):
            resul[key].append(user.get('name'))
        else:
            resul[key] = [user.get("name")]
    # print(resul)
    result_list = []
    for key, value in resul.items():
        result_list.append(f'{key}: {value}')
        resul = ';'.join(result_list)
    print(resul)

    # print(current_date_birt.weekday())
    # print(d.date())
    # print(d.weekday())


get_birthdays_per_week(users)
