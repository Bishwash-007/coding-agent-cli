from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich import box

console = Console()

def show_welcome():
    welcome_text = Text()
    welcome_text.append("Welcome \n", style="bold white")
    welcome_text.append("Braniac AI here on your service \n", style="bold white")
    welcome_text.append("\nAsk me anything \n", style="dim white")
    welcome_text.append("Type 'exit' or 'quit' to leave the session.", style="italic dim")
    
    console.print(
        Panel(
            welcome_text,
            title="[bold white]Braniac AI[/bold white]",
            border_style="white",
            expand=True,
            padding=(1, 2),
            box=box.ROUNDED
        )
    )

def display_response(content: str, style="white"):
    """Pretty print a response from the agent."""
    console.print(
        Panel(
            Text(content, style=style),
            border_style=style,
            box=box.SIMPLE,
            padding=(1, 2)
        )
    )

def prompt_input() -> str:
    """Prompt user input with a styled prompt."""
    return Prompt.ask(f"\n[bold white]You[/bold white]")
