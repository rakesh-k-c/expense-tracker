
from datetime import datetime
from dataclasses import asdict

from rich.console import Console

from expense_tracker.config import TRANSACTIONS_FILE
from expense_tracker.models.transaction import Transaction
from expense_tracker.repositories.transaction_repository import TransactionRepository
from expense_tracker.services.transaction_service import TransactionService
from expense_tracker.utils.validations import validate_choice

console = Console()

def main():
    console.print("\n\tExpense Tracker", style="bold blue")
    console.print("--------------------------------", style="bold blue")

    transaction = Transaction(
        id=1,
        type="expense",
        amount=4440.0,
        category="foot",
        description="lunch",
        created_at=datetime.now(),
    )

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
                print("1...")
            case 2:
                print("2....")
            case 'q':
                console.print("\n\tSee you soon!", style="bold dodger_blue1")
                print()
                break











if __name__ == "__main__":
    main()








































































