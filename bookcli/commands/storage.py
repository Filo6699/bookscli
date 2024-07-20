from typing import List

from bookcli.books import Library, Book
from bookcli.commands import Command


def load_books(_: List[str]) -> None:
    books_amount = Library.load_books()

    if books_amount == -1:
        print("Failed to load books.")
    else:
        print(f"Books loaded succesfully. ({books_amount} items)")


def save_books(_: List[str]) -> None:
    result = Library.save_books()
    if result == -1:
        print("Failed to save books.")
    else:
        print("Saved books succesfully.")


COMMANDS: List[Command] = [
    Command("load", load_books, "Load books from a .json file"),
    Command("save", save_books, "Saves books to a .json file"),
]
