import pytest
from bankpack.bank import Account, InsufficientAmount


def test_setting_name():
    my_account = Account(name="Blessy")
    assert my_account.name == "Blessy"


def test_default_balance():
    my_account = Account(name="Blessy")
    assert my_account.balance == 0


def test_setting_balance():
    my_account = Account(name="Blessy", balance=250)
    assert my_account.balance == 250


def test_account_deposit():
    my_account = Account(name="Blessy", balance=250)
    my_account.deposit(120)
    assert my_account.balance == 370


def test_account_withdraw():
    my_account = Account(name="Blessy", balance=250)
    my_account.withdraw(10)
    assert my_account.balance == 240


def test_account_withdraw_raises_insufficient_amount_exception():
    my_account = Account(name="Blessy")
    with pytest.raises(InsufficientAmount):
        my_account.withdraw(100)
