from repositories.account_repository import AccountRepository
from use_cases.user_use_case import UserUseCase
from threading import Thread, Lock
import time


class TransactionUseCase:
    def make_transaction(self, account_id, amount, transaction_type):
        """Make a transaction"""
        try:
            account = AccountRepository.find_account_by_id(account_id)
            if transaction_type == 'deposit':
                account.deposit(amount)
            elif transaction_type == 'withdraw':
                account.withdraw(amount)
            else:
                raise ValueError
        except ValueError as e:
            print(e)
            return "Invalid transaction type"
        except Exception as e:
            print(e)
            return e  


if __name__ == '__main__':
    customer = UserUseCase.create_customer("Test User", "testuser@test.com", "1234567890")
    account = UserUseCase.create_account(customer, 1000)
    print(account.account_id,'id')
    threads = []

    for i in range(10):
        threads.append(Thread(target=TransactionUseCase.make_transaction, args=(account.account_id,100,'deposit')))

    for thread in threads:
        thread.start()
        
    # Joins threads back to the parent process
    for thread in threads:
        thread.join()

