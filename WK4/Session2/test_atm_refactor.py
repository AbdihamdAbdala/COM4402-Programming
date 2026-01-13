# test_atm_refactor.py

import pytest
import atm_refactor as atm


# -------- deposit tests --------

@pytest.mark.parametrize("balance, amount, expected", [
    (0.0, 50.0, 50.0),
    (100.0, 25.0, 125.0),
])
def test_deposit_valid(balance, amount, expected):
    result = atm.deposit(balance, amount)
    assert result == pytest.approx(expected), (
        f"deposit({balance}, {amount}) should give {expected}, but got {result}"
    )


@pytest.mark.parametrize("balance, bad_amount", [
    (0.0, 0.0),
    (50.0, -10.0),
])
def test_deposit_non_positive_amount_raises_value_error(balance, bad_amount):
    with pytest.raises(ValueError):
        atm.deposit(balance, bad_amount)


# -------- withdraw tests --------

@pytest.mark.parametrize("balance, amount, expected", [
    (100.0, 40.0, 60.0),
    (50.0, 50.0, 0.0),
])
def test_withdraw_valid(balance, amount, expected):
    result = atm.withdraw(balance, amount)
    assert result == pytest.approx(expected), (
        f"withdraw({balance}, {amount}) should give {expected}, but got {result}"
    )


@pytest.mark.parametrize("balance, bad_amount", [
    (50.0, 0.0),
    (50.0, -5.0),
])
def test_withdraw_non_positive_amount_raises_value_error(balance, bad_amount):
    with pytest.raises(ValueError):
        atm.withdraw(balance, bad_amount)


def test_withdraw_insufficient_funds_raises_value_error():
    balance = 50.0
    amount = 60.0
    with pytest.raises(ValueError):
        atm.withdraw(balance, amount)


# -------- show_balance tests (if implemented) --------

def test_show_balance_format():
    if hasattr(atm, "show_balance"):
        result = atm.show_balance(100.0)
        assert isinstance(result, str), (
            "show_balance should return a string"
        )
        assert "100.00" in result, (
            "show_balance(100.0) should include '100.00' in the returned string"
        )