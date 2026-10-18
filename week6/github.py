import re


def get_username(url):
    match = re.fullmatch(
        r"(https?://)?(www\.)?github\.com/([A-Za-z0-9-]+)",
        url
    )

    if match is None:
        return None

    return match.group(3)


# test py

def test_valid_urls():
    assert get_username("https://github.com/isatemelci1") == "isatemelci1"
    assert get_username("http://github.com/isatemelci1") == "isatemelci1"
    assert get_username("github.com/isatemelci1") == "isatemelci1"
    assert get_username("https://www.github.com/isatemelci1") == "isatemelci1"


def test_invalid_urls():
    assert get_username("https://gitlab.com/isatemelci1") is None
    assert get_username("https://githubXcom/isatemelci1") is None
    assert get_username("https://github.com/") is None
    assert get_username("not a URL") is None


def test_extra_path_or_query():
    assert get_username("https://github.com/isatemelci1/") is None
    assert get_username("https://github.com/isatemelci1?tab=repositories") is None
