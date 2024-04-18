import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """Returns a list of unique and sorted random numbers in the range from min to max inclusive.
    If the input data is incorrect, returns an empty list.
    
    Args:
        min (int): minimum value of the range
        max (int): maximum value of the range
        quantity (int): the number of random numbers in the list"""
    if min < 1 or max > 1000 or min > max or quantity < 1 or quantity > max-min+1:
        return []
    
    result = sorted(random.sample(range(min, max + 1), quantity))

    return result