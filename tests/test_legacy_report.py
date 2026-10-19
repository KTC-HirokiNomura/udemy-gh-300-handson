"""legacy/old_report.py の振る舞いを固定するテスト（L7-1 で書き直した後も通ることを確かめる）。"""
import importlib.util

from conftest import ROOT

spec = importlib.util.spec_from_file_location("old_report", ROOT / "legacy" / "old_report.py")
old_report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old_report)


def test_load_books(books_csv):
    books = old_report.load_books(str(books_csv))
    assert len(books) == 50
    assert books[0] == {"id": 1, "title": "Python 入門ノート", "author": "宮本 健", "published": 2000}


def test_summary(books_csv):
    lines = old_report.summary(old_report.load_books(str(books_csv))).splitlines()
    assert lines[0] == "蔵書の数: 50"
    assert lines[1:] == sorted(lines[1:])
    assert sum(int(line.split(": ")[1].rstrip("冊")) for line in lines[1:]) == 50


def test_write_report(books_csv, tmp_path):
    path = old_report.write_report(old_report.load_books(str(books_csv)), str(tmp_path / "out"))
    with open(path, encoding="utf-8") as f:
        assert f.read().startswith("蔵書の数: 50")
