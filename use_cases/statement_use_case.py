from repositories.account_repository import AccountRepository


class StatementUseCase:
    def generate_account_statement(self, account_id):
        """Generate account statement"""
        try:
            account = AccountRepository.find_account_by_id(account_id)
            if account:
                statement = f"Account Statement for Account ID: {account.account_id}\n"
                # Append transaction details to statement
                return statement
            else:
                message = 'Account not found!'
                return message
        except Exception as e:
            print(e)
            return e
