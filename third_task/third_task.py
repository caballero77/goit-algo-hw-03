import re

def normalize_phone(phone_number: str) -> str:
    """Normalize phone number to +380XXXXXXXXX (Ukraine) format.
    
    Args:
        phone_number: str: phone number in any format."""
    
    phone_number = re.sub(r'[^0-9]', '', phone_number)
    if len(phone_number) == 9: # number without country code
        phone_number = '+380' + phone_number
    elif len(phone_number) == 10 and phone_number[0] == "0": # number without country code but with 0 at the beginning
        phone_number = '+38' + phone_number
    elif len(phone_number) == 12: # number with country code
        phone_number = '+' + phone_number
    else:
        raise ValueError('Invalid phone number')
    return phone_number