import re

def is_valid_postcode(postcode: str) -> bool:
    postcode = postcode.upper()
    return bool(re.fullmatch(r"[1-9][0-9]{3} ?[A-Z]{2}", postcode))


def test_is_valid_postcode():
    assert is_valid_postcode("3861 AB")
    assert is_valid_postcode("3861AB")
    assert is_valid_postcode("3861 ab")
    assert is_valid_postcode("1234 XY")

    assert not is_valid_postcode("0861 AB")
    assert not is_valid_postcode("386 AB")
    assert not is_valid_postcode("3861 ABC")
    assert not is_valid_postcode("3861 AB\n")
    assert not is_valid_postcode("٣861 AB")