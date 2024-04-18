from datetime import datetime

def get_difference_in_days(first: datetime, second: datetime) -> int:
    """Returns the difference in days between two dates."""
    return (first - second).days

def get_days_from_today(date: str) -> int:
    """Returns the difference in days between today and provided date.
    
    Keyword arguments:
        date: date in format 'YYYY-MM-DD'"""
    try:
        parsed_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError("Provided date can't be properly parsed") from e

    return get_difference_in_days(datetime.now(), parsed_date)
