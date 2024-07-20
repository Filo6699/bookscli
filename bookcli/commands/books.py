from typing import List

from bookcli.books import Library, Book
from bookcli.commands import Command


def list_books(_: List[str]):
    for book in Library.get_all_books():
        print(book)


COMMANDS: List[Command] = [
    Command("list", list_books, "Shows all of the books in the library"),
]
