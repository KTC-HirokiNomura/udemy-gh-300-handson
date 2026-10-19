# -*- coding: utf-8 -*-
# 蔵書の CSV を読んで、著者ごとの冊数の報告を書き出すスクリプト（古い書き方のまま）
import os
import sys


def load_books(path):
    books = []
    f = open(path, "r", encoding="utf-8")
    lines = f.readlines()
    f.close()
    i = 0
    for line in lines:
        if i == 0:
            i = i + 1
            continue
        parts = line.strip().split(",")
        book = {}
        book["id"] = int(parts[0])
        book["title"] = parts[1]
        book["author"] = parts[2]
        book["published"] = int(parts[4])
        books.append(book)
        i = i + 1
    return books


def summary(books):
    total = 0
    authors = {}
    for b in books:
        total = total + 1
        if b["author"] in authors.keys():
            authors[b["author"]] = authors[b["author"]] + 1
        else:
            authors[b["author"]] = 1
    lines = []
    lines.append("蔵書の数: %d" % total)
    keys = list(authors.keys())
    keys.sort()
    for k in keys:
        lines.append("%s: %d冊" % (k, authors[k]))
    return "\n".join(lines)


def write_report(books, out_dir):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    path = os.path.join(out_dir, "report.txt")
    f = open(path, "w", encoding="utf-8")
    f.write(summary(books))
    f.close()
    return path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使い方: python legacy/old_report.py data/books.csv")
        sys.exit(1)
    print(write_report(load_books(sys.argv[1]), "out"))
