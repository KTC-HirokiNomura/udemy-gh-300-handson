from booklib.report import format_book, format_catalog


def test_format_book(small_catalog):
    assert format_book(small_catalog.get(1)) == "Python 入門ノート／青木 葵（2020年）"


def test_format_catalog(small_catalog):
    lines = format_catalog(small_catalog.all_books()).splitlines()
    assert len(lines) == 3
    assert lines[2] == "海辺の図書室／青木 葵（2015年）"
