class ScreenManager:
    def __init__(self):
        self.screens = {}

    def print_header(self, header=None):
        print("\n" + "=" * 40)
        print(header == None ? "Tire Volume Calculator" : f"Tire Volume Calculator - {header}")
        print("=" * 40)

    def selection_footer(self, message):
        print("\n" + "=" * 40)
        result = input(f"{message}: ")
        print("=" * 40)
        return result
    
    def main_menu(self):
        self.print_header()
        print("1. Calculate Tire Volume")
        print("2. Exit")
        return self.selection_footer("Select an option")