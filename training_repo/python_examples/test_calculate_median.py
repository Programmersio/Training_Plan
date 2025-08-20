import pytest
from data_processing import calculate_median

def test_odd_length():
    scores = [3, 1, 2]
    assert calculate_median(scores) == 2.0, "Median of [3,1,2] should be 2.0"

def test_even_length():
    scores = [4, 1, 2, 3]
    assert calculate_median(scores) == 2.5, "Median of [4,1,2,3] should be 2.5"

def test_duplicates():
    scores = [2, 2, 2, 2]
    assert calculate_median(scores) == 2.0, "Median of [2,2,2,2] should be 2.0"

def test_negative_numbers():
    scores = [-5, -1, -3]
    assert calculate_median(scores) == -3.0, "Median of [-5,-1,-3] should be -3.0"

def test_large_list():
    scores = list(range(1000001))
    assert calculate_median(scores) == 500000.0, "Median of 0..1000000 should be 500000.0"

def test_empty_list():
    with pytest.raises(ValueError, match="Input list is empty"):
        calculate_median([])