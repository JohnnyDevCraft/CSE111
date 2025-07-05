from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, FloatPrompt
from rich.style import Style
from rich.table import Table
from Tire import Tire
from Exporter import Exporter

from pythonclimenu import menu

class App:
    def __init__(self, name: str):
        self.name = name
        self.console = Console()
        self.exporter = Exporter("volumes.txt")

    def console(self):
        return self.console

    def print_header(self, subtitle = ""):
        style = Style(color="blue", bold=True)
        self.console.print(Panel(f"Tire Volume Calculator: {subtitle}", border_style="blue", padding=(1, 2), expand=True, style=style))

    def print_footer(self, message: str):
        self.console.print(Panel.fit(message, title="Thank you for using the Tire Volume Calculator", subtitle="Designed By: Johnathon Smith", border_style="blue", padding=(1, 2)))

    def enter_tire_details(self):
        self.print_header("Enter Tire Details")
        tire = Tire()
        tire.set_diameter(FloatPrompt.ask(Tire.DIAMETER_REQ, default=15.0))
        tire.set_width(FloatPrompt.ask(Tire.WIDTH_REQ, default=205.0))
        tire.set_aspect_ratio(FloatPrompt.ask(Tire.ASPECT_RATIO_REQ, default=60.0))
        self.exporter.export_csv_line(tire)
        Prompt.ask(f"Data Saved!\n{tire.get_volume_str()}\nPress Enter to continue...")

    def view_history(self):
        self.print_header(f"View History")
        tires = self.exporter.read_csv_lines()

        if not tires:
            self.console.print("No history found.")
            Prompt.ask("Press Enter to continue...")
            return

        table = Table(title="History of Volumes Calculated", show_header=True, header_style="bold green")
        table.add_column("Date", style="magenta")
        table.add_column("Diameter (inches)", style="cyan")
        table.add_column("Width (mm)", style="cyan")
        table.add_column("Aspect Ratio", style="cyan")
        table.add_column("Volume (liters)", style="cyan")

        for tire in tires:
            table.add_row(str(tire.get_date()).format("%Y-%m-%d"),str(tire.diameter), str(tire.width), str(tire.aspect_ratio), str(tire.calculate_volume()))

        self.console.print(table)

        Prompt.ask("Press Enter to continue...")


    def main_menu(self):
        self.print_header()

        OPTIONS = ["Calculate tire volume", "View History", "Exit"]

        while True:
            choice = menu(
                title="Tire Volume Calculator",
                options=OPTIONS,
                cursor_color="blue"
            )

            if choice == "Calculate tire volume":
                self.enter_tire_details()
            elif choice == "View History":
                self.view_history()
            elif choice == "Exit":
                self.print_footer("Thank you for using the Tire Volume Calculator!")
                break
            else:
                self.console.print("Invalid option, please try again.")

    def Run(self):
        self.main_menu()
        self.console.print("Application closed successfully.")

