
from expense_tracker.models.transaction import Transaction
from rich.text import Text
from rich.table import Table
from rich.console import Console

console = Console()

def show_transactions(transactions: list[Transaction], table_title: str, type: str) -> None:

    # Listing all transactions on console
    title = ""
    if type == "income":
        title = Text(table_title, style="bold green")
    elif type == "expense":
        title = Text(table_title, style="bold red")
    else:
        title = Text(table_title, style="bold dodger_blue1")
    table = Table(title=title, style="bold gray50")
    table.add_column("ID", style=" gray70")
    table.add_column("TYPE", style=" gray70")
    table.add_column("AMOUNT", style=" gray70")
    table.add_column("CATEGORY", style=" gray70")
    table.add_column("DESCRIPTION", style=" gray70")
    table.add_column("CREATED AT", style=" gray70")

    for transaction in transactions:

        if transaction.type == "expense":
            text = Text.assemble(str(transaction.amount), style="red")
        elif transaction.type == "income":
            text = Text.assemble(str(transaction.amount), style="green")

        table.add_row(
            str(transaction.id), 
            str(transaction.type), 
            text,
            str(transaction.category),
            str(transaction.description),
            str(transaction.created_at),
        )

    console.print(table)