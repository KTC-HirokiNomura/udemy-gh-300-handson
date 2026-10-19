from datetime import date

import pytest

from booklib.loans import LOAN_DAYS, LoanService


def test_borrow_sets_due_date(small_catalog):
    service = LoanService(small_catalog)
    loan = service.borrow(1, 10, date(2024, 4, 1))
    assert loan.due_on == date(2024, 4, 15)
    assert LOAN_DAYS == 14


def test_return_book(small_catalog):
    service = LoanService(small_catalog)
    service.borrow(1, 10, date(2024, 4, 1))
    loan = service.return_book(1, date(2024, 4, 5))
    assert loan.returned_on == date(2024, 4, 5)
    assert service.on_loan() == []


def test_return_book_not_on_loan(small_catalog):
    service = LoanService(small_catalog)
    with pytest.raises(ValueError):
        service.return_book(1, date(2024, 4, 5))
