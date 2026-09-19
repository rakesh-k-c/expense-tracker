
from rich.console import Console

console = Console()


def validate_choice(min: int, max: int) -> int | str:
    while True:
        val = input("Choose the above option: ")
        if val == 'q':
            return val
        elif int(val) >= min and int(val) <= max:
            return int(val)
        else:
            console.print("Invalid options, try again...", style="bold red")
            continue