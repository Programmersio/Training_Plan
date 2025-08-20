"""
Unit tests for ``file_io`` module.

These tests cover the basic functionality described in the docstrings of
``python_examples/file_io.py``.  They can be extended to include more
edge cases and error conditions as you practise prompt engineering and unit
test generation.
"""

import os
import tempfile
import pytest
from python_examples.file_io import parse_csv_content, load_csv_file, summarise_log_file


def test_parse_csv_content_simple() -> None:
    content = "name,age\nAlice,30\nBob,25"
    rows = parse_csv_content(content)
    assert rows == [
        {'name': 'Alice', 'age': '30'},
        {'name': 'Bob', 'age': '25'},
    ]


def test_parse_csv_content_missing_fields() -> None:
    content = "id,value\n1,foo\n2"
    rows = parse_csv_content(content)
    assert rows == [
        {'id': '1', 'value': 'foo'},
        {'id': '2', 'value': None},
    ]


def test_load_csv_file(tmp_path: tempfile.TemporaryDirectory) -> None:
    # Create a temporary CSV file
    csv_content = "a,b\n1,2\n3,4"
    file_path = tmp_path / "data.csv"
    file_path.write_text(csv_content)
    result = load_csv_file(str(file_path))
    assert result == [
        {'a': '1', 'b': '2'},
        {'a': '3', 'b': '4'},
    ]


def test_summarise_log_file(tmp_path: tempfile.TemporaryDirectory) -> None:
    log_lines = [
        "INFO: Service started",
        "WARNING: Disk space low",
        "ERROR: Connection failed",
        "WARNING: Disk space low",  # duplicate warning
        "",
        "error: unexpected end",  # case-insensitive error
    ]
    log_file = tmp_path / "app.log"
    log_file.write_text("\n".join(log_lines))
    summary = summarise_log_file(str(log_file))
    assert summary['line_count'] == 5  # excludes empty line
    assert summary['error_count'] == 2
    assert sorted(summary['warnings']) == ['Disk space low']