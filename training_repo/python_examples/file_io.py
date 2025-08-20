"""
File input/output and parsing utilities for training exercises.

This module contains placeholder functions to practise reading data from files
and transforming it into Python data structures.  The docstrings describe
the expected behaviour in detail.  Use an AI coding assistant to complete
these functions and write tests in ``tests/test_file_io.py``.

Functions:
    parse_csv_content(content):
        Convert a CSV string into a list of dictionaries keyed by header.
    load_csv_file(path):
        Read a CSV file from disk and parse its contents.
    summarise_log_file(path):
        Read a log file and return summary statistics about its contents.
"""

from typing import Dict, List, Any


def parse_csv_content(content: str) -> List[Dict[str, Any]]:
    """Parse comma‑separated values into a list of dictionaries.

    Given a string ``content`` representing CSV data with a header row,
    return a list of dictionaries.  Each dictionary maps column names to
    values.  Leading/trailing whitespace should be stripped from headers
    and values.  Empty lines should be ignored.  If a line has fewer
    fields than the header row, fill missing values with ``None``.  If
    there are extra fields, include them using generated header names like
    ``extra_1``, ``extra_2``, etc.  Values should be returned as strings.

    Parameters
    ----------
    content : str
        The raw contents of a CSV file, including newlines.

    Returns
    -------
    List[Dict[str, Any]]
        A list of row dictionaries.

    Examples
    --------
    >>> parse_csv_content("name,age\nAlice,30\nBob,25")
    [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
    >>> parse_csv_content("id,value\n1,foo\n2")
    [{'id': '1', 'value': 'foo'}, {'id': '2', 'value': None}]
    """
    # TODO: implement this function using an AI coding assistant
    raise NotImplementedError


def load_csv_file(path: str) -> List[Dict[str, Any]]:
    """Read a CSV file from ``path`` and return its parsed contents.

    Open the file located at ``path`` using UTF‑8 encoding, read its contents
    and pass them to ``parse_csv_content``.  If the file does not exist,
    raise ``FileNotFoundError``.  If an error occurs while reading the file,
    let the exception propagate.  This function does not modify the data; it
    simply delegates to ``parse_csv_content``.

    Parameters
    ----------
    path : str
        The filesystem path to the CSV file.

    Returns
    -------
    List[Dict[str, Any]]
        A list of dictionaries parsed from the file’s content.
    """
    # TODO: implement this function using an AI coding assistant
    raise NotImplementedError


def summarise_log_file(path: str) -> Dict[str, Any]:
    """Read a log file and summarise its contents.

    Given a plain‑text log file at ``path``, return a summary dictionary
    with the following keys:

    * ``line_count``: the total number of non‑empty lines.
    * ``error_count``: the number of lines containing the word ``ERROR`` (case-insensitive).
    * ``warnings``: a list of unique warning messages extracted from lines containing
      ``WARNING:``.  Strip the prefix ``WARNING:`` and any leading/trailing whitespace.

    The log file may contain informational messages, warnings and errors.  You do
    not need to parse timestamps or other data unless necessary for the summary.

    Parameters
    ----------
    path : str
        The filesystem path to the log file.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing summary statistics.

    Examples
    --------
    >>> summarise_log_file("/path/to/log.txt")
    {'line_count': 42, 'error_count': 3, 'warnings': ['Disk space low', 'Retrying request']}
    """
    # TODO: implement this function using an AI coding assistant
    raise NotImplementedError