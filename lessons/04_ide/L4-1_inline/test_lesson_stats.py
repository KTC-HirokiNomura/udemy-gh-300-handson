"""L4-1 で Copilot の提案から書いた stats.py を確かめるテスト。

    pytest lessons/04_ide/L4-1_inline
"""
from booklib.models import Book
from booklib.stats import count_by_author, titles_by_year

BOOKS = [
    Book(1, "Python 入門ノート", "青木 葵", "000-0-0000-0001", 2020),
    Book(2, "はじめての Git", "石川 健", "000-0-0000-0002", 2018),
    Book(3, "海辺の図書室", "青木 葵", "000-0-0000-0003", 2015),
]


def test_count_by_author():
    assert count_by_author(BOOKS) == {"青木 葵": 2, "石川 健": 1}


def test_count_by_author_empty():
    assert count_by_author([]) == {}


def test_titles_by_year():
    assert titles_by_year(BOOKS) == ["海辺の図書室", "はじめての Git", "Python 入門ノート"]
