
from datetime import datetime
from dataclasses import asdict

from rich.console import Console
from rich.table import Table
from rich.text import Text

from expense_tracker.config import TRANSACTIONS_FILE
from expense_tracker.models.transaction import Transaction
from expense_tracker.models.enums import TransactionType, IncomeCategoryType, ExpenseCategoryType
from expense_tracker.repositories.transaction_repository import TransactionRepository
from expense_tracker.services.transaction_service import TransactionService

from expense_tracker.utils.validations import validate_choice
from expense_tracker.utils.get_next_id import get_next_id
from expense_tracker.utils.print_transactions import show_transactions, show_incomes, show_expenses

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


        console.print("\n[dodger_blue1][1]. Add transaction[/dodger_blue1]")
        console.print("[dodger_blue1][2]. Show all transactions[/dodger_blue1]")
        console.print("[dodger_blue1][3]. Show incomes [/dodger_blue1]")
        console.print("[dodger_blue1][4]. Show expenses [/dodger_blue1]")
        console.print("[dodger_blue1][5]. Update Transaction [/dodger_blue1]")
        console.print("[dodger_blue1][6]. Delete Transaction [/dodger_blue1]")
        console.print("[dodger_blue1][7]. Search Transaction by ID[/dodger_blue1]")
        console.print("[dodger_blue1][8]. MONTHLY SUMMERY REPORT[/dodger_blue1]")
        console.print("[dodger_blue1][q]. Press 'q' to quit[/dodger_blue1]")

        # min=1 and max=3 and also take 'q' for quit
        choice = validate_choice(min=1, max=8)

        match choice:
            case 1:
                # ID
                id = get_next_id(transactions)

                # Transaction Type
                print("[1]. Income")
                print("[2]. Expense")
                transaction_type_choice = validate_choice(min=1, max=2)
                match transaction_type_choice:
                    case 1:
                        transaction_type = TransactionType.INCOME
                    case 2:
                        transaction_type = TransactionType.EXPENSE

                amount = float(input("Enter Amount "))

                # Category
                if transaction_type == TransactionType.INCOME:
                    print("[1] Salary")
                    print("[2] Rent")
                    print("[3] Investment return")
                    print("[4] Other")
                    category_type_choice = validate_choice(min=1, max=4)
                    match category_type_choice:
                        case 1:
                            category = IncomeCategoryType.SALARY
                        case 2:
                            category = IncomeCategoryType.RENT
                        case 3:
                            category = IncomeCategoryType.INVESTMENT_RETURN
                        case 4:
                            category = IncomeCategoryType.OTHER
                else:
                    print("[1] Food")
                    print("[2] Fashion")
                    print("[3] Household Accessories")
                    print("[4] Other")
                    category_type_choice = validate_choice(min=1, max=4)
                    match category_type_choice:
                        case 1:
                            category = ExpenseCategoryType.FOOD
                        case 2:
                            category = ExpenseCategoryType.FASHION
                        case 3:
                            category = ExpenseCategoryType.HOUSEHOLD_ACCESSORIES
                        case 4:
                            category = ExpenseCategoryType.OTHER

                # Description
                description = input("Enter description (rent for august etc.) ")

                # created at
                created_at = datetime.now()

                transaction = Transaction(id, transaction_type, amount, category, description, created_at)
                service.add_transaction(transaction)

            case 2:
                show_transactions(transactions, title="ALL TRANSACTIONS")
                
            case 3:
                show_incomes(transactions)
                
            case 4:
                show_expenses(transactions)

            case 5:
                trans_id = int(input("Enter transaction id: "))
                console.print("You can update only {amount, category, description}\n")
                amount = float(input("Enter Amount "))
                category = input("Enter category (Food, Shopping, Home expense, rent) ")
                description = input("Enter description (rent for august etc.) ")
                updated_transaction_details = {
                    "amount" : amount,
                    "category" : category,
                    "description" : description
                }
                service.update_transaction(trans_id, **updated_transaction_details);

            case 6:
                trans_id = int(input("Enter transaction id: "))
                service.delete_transaction(trans_id)

            case 7:
                trans_id = int(input("Enter transaction id: "))
                transaction = service.search_transaction_by_ID(trans_id)

                show_transactions([transaction], title=f"ID : {trans_id}")

            case 'q':
                console.print("\n\tSee you soon!", style="bold dodger_blue1")
                print()
                break











if __name__ == "__main__":
    main()








































































