from typing import List
from uuid import UUID

from bookcli.books import Library, Book
from bookcli.command import Command
from bookcli.utils import Format
from bookcli.commands import register_command


@register_command("list", "Shows all of the books in the library")
def list_books():
    """Команда отображения всех книг."""

    books = Library.get_all_books()
    print(f"{Format.REVERSE} Found {len(books)} books {Format.RESET}")
    for book in books:
        print(book)


@register_command("find", "Find books based on their parameters")
def find_books() -> None:
    """Команда поиска книг в библиотеке по таким параметрам как
    - title
    - author
    - year
    """

    print(f"{Format.REVERSE} Book search {Format.RESET}")
    print("Enter information to filter the books (at least one filter is required)")

    # or None присвоит значение None, если введена пустая строка
    title = input("Title: ").strip() or None
    author = input("Author: ").strip() or None
    year = input("Year: ").strip()

    try:
        year = int(year) if year else None
    except ValueError:
        print(f"{Format.RED}{Format.REVERSE} Error! Not a valid number {Format.RESET}")
        return

    if not any([title, author, year]):
        print(
            f"{Format.RED}{Format.REVERSE} Not enough filters. Must enter at least 1 {Format.RESET}"
        )
        return

    result = Library.find_books(title, author, year)
    print(f"{Format.REVERSE} {len(result)} books found {Format.RESET}")
    for book in result:
        print(book)


@register_command("add", "Add a book to the library")
def add_book() -> None:
    """Команда добавления книги в библиотеку."""

    print(f"{Format.REVERSE} New book {Format.RESET}")
    print("Enter information about the new book. All of the fields are required")

    title = input("Title: ").strip()
    author = input("Author: ").strip()
    year = input("Year: ").strip()

    try:
        year = int(year) if year else None
    except ValueError:
        print(f"{Format.RED}{Format.REVERSE} Error! Not a valid number {Format.RESET}")
        return

    if not all([title, author, year]):
        print(
            f"{Format.RED}{Format.REVERSE} All of the fields are required {Format.RESET}"
        )
        return

    new_book = Book(title, author, year)
    print(new_book)
    Library.add_book(new_book)
    print(f"{Format.GREEN}{Format.REVERSE} Succesfully added a book {Format.RESET}")


@register_command("delete", "Delete a book from the library")
def delete_book() -> None:
    """Команда удаления книги из библиотеки по её ID"""

    print(f"{Format.YELLOW}{Format.REVERSE} Book deletion {Format.RESET}")
    book_id = input("Enter book ID: ").strip()
    try:
        book_id = UUID(book_id)
    except ValueError:
        print(f"{Format.RED}{Format.REVERSE} Incorrect UUID format {Format.RESET}")
        return
    result = Library.delete_book(book_id)
    if result == -1:
        print(f"{Format.YELLOW}{Format.REVERSE} Book doesn't exist {Format.RESET}")
    else:
        print(
            f"{Format.GREEN}{Format.REVERSE} Succesfully deleted a book {Format.RESET}"
        )


@register_command("edit", "Change the status of a book")
def edit_book() -> None:
    """Команда изменения статуса книги по её ID."""

    print(f"{Format.REVERSE} Book edit {Format.RESET}")
    book_id = input("Enter book ID: ").strip()
    try:
        book_id = UUID(book_id)
    except ValueError:
        print(f"{Format.RED}{Format.REVERSE} Incorrect UUID format {Format.RESET}")
        return
    book = Library.get_book(book_id)
    if not book:
        print(f"{Format.YELLOW}{Format.REVERSE} Book doesn't exist {Format.RESET}")
        return
    book.status = input("New status (в наличии/выдана): ").strip()
