


from pathlib import Path
import json
from dataclasses import asdict
from datetime import datetime

from expense_tracker.models.transaction import Transaction
from expense_tracker.models.enums import TransactionType, IncomeCategoryType, ExpenseCategoryType



class TransactionRepository:

    def __init__(self, data_file: Path) -> None:
        self.data_file = data_file


    def load_transactions(self) -> list[Transaction]:

        if not self.data_file.exists():
            return []

        with open(self.data_file, 'r', encoding='utf-8') as file:
            transactions_data = json.load(file)

        transactions = []

        for data in transactions_data:

            transaction_type = TransactionType(data["type"])

            if transaction_type == TransactionType.INCOME:
                category = IncomeCategoryType(data["category"])
            else:
                category = ExpenseCategoryType(data["category"])

            transactions.append(
                Transaction(
                    id=data["id"],
                    type=transaction_type,
                    amount=data["amount"],
                    category=category,
                    description=data["description"],
                    created_at=datetime.fromisoformat(data["created_at"])
                )
            )

        return transactions

    def save_transaction(self, transaction: Transaction) -> None:

        transactions = self.load_transactions()
        transactions.append(transaction)

        transactions_data = []

        for data in transactions:
            transaction_data = asdict(data)

            transaction_data["type"] = data.type.value
            transaction_data["category"] = data.category.value
            transaction_data["created_at"] = transaction_data['created_at'].isoformat()
            transactions_data.append(transaction_data)

        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump(transactions_data, file, indent=4, ensure_ascii=False)

    def save_updated_transaction(self, updated_transactions: list[Transaction]):
        transactions = []

        for data in updated_transactions:
            transaction_data = asdict(data)

            transaction_data["type"] = data.type.value
            transaction_data["category"] = data.category.value
            transaction_data["created_at"] = transaction_data['created_at'].isoformat()
            transactions.append(transaction_data)

        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump(transactions, file, indent=4, ensure_ascii=False)

    def save_del_updated_transaction(self, deleted_transactions: list[Transaction]):
        transactions = []
        
        for data in deleted_transactions:
            transaction_data = asdict(data)

            transaction_data["type"] = data.type.value
            transaction_data["category"] = data.category.value
            transaction_data["created_at"] = transaction_data['created_at'].isoformat()
            transactions.append(transaction_data)

        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump(transactions, file, indent=4, ensure_ascii=False)


        






























































