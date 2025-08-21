import pytest
from python_examples.invoice_utils import InvoiceAdd, processLineItem1, processLineItem2

def test_invoice_add_to_ledger():
    ledger = []
    inv = InvoiceAdd(101, 250.0)
    inv.add_to_ledger(ledger)
    assert ledger == [{'invoice_id': 101, 'amount': 250.0}]

def test_processLineItem1_and_2():
    item = {'price': 100, 'quantity': 2}
    assert processLineItem1(item) == 220.0
    assert processLineItem2(item) == 220.0
    # Test with missing quantity (should default to 1)
    item2 = {'price': 50}
    assert processLineItem1(item2) == 55.0
    assert processLineItem2(item2) == 55.0
