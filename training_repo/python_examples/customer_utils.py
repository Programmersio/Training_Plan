class Customer:
    """A simple customer class for demonstration."""
    def __init__(self, customer_id: int, name: str):
        self.customer_id = customer_id
        self.name = name

    def get_summary(self) -> str:
        return f"Customer {self.customer_id}: {self.name}"


def duplicate_logic_a(x: int) -> int:
    """Duplicate logic function A."""
    if x > 10:
        return x * 2
    return x + 2


def duplicate_logic_b(x: int) -> int:
    """Duplicate logic function B (nearly identical to A)."""
    if x > 10:
        return x * 2
    return x + 2


def long_function():
    """A long function to demonstrate splitting into helpers."""
    result = 0
    for i in range(5):
        result += i * 2
    for j in range(5, 10):
        result += j * 3
    for k in range(10, 15):
        result += k * 4
    return result
