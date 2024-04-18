from datetime import datetime

def get_next_birthday(today, birth_date):
    """Get next birthday date for user. If birthday is already passed this year, return next year's date.
    
    Args:
        today (datetime): current date
        birth_date (datetime): user's birth date
    """
    birth_date = birth_date.replace(year=today.year)
    if birth_date < today:
        birth_date = birth_date.replace(year=today.year + 1)
    return birth_date

def get_next_weekday(date):
    """If birthday is on weekend, move it to the nearest weekday of next week."""
    if date.weekday() == 5: # Saturday
        date = date.replace(day=date.day + 2)
    elif date.weekday() == 6: # Sunday
        date = date.replace(day=date.day + 1)
    return date

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        next_birthday = get_next_birthday(today, datetime.strptime(user['birthday'], "%Y.%m.%d").date())
        if (next_birthday - today).days <= 7:
            upcoming_birthdays.append({'name': user['name'], 'congratulation_date': get_next_weekday(next_birthday).strftime("%Y.%m.%d")})
    return upcoming_birthdays