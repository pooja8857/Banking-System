import pytest
from use_cases.user_use_case import UserUseCase
from tests.conftest import customer_and_account


def test_create_account():
    user_use_case = UserUseCase()

    # Customer creation test.
    customer = user_use_case.create_customer("Test User", "testuser@test.com", "1234567890")
    assert customer is not None
    assert customer.name == "Test User"
    assert customer.email == "testuser@test.com"
    assert customer.phone_number == "1234567890"

    # Account creation test.
    account = user_use_case.create_account(customer, 1000)
    assert account is not None
    assert account.customer.customer_id == customer.customer_id
    assert account.balance == 1000

def test_get_account_balance(customer_and_account):
    _, account = customer_and_account
    initial_balance = account.get_balance()
    assert initial_balance == 1000

def test_valid_withdraw(customer_and_account):
    _, account = customer_and_account
    account.withdraw(500)
    assert account.get_balance() == 500


def test_invalid_withdraw(customer_and_account):
    _, account = customer_and_account
    result = account.withdraw(1200)
    assert result == "Insufficient funds"


def test_deposit(customer_and_account):
    _, account = customer_and_account
    account.deposit(100)
    assert account.get_balance() == 1100

 


