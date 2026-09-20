
from datetime import datetime
from dataclasses import asdict

from rich.console import Console

from expense_tracker.config import TRANSACTIONS_FILE
from expense_tracker.models.transaction import Transaction
from expense_tracker.repositories.transaction_repository import TransactionRepository
from expense_tracker.services.transaction_service import TransactionService
from expense_tracker.utils.validations import validate_choice
from expense_tracker.utils.get_next_id import get_next_id

console = Console()

def main():
    console.print("\n\tExpense Tracker", style="bold blue")
    console.print("--------------------------------", style="bold blue")


    repo = TransactionRepository(TRANSACTIONS_FILE)
    service = TransactionService(repo)


    while True:
        console.print("\n[dodger_blue1][1]. Add transaction[/dodger_blue1]")
        console.print("[dodger_blue1][2]. Show all transactions[/dodger_blue1]")
        console.print("[dodger_blue1][3]. Press 'q' to quit[/dodger_blue1]")

        # min=1 and max=3 and also take 'q' for quit
        choice = validate_choice(min=1, max=3)

        match choice:
            case 1:
                transactions = service.get_transactions()

                id = get_next_id(transactions)
                name = input("Enter Name ")
                amount = float(input("Enter Amount "))
                category = input("Enter category (Food, Shopping, Home expense, rent) ")
                description = input("Enter description (rent for august etc.) ")
                created_at = datetime.now()

                transaction = Transaction(id, name, amount, category, description, created_at)
                service.add_transaction(transaction)

            case 2:
                print("2....")
            case 'q':
                console.print("\n\tSee you soon!", style="bold dodger_blue1")
                print()
                break











if __name__ == "__main__":
    main()








































































