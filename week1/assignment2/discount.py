from datetime import datetime;

DISCOUNT_RATE = .1;
TAX_RATE = .06;
DISCOUNT_DAYS = ["Wednesday", "Thursday"];

today = datetime.now().strftime("%A");

if today in DISCOUNT_DAYS:
    print(f"Today is {today}, you get a discount!");
else:
    print(f"Today is {today}, no discount available."); 
class InvoiceItem:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.quantity * self.price

    def __str__(self):
        return f"Line Item x {self.quantity} @ ${self.price:.2f} = ${self.total():.2f}"

class Invoice:
    def __init__(self, items):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def take_order(self):
        quantity = 1
        while quantity != 0:
            quantity = int(input("Enter quantity: "))
            if quantity == 0:
                break
            if quantity < 0:
                print("Quantity cannot be negative. Please enter a valid quantity.")
                break
            price = float(input("Enter price: $"))
            item = InvoiceItem(quantity, price)
            self.add_item(item)
            print(f"Added item to the invoice.\n Next item? (Enter 0 to finish)")

    def subtotal(self):
        return sum(item.total() for item in self.items)
    
    def discount(self):
        if today in DISCOUNT_DAYS:
            if self.subtotal() < 50:
                return 0
            else:
                return self.subtotal() * DISCOUNT_RATE
        else:
            return 0
        
    def print_invoice(self):
        ## Clear Screen and print header
        print("\n" + "="*40);
        print("INVOICE");
        print("="*40);
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}");
        print(f"Today: {today}");
        print("\nItems:");
        for item in self.items:
            print(item);
        print("\nSummary:");
        print(f"Items count: {len(self.items)}");
        print (f"Subtotal: ${self.subtotal():.2f}");
        print (f"Discount: ${self.discount():.2f}");
        print (f"Pre-tax total: ${self.subtotal() - self.discount():.2f}");
        print (f"Tax: ${self.tax():.2f}");
        print (f"Total: ${self.total():.2f}");
    
    def tax(self):
        return (self.subtotal() - self.discount()) * TAX_RATE
    
    def total(self):
        return self.subtotal() - self.discount() + self.tax()

    def __str__(self):
        return "\n".join(str(item) for item in self.items) + f"\nTotal: ${self.total():.2f}"

invoice = Invoice([]);

invoice.take_order();
invoice.print_invoice();

