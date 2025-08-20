#
import statistics

def calculate_median(scores: list[int]) -> float:
    """
    Calculate the median of a list of integers.

    Args:
        scores (list[int]): List of integers.

    Returns:
        float: The median value.

    Raises:
        ValueError: If the input list is empty.

    This function uses the statistics.median function, which internally uses a selection algorithm
    to find the median in O(n) time for unsorted data. If the list is empty, a ValueError is raised.
    """
    if not scores:
        raise ValueError("Input list is empty")
    return float(statistics.median(scores))
"""
Data processing utilities for training exercises.

This module contains stub functions intended for hands‑on practice with GitHub Copilot
and RooCode.  Each function includes a docstring describing the expected behaviour.
You can use Copilot or RooCode to implement the functions based on the docstrings
and then write unit tests to verify their correctness.

Functions:
    calculate_student_statistics(scores):
        Compute average, median and maximum scores from a list of numbers.
    normalise_scores(scores, target=100):
        Scale scores proportionally so that the highest score equals the target.
    group_by_grade(scores):
        Group numeric scores into letter grades (A, B, C, D, F).

Instructions:
    • Read the docstring of each function.
    • Use an AI coding assistant to generate the implementation.
    • Ask the assistant to write unit tests in `tests/test_data_processing.py`.
    • Run the tests and iterate on your prompts until all tests pass.
"""

from typing import Dict, List, Tuple


def calculate_student_statistics(scores: List[float]) -> Tuple[float, float, float]:
    """Calculate summary statistics for a list of student scores.

    Given a list of numeric scores, return a tuple containing the average,
    median and maximum score.  The average should be a floating‑point number
    rounded to two decimal places.  The median should be the middle value when
    the scores are sorted; if there are an even number of scores, return the
    average of the two middle values.  The maximum is simply the highest
    value in the list.  If the list is empty, raise a ``ValueError``.

    Parameters
    ----------
    scores : List[float]
        A list of numeric scores (integers or floats).

    Returns
    -------
    Tuple[float, float, float]
        A tuple of (average, median, maximum).

    Examples
    --------
    >>> calculate_student_statistics([90, 80, 70])
    (80.0, 80.0, 90.0)
    >>> calculate_student_statistics([100.0, 75.5])
    (87.75, 87.75, 100.0)
    """
    # TODO: implement this function using an AI coding assistant
    raise NotImplementedError


def normalise_scores(scores: List[float], target: float = 100.0) -> List[float]:
    """Normalise scores so that the highest score equals a target value.

    Scale each score in the input list proportionally such that the maximum
    score becomes equal to ``target``.  For example, if the highest score is 50
    and ``target`` is 100, all scores should be doubled.  Preserve the
    original ordering of scores.  If the list is empty, return an empty list.
    If the maximum score is zero, return a list of zeros of the same length.

    Parameters
    ----------
    scores : List[float]
        A list of numeric scores.
    target : float, optional
        The desired maximum value after normalisation (default is 100.0).

    Returns
    -------
    List[float]
        A new list containing the normalised scores.

    Examples
    --------
    >>> normalise_scores([25, 50], target=100)
    [50.0, 100.0]
    >>> normalise_scores([], target=100)
    []
    """
    # TODO: implement this function using an AI coding assistant
    raise NotImplementedError


def group_by_grade(scores: List[float]) -> Dict[str, List[float]]:
    """Group scores into letter grades.

    Categorise each numeric score into letter grades using the following
    scale:

    * **A**: 90 – 100
    * **B**: 80 – 89
    * **C**: 70 – 79
    * **D**: 60 – 69
    * **F**: below 60

    Return a dictionary where keys are letter grades and values are lists of
    scores belonging to those grades.  Exclude grades that have no scores.
    The order of grades in the resulting dictionary is not important.

    Parameters
    ----------
    scores : List[float]
        A list of numeric scores.

    Returns
    -------
    Dict[str, List[float]]
        A dictionary mapping letter grades to lists of scores.

    Examples
    --------
    >>> group_by_grade([95, 82, 67, 50])
    {'A': [95], 'B': [82], 'D': [67], 'F': [50]}
    """
    # TODO: implement this function using an AI coding assistant
    raise NotImplementedError