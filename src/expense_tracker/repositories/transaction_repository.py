


from pathlib import Path
import json
from dataclasses import asdict
from datetime import datetime

from expense_tracker.models.transaction import Transaction



class TransactionRepository:

    def __init__(self, data_file: Path) -> None:
        self.data_file = data_file


    def load(self) -> list[Transaction]:

        if not self.data_file.exists():
            return []

        with open(self.data_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        transactions = []

        for transaction in data:
            transaction["created_at"] = datetime.fromisoformat(transaction["created_at"])       

            transactions.append(Transaction(**transaction))

        return transactions

    def save(self, transaction: Transaction) -> None:

        transactions = self.load()
        transactions.append(transaction)

        transactions_data = []

        for data in transactions:
            transaction_data = asdict(data)

            transaction_data["created_at"] = transaction_data['created_at'].isoformat()
            transactions_data.append(transaction_data)

        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump(transactions_data, file, indent=4, ensure_ascii=False)


        






























































