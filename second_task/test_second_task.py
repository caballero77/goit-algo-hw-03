from second_task import get_numbers_ticket
import pytest

def is_sorted(arr):
    """Check if the list is sorted in ascending order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def has_unique_elements(arr):
    """Check if the list has only unique elements."""
    return len(arr) == len(set(arr))

@pytest.mark.parametrize("min,max,quantity,condition", [
   (1, 1000, 5, lambda x: is_sorted(x) and has_unique_elements(x) and len(x) == 5),
   (-1, 10, 1, lambda x: len(x) == 0),
   (5, 1001, 5, lambda x: len(x) == 0),
   (-23, 1000000, 12, lambda x: len(x) == 0),
   (15, 3, 3, lambda x: len(x) == 0),
   (1, 1000, 1000, lambda x: is_sorted(x) and has_unique_elements(x) and len(x) == 1000),
   (1, 1000, 1001, lambda x: len(x) == 0),
   (1, 1000, 0, lambda x: len(x) == 0),
   (1, 1, 1, lambda x: x == [1]),
   (1, 1, 0, lambda x: len(x) == 0),
   (1, 1, 2, lambda x: len(x) == 0),
   (1, 49, 6, lambda x: is_sorted(x) and has_unique_elements(x) and len(x) == 6),
])
def test_second_task(min, max, quantity, condition):
      assert condition(get_numbers_ticket(min, max, quantity))