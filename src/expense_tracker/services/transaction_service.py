
from expense_tracker.models.transaction import Transaction
from expense_tracker.repositories.transaction_repository import TransactionRepository


class TransactionService:

    def __init__(self, repo: TransactionRepository) -> None:
        self.repo = repo

    def add_transaction(self, transaction: Transaction) -> None:
        self.repo.save_transaction(transaction)

    def get_transactions(self) -> list[Transaction]:
        return self.repo.load_transactions()

    def get_total_income(self) -> float:
        total_income = 0
        for transaction in self.get_transactions():
            if transaction.type == "income":
                total_income += transaction.amount

        return total_income

    def get_total_expense(self) -> float:
        total_expense = 0
        for transaction in self.get_transactions():
            if transaction.type == "expense":
                total_expense += transaction.amount

        return total_expense

    def current_balance(self) -> float:
        return self.get_total_income() - self.get_total_expense()