"""蔵書と利用者のデータ。"""
from dataclasses import dataclass, field


@dataclass
class Book:
    id: int
    title: str
    author: str
    isbn: str
    published: int  # 出版年
    tags: list[str] = field(default_factory=list)


@dataclass
class Member:
    id: int
    name: str
