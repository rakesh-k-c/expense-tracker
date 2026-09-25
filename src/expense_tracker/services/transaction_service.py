
from expense_tracker.models.transaction import Transaction
from expense_tracker.repositories.transaction_repository import TransactionRepository


class TransactionService:

    def __init__(self, repo: TransactionRepository) -> None:
        self.repo = repo

    def add_transaction(self, transaction: Transaction) -> None:
        self.repo.save_transaction(transaction)

    def get_transactions(self) -> list[Transaction]:
        return self.repo.load_transactions()

    def get_income_transactions(self) -> list[Transaction]:
        all_transactions = self.repo.load_transactions()
        income_transactions = []
        for transaction in all_transactions:
            if transaction.type == "income":
                income_transactions.append(transaction)
        return income_transactions

    def get_expense_transactions(self) -> list[Transaction]:
        all_transactions = self.repo.load_transactions()
        expense_transactions = []
        for transaction in all_transactions:
            if transaction.type == "expense":
                expense_transactions.append(transaction)
        return expense_transactions

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


    def update_transaction(self, id, **kwargs) -> None:
        transactions = self.repo.load_transactions()
        type = kwargs["type"]
        amount = kwargs["amount"]
        category = kwargs["category"]
        description = kwargs["description"]

        for transaction in transactions:
            if transaction.id == id:
                transaction.type = type
                transaction.amount = float(amount)
                transaction.category = category
                transaction.description = description

                self.repo.save_updated_transaction(transactions)
                return
            

        raise ValueError(f"Transactions with id : {id} is not found.")

    def delete_transaction(self, id) -> None:
        transactions = self.repo.load_transactions()

        for transaction in transactions:
            if transaction.id == id:
                transactions.remove(transaction)
                self.repo.save_del_updated_transaction(transactions)
                return
        raise ValueError(f"Transactions with id : {id} is not found.")

    def search_transaction_by_ID(self, id) -> Transaction:
        for transaction in self.get_transactions():
            if transaction.id == id:
                return transaction

        raise ValueError(f"Invalid input, id {id} is not found")

        
                