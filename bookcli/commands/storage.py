from typing import List

from bookcli.books import Library, Book
from bookcli.command import Command
from bookcli.commands import register_command
from bookcli.utils import Format


@register_command("load", "Load books from a .json file")
def load_books() -> None:
    """Команда для загрузки библиотеки книг из .json файла."""

    books_amount = Library.load_books()

    if books_amount == -1:
        print(f"{Format.RED}{Format.REVERSE} Failed to load books {Format.RESET}")
    else:
        print(
            f"{Format.GREEN}{Format.REVERSE} Books loaded succesfully. ({books_amount} items) {Format.RESET}"
        )


@register_command("save", "Saves books to a .json file")
def save_books() -> None:
    """Команда для сохранения библиотеки книг в .json файл."""

    result = Library.save_books()
    if result == -1:
        print(f"{Format.RED}{Format.REVERSE} Failed to save books {Format.RESET}")
    else:
        print(f"{Format.GREEN}{Format.REVERSE} Saved books succesfully {Format.RESET}")
