from third_task import normalize_phone
import pytest

@pytest.mark.parametrize("phone_number,normalized", [
    ("067\\t123 4567", '+380671234567'),
    ("(095) 234-5678\\n", '+380952345678'),
    ("+38 (050) 12-34-567", '+380501234567'),
    ("+38050123-45-67", '+380501234567'),
    ("0501234567", '+380501234567'),
    ("+38(050)123-32-34", '+380501233234'),
    ("0503451234", '+380503451234'),
    ("(050)8889900", '+380508889900'),
    ("38050-111-22-22", '+380501112222'),
    ("38050 111 22 11   ", '+380501112211'),
    ("Number: +38 050 123-45-67", '+380501234567'),
    ("+38 050 123-45-67", '+380501234567'),
    ("+380501234567", '+380501234567'),
    ("+38{050}/123/45/67 deewfew", '+380501234567'),
])
def test_third_task(phone_number, normalized):
    assert normalize_phone(phone_number) == normalized

@pytest.mark.parametrize("phone_number", [
    "not a phone number",
    "1234567890123456",
    "12345678901234",
    "+2803243544554664",
    "+38501234567",
])
def test_third_task_with_exception(phone_number):
    with pytest.raises(ValueError):
        normalize_phone(phone_number)