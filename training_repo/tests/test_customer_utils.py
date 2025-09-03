import pytest
from python_examples.customer_utils import CustomerName, duplicate_logic_a, duplicate_logic_b, long_function

import pytest
from python_examples.customer_utils import CustomerName, duplicate_logic_a, duplicate_logic_b, long_function

def test_customer_summary():
    c = CustomerName(1, "Alice")
    assert c.get_summary() == "Customer 1: Alice"

def test_duplicate_logic():
    assert duplicate_logic_a(5) == 7
    assert duplicate_logic_b(5) == 7
    assert duplicate_logic_a(20) == 40
    assert duplicate_logic_b(20) == 40

def test_long_function():
    # The result should be deterministic
    assert long_function() == sum([i*2 for i in range(5)]) + sum([j*3 for j in range(5,10)]) + sum([k*4 for k in range(10,15)])
