from .utils import (
    generate_account_id,
    generate_account_number
)


class Account:

    def __init__(self, builder):
        self.account_id = builder.account_id
        self.customer = builder.customer
        self.account_number = builder.account_number
        self.balance = builder.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        try:
            if self.balance >= amount:
                self.balance -= amount
            else:
                raise ValueError
        except ValueError as e:
            print(e)
            return "Insufficient funds"
        except Exception as e:
            print(e)
            return e    

    def get_balance(self):
        return self.balance
    
    def get_account_number(self):
        return self.account_number

    @staticmethod
    def get_builder():
        return AccountBuilder()


class AccountBuilder:
    def __init__(self):
        self.account_id = generate_account_id()
        self.account_number = generate_account_number()
        self.customer = None
        self.balance = None

    def set_customer(self, customer):
        self.customer = customer
        return self

    def set_balance(self, balance):
        self.balance = balance
        return self

    def build(self):
        try:
            if not all([self.account_id, self.customer, self.account_number, self.balance]):
                raise ValueError("Missing required attributes")
            return Account(self)
        except ValueError as e:
            print(e)
            return e
        except Exception as e:
            print(e)
            return e

