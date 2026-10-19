"""貸出と返却。"""
from dataclasses import dataclass
from datetime import date, timedelta

from booklib.catalog import Catalog

LOAN_DAYS = 14  # 貸出の期間（日）


@dataclass
class Loan:
    book_id: int
    member_id: int
    borrowed_on: date
    due_on: date
    returned_on: date | None = None


class LoanService:
    def __init__(self, catalog: Catalog) -> None:
        self._catalog = catalog
        self._loans: list[Loan] = []

    def borrow(self, book_id: int, member_id: int, today: date) -> Loan:
        loan = Loan(book_id, member_id, today, today + timedelta(days=LOAN_DAYS))
        self._loans.append(loan)
        return loan

    def return_book(self, book_id: int, today: date) -> Loan:
        for loan in self._loans:
            if loan.book_id == book_id and loan.returned_on is None:
                loan.returned_on = today
                return loan
        raise ValueError(f"蔵書 ID {book_id} は貸出中ではありません")

    def on_loan(self) -> list[Loan]:
        return [loan for loan in self._loans if loan.returned_on is None]

    def overdue(self, today: date) -> list[Loan]:
        return [loan for loan in self.on_loan() if loan.due_on < today]
