"""日付の文字列を扱う。"""
from datetime import date


def parse_date(text: str) -> date:
    # 2024-01-05 の形だけを読む
    return date.fromisoformat(text)


def normalize_date(text: str) -> str:
    """日付の文字列の形をそろえる。"""
    raise NotImplementedError  # L3-2 で Copilot に書いてもらう
