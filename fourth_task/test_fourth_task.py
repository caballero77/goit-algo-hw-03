from fourth_task import get_upcoming_birthdays, get_next_weekday, get_next_birthday
from datetime import datetime
import pytest
from freezegun import freeze_time

@pytest.mark.parametrize('date, expected', [
    ("2024-04-15", "2024-04-15"),
    ("2024-04-16", "2024-04-16"),
    ("2024-04-17", "2024-04-17"),
    ("2024-04-18", "2024-04-18"),
    ("2024-04-19", "2024-04-19"),
    ("2024-04-20", "2024-04-22"),
    ("2024-04-21", "2024-04-22"),
    ("2024-04-22", "2024-04-22"),
    ("2024-04-23", "2024-04-23"),
    ("2024-04-24", "2024-04-24"),
])
def test_handle_weekend(date, expected):
    assert get_next_weekday(datetime.strptime(date, "%Y-%m-%d")) == datetime.strptime(expected, "%Y-%m-%d")

@pytest.mark.parametrize('today, date, expected', [
    ("2024-04-16", "1991-04-17", "2024-04-17"),
    ("2024-04-16", "1991-04-15", "2025-04-15"),
    ("2024-04-16", "2024-04-17", "2024-04-17"),
    ("2024-04-16", "1991-09-12", "2024-09-12"),
    ("2024-04-16", "1991-01-01", "2025-01-01"),
])
def test_get_next_birthday(today, date, expected):
    assert get_next_birthday(datetime.strptime(today, "%Y-%m-%d"), datetime.strptime(date, "%Y-%m-%d")) == datetime.strptime(expected, "%Y-%m-%d")

@pytest.mark.parametrize('users, expected', [
    ([
        {"name": "John Doe", "birthday": "1985.02.13"},
        {"name": "Jane Smith", "birthday": "1990.02.17"}
    ], [
        {'name': 'John Doe', 'congratulation_date': '2024.02.13'}, 
        {'name': 'Jane Smith', 'congratulation_date': '2024.02.19'}
    ]),
    ([
        {"name": "John Doe", "birthday": "1985.02.13"},
        {"name": "Jane Smith", "birthday": "1990.01.17"}
    ], [
        {'name': 'John Doe', 'congratulation_date': '2024.02.13'},
    ]),
    ([
        {"name": "John Doe", "birthday": "1985.03.13"},
        {"name": "Jane Smith", "birthday": "1990.01.17"}
    ], []),
    ([
        {"name": "John Doe", "birthday": "1985.02.13"},
        {"name": "Jane Smith", "birthday": "1990.02.19"},
        {"name": "Kentaro Miura", "birthday": "1966.02.20"},
        {'name': 'Leeroy Jenkins', 'birthday': "2005.05.11"},
        {'name': 'Rick Astley', 'birthday': "1996.02.06"}, #https://www.youtube.com/watch?v=dQw4w9WgXcQ
    ], [
        {'name': 'John Doe', 'congratulation_date': '2024.02.13'},
        {'name': 'Jane Smith', 'congratulation_date': '2024.02.19'}
    ]),
])
@freeze_time("2024-02-12")
def test_get_upcoming_birthdays(users, expected):
    assert get_upcoming_birthdays(users) == expected