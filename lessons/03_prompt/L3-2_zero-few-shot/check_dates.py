"""normalize_date が、いろいろな形の日付を 2024-01-05 の形にそろえられるかを数える。

    python lessons/03_prompt/L3-2_zero-few-shot/check_dates.py
"""
from booklib.dates import normalize_date

CASES = [
    ("2024-01-05", "2024-01-05"),
    ("2024/1/5", "2024-01-05"),
    ("2024/01/05", "2024-01-05"),
    ("20240105", "2024-01-05"),
    ("2024.1.5", "2024-01-05"),
    ("2024年1月5日", "2024-01-05"),
    ("2023年12月31日", "2023-12-31"),
    ("令和6年1月5日", "2024-01-05"),
    ("令和元年5月1日", "2019-05-01"),
    ("平成31年4月30日", "2019-04-30"),
    ("R6.1.5", "2024-01-05"),
    ("H30.12.1", "2018-12-01"),
]


def main() -> None:
    ok = 0
    for text, expected in CASES:
        try:
            got = normalize_date(text)
        except Exception as e:  # noqa: BLE001
            got = f"{type(e).__name__}"
        mark = "○" if got == expected else "×"
        ok += got == expected
        print(f"{mark} {text!r:22} → {got!r}")
    print(f"\n{len(CASES)}件中 {ok}件 通りました")


if __name__ == "__main__":
    main()
