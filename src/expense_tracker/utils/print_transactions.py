
from expense_tracker.models.transaction import Transaction
from expense_tracker.models.enums import TransactionType, IncomeCategoryType, ExpenseCategoryType
from rich.text import Text
from rich.table import Table
from rich.console import Console

console = Console()

def printHeader(table):
    table.add_column("ID", style=" gray70")
    table.add_column("TYPE", style=" gray70")
    table.add_column("AMOUNT", style=" gray70")
    table.add_column("CATEGORY", style=" gray70")
    table.add_column("DESCRIPTION", style=" gray70")
    table.add_column("CREATED AT", style=" gray70")

def show_transactions(transactions: list[Transaction], title: str) -> None:

    # Listing all transactions on console
    table_title = Text(title, style="bold blue")
    table = Table(title=table_title, style="bold blue")

    printHeader(table=table)

    for transaction in transactions:

        if transaction.type == TransactionType.EXPENSE:
            text = Text(str(transaction.amount), style="red")
        elif transaction.type == TransactionType.INCOME:
            text = Text(str(transaction.amount), style="green")

        table.add_row(
            str(transaction.id), 
            str(transaction.type.value), 
            text,
            str(transaction.category.value),
            str(transaction.description),
            str(transaction.created_at),
        )

    console.print(table)

def show_incomes(transactions: list[Transaction]) -> None:
    # Listing all transactions on console
    table = Table(title=Text("INCOME TRANSACTIONS", style="bold green"), style="bold green")

    printHeader(table=table)

    for transaction in transactions:

        if transaction.type == TransactionType.INCOME:
            table.add_row(
                str(transaction.id), 
                str(transaction.type.value), 
                Text(str(transaction.amount), style="green"),
                str(transaction.category.value),
                str(transaction.description),
                str(transaction.created_at),
            )

    console.print(table)

def show_expenses(transactions: list[Transaction]) -> None:
    # Listing all transactions on console
    table = Table(title=Text("EXPENSE TRANSACTIONS", style="bold red"), style="bold red")

    printHeader(table=table)

    for transaction in transactions:

        if transaction.type == TransactionType.EXPENSE:
            table.add_row(
                str(transaction.id), 
                str(transaction.type.value), 
                Text(str(transaction.amount), style="red"),
                str(transaction.category.value),
                str(transaction.description),
                str(transaction.created_at),
            )

    console.print(table)
