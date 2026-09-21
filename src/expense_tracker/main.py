
from datetime import datetime
from dataclasses import asdict

from rich.console import Console
from rich.table import Table
from rich.text import Text

from expense_tracker.config import TRANSACTIONS_FILE
from expense_tracker.models.transaction import Transaction
from expense_tracker.repositories.transaction_repository import TransactionRepository
from expense_tracker.services.transaction_service import TransactionService

from expense_tracker.utils.validations import validate_choice
from expense_tracker.utils.get_next_id import get_next_id
from expense_tracker.utils.print_transactions import show_transactions

console = Console()

def main():
    console.print("\n\t\tExpense Tracker", style="bold blue")
    console.print("-------------------------------------------------", style="bold blue")


    repo = TransactionRepository(TRANSACTIONS_FILE)
    service = TransactionService(repo)


    while True:

        transactions = service.get_transactions()


        curr_balance = Text(str(service.current_balance()), style="bold green")
        total_income = Text(str(service.get_total_income()), style="green")
        total_expense = Text.assemble(str(service.get_total_expense()), style="red")

        console.print("-------------------------------------------------", style="dodger_blue1")
        console.print(f"\t\tBALANCE : {curr_balance}", style="bold gray70")
        console.print(f"\nINCOME : {total_income}", style="green", end="")
        console.print(f"\t\tEXPENSE : {total_expense}", style="red")
        console.print("-------------------------------------------------", style="dodger_blue1")


        """
            [1] Add transaction
            [2] Show all transactions
            [3] Show incomes
            [4] Show expenses
            [5] Update transaction
            [6] Delete transaction
            [7] Search/filter transactions
            [8] Monthly summary
            [9] Quit
        """



        console.print("\n[dodger_blue1][1]. Add transaction[/dodger_blue1]")
        console.print("[dodger_blue1][2]. Show all transactions[/dodger_blue1]")
        console.print("[dodger_blue1][3]. Show incomes [/dodger_blue1]")
        console.print("[dodger_blue1][4]. Show expenses [/dodger_blue1]")
        console.print("[dodger_blue1][q]. Press 'q' to quit[/dodger_blue1]")

        # min=1 and max=3 and also take 'q' for quit
        choice = validate_choice(min=1, max=4)

        match choice:
            case 1:
                # Adding Transactions
                id = get_next_id(transactions)
                type = input("Enter Type ")
                amount = float(input("Enter Amount "))
                category = input("Enter category (Food, Shopping, Home expense, rent) ")
                description = input("Enter description (rent for august etc.) ")
                created_at = datetime.now()

                transaction = Transaction(id, type, amount, category, description, created_at)
                service.add_transaction(transaction)

            case 2:
                show_transactions(transactions, "List of all Transactions", type="all")
                
            case 3:
                income_transactions = service.get_income_transactions()
                show_transactions(income_transactions, "Income Transactions", type="income")

            case 4:
                expense_transactions = service.get_expense_transactions()
                show_transactions(expense_transactions, "Expense Transactions", type="expense")

            case 'q':
                console.print("\n\tSee you soon!", style="bold dodger_blue1")
                print()
                break











if __name__ == "__main__":
    main()








































































