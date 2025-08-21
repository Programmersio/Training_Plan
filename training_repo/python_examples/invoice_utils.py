class InvoiceAdd:
    """A dummy class representing an invoice addition operation."""
    def __init__(self, invoice_id: int, amount: float):
        self.invoice_id = invoice_id
        self.amount = amount

    def add_to_ledger(self, ledger: list) -> None:
        ledger.append({'invoice_id': self.invoice_id, 'amount': self.amount})

def processLineItem1(item: dict) -> float:
    """Process a line item and return the total after tax (v1)."""
    subtotal = item.get('price', 0) * item.get('quantity', 1)
    tax = subtotal * 0.1
    total = subtotal + tax
    return round(total, 2)

def processLineItem2(item: dict) -> float:
    """Process a line item and return the total after tax (v2, nearly identical)."""
    subtotal = item.get('price', 0) * item.get('quantity', 1)
    tax = subtotal * 0.1
    total = subtotal + tax
    return round(total, 2)
