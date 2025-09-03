class CustomerName:
    """A simple customer class for demonstration."""
    def __init__(self, customer_id: int, name: str):
        self.customer_id = customer_id
        self.name = name

    def get_summary(self) -> str:
        return f"Customer {self.customer_id}: {self.name}"


def _apply_conditional_logic(x: int) -> int:
    """
    Encapsulated logic for conditional calculations.
    Used by both duplicate_logic_a and duplicate_logic_b to eliminate duplication.
    """
    if x > 10:
        return x * 2
    return x + 2


def duplicate_logic_a(x: int) -> int:
    """Duplicate logic function A - now uses shared helper."""
    return _apply_conditional_logic(x)


def duplicate_logic_b(x: int) -> int:
    """Duplicate logic function B - now uses shared helper."""
    return _apply_conditional_logic(x)


def _calculate_range_sum(start: int, end: int, multiplier: int) -> int:
    """
    Generic helper to calculate sum for a range with a multiplier.
    
    Args:
        start: Start of range (inclusive)
        end: End of range (exclusive)
        multiplier: Value to multiply each number by
        
    Returns:
        int: Sum of range values multiplied by the multiplier
    """
    return sum(i * multiplier for i in range(start, end))


def _calculate_segment_1_sum() -> int:
    """Calculate sum for segment 1 (0-4 with multiplier 2)."""
    return _calculate_range_sum(0, 5, 2)


def _calculate_segment_2_sum() -> int:
    """Calculate sum for segment 2 (5-9 with multiplier 3)."""
    return _calculate_range_sum(5, 10, 3)


def _calculate_segment_3_sum() -> int:
    """Calculate sum for segment 3 (10-14 with multiplier 4)."""
    return _calculate_range_sum(10, 15, 4)


def long_function():
    """
    Calculate total sum across multiple segments with different multipliers.
    
    This function has been refactored to use smaller helper functions for better
    readability and maintainability.
    
    Returns:
        int: Total sum across all segments
    """
    return (_calculate_segment_1_sum() +
            _calculate_segment_2_sum() +
            _calculate_segment_3_sum())
