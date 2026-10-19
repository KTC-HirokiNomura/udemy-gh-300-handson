from datetime import date

from booklib.dates import parse_date


def test_parse_date():
    assert parse_date("2024-01-05") == date(2024, 1, 5)
