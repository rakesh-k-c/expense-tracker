
from expense_tracker.models.transaction import Transaction
from expense_tracker.repositories.transaction_repository import TransactionRepository


class TransactionService:

    def __init__(self, repo: TransactionRepository) -> None:
        self.repo = repo

    def add_transaction(self, transaction: Transaction) -> None:
        self.repo.save_transaction(transaction)

    def get_transactions(self) -> list[Transaction]:
        return self.repo.load_transactions()