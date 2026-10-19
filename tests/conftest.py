from pathlib import Path

import pytest

from booklib.catalog import Catalog, load_catalog
from booklib.models import Book

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def books_csv() -> Path:
    return ROOT / "data" / "books.csv"


@pytest.fixture
def small_catalog() -> Catalog:
    catalog = Catalog()
    catalog.add_book(Book(1, "Python 入門ノート", "青木 葵", "000-0-0000-0001", 2020, ["python", "入門"]))
    catalog.add_book(Book(2, "はじめての Git", "石川 健", "000-0-0000-0002", 2018, ["git", "入門"]))
    catalog.add_book(Book(3, "海辺の図書室", "青木 葵", "000-0-0000-0003", 2015, ["小説"]))
    return catalog


@pytest.fixture
def full_catalog(books_csv: Path) -> Catalog:
    return load_catalog(books_csv)
