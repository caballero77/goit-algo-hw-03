
from datetime import datetime, timedelta
from first_task import get_difference_in_days, get_days_from_today
import pytest

@pytest.mark.parametrize("start,end,expected", [
    ("2024-01-10", "2024-01-09", 1),
    ("2024-01-10", "2024-01-01", 9),
    ("2024-01-1", "2024-01-10", -9),
    ("2024-01-01", "2023-01-01", 365),
    ("2021-01-01", "2020-01-01", 366),
    ("4000-01-01", "4000-01-01", 0),
    ("0001-01-01", "0001-01-01", 0),
])
def test_first_task(start: str, end: str, expected: int):
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    assert get_difference_in_days(start, end) == expected

@pytest.mark.parametrize("delta", [
    timedelta(days=10),
    timedelta(days=-20),
    timedelta(days=12, hours=100),
    timedelta()
])
def test_first_task_with_dependencies(delta: timedelta):
    date = datetime.now() - delta
    assert get_days_from_today(date.strftime("%Y-%m-%d")) == delta.days

def test_first_task_with_exception():
    with pytest.raises(ValueError):
        get_days_from_today("not a correct date")