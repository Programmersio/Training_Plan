"""
Library system model classes for training exercises.

This module defines basic classes that model a simple library system.  Use
these classes to practise documentation generation, Mermaid diagram creation,
and prompt engineering.  Some methods are intentionally left unimplemented
so that you can use AI tools to fill them in.

Classes:
    Author – represents an author with a name and biography.
    Book – represents a book with a title, author and ISBN.
    Library – manages a collection of books and provides search functionality.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Author:
    """Represents an author.

    Attributes
    ----------
    name : str
        The full name of the author.
    biography : str
        A short biography of the author.

    """
    name: str
    biography: str


@dataclass
class Book:
    """Represents a book in the library.

    Attributes
    ----------
    title : str
        The title of the book.
    author : Author
        The author of the book.
    isbn : str
        The International Standard Book Number.

    Methods
    -------
    describe() -> str
        Return a string description of the book.
    """
    title: str
    author: Author
    isbn: str

    def describe(self) -> str:
        """Return a human‑readable description of the book.

        Combine the title and the author's name into a single sentence.
        Mention the ISBN number.  For example: ``"1984" by George Orwell (ISBN: 1234567890)``.

        Returns
        -------
        str
            A descriptive string.
        """
        # TODO: implement this method using an AI coding assistant
        raise NotImplementedError


class Library:
    """Manage a collection of books.

    The Library class stores books in an internal catalog keyed by ISBN.  It
    supports adding books, removing books, searching by title or author and
    listing all books.  Use this class to practise writing class methods,
    docstrings, and diagrams.
    """

    def __init__(self) -> None:
        self._catalog: Dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        """Add a book to the library.

        If a book with the same ISBN already exists, overwrite it.  This method
        does not return anything.
        """
        # TODO: implement this method using an AI coding assistant
        raise NotImplementedError

    def remove_book(self, isbn: str) -> Optional[Book]:
        """Remove a book by ISBN and return it.

        If the ISBN is not found, return ``None``.  Otherwise return the
        removed Book object.
        """
        # TODO: implement this method using an AI coding assistant
        raise NotImplementedError

    def search_by_title(self, keyword: str) -> List[Book]:
        """Search for books whose titles contain the given keyword.

        Return a list of books whose titles include ``keyword`` (case-insensitive).
        The order of books in the returned list is not important.
        """
        # TODO: implement this method using an AI coding assistant
        raise NotImplementedError

    def search_by_author(self, author_name: str) -> List[Book]:
        """Search for books written by the specified author.

        Return a list of books whose author's name matches ``author_name``
        (case-insensitive).  Partial matches should be allowed.  If no
        matches are found, return an empty list.
        """
        # TODO: implement this method using an AI coding assistant
        raise NotImplementedError

    def list_books(self) -> List[Book]:
        """Return a list of all books in the library.
        The order of books in the returned list is not important.
        """
        # TODO: implement this method using an AI coding assistant
        raise NotImplementedError