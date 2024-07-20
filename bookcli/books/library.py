import json
from json.decoder import JSONDecodeError
from os import path
from typing import List, Dict, Optional
from uuid import UUID

from bookcli.utils import Format
from .book import Book


class Library:
    """Синглтон класс, библиотека книг."""

    _books: List[Book] = []

    @classmethod
    def load_books(cls, filepath="books.json") -> None:
        """Загружает книги из json файла.

        return value
            Вернёт количество загруженных книг.
            При ошибке вернёт -1 и отобразит ошибку.
        """

        fullpath = path.join(
            path.dirname(__file__),
            "..",
            filepath,
        )

        try:
            with open(fullpath, "r") as fp:
                books_json = json.load(fp)
        except (FileNotFoundError, IsADirectoryError, JSONDecodeError) as err:
            print(f"{Format.RED}Error while trying to load {filepath}")
            print(err, Format.RESET)
            return -1

        cls._books = []

        for book in books_json:
            try:
                loaded_book = Book.from_json(book)
            except KeyError as err:
                print(
                    f"{Format.RED}KeyError while trying to load a book.{Format.RESET}"
                )
                continue
            cls._books.append(loaded_book)
        return len(cls._books)

    @classmethod
    def save_books(cls, filepath="books.json") -> int:
        """Сохраняет книги в json файл.

        return value
            Вернёт количество сохраннёных книг.
            При ошибке вернёт -1 и отобразит ошибку.
        """

        fullpath = path.join(
            path.dirname(__file__),
            "..",
            filepath,
        )

        try:
            with open(fullpath, "w") as fp:
                json_books = [bk.to_json() for bk in cls._books]
                json.dump(json_books, fp)
        except (FileNotFoundError, IsADirectoryError) as err:
            print(f"{Format.RED}Error while trying to load {filepath}")
            print(err, Format.RESET)
            return -1
        return len(cls._books)

    @classmethod
    def get_all_books(cls) -> List[Book]:
        """Возвращает список из всех книг библиотеки."""
        return cls._books

    @classmethod
    def get_book(cls, book_id: UUID) -> Optional[Book]:
        """Возвращает книгу с совпадающим book_id, если она есть, иначе вернёт None."""
        for book in cls._books:
            if book.id == book_id:
                return book
        return None

    # @classmethod
    # def edit_book_status(cls, book: Book, new_status)

    @classmethod
    def add_book(cls, book: Book) -> None:
        """Добавляет новую книгу в библиотеку."""
        cls._books.append(book)

    @classmethod
    def delete_book(cls, book_id: UUID) -> int:
        """Удаляет книгу из библиотеки.

        return value
            Вернёт 0 при успешном удалении
            Вернёт -1, если книга не найдена
        """
        try:
            book = cls.get_book(book_id)
            if not book:
                return -1
            cls._books.remove(book)
            return 0
        except ValueError:  # Книга не найдена
            return -1

    @classmethod
    def find_books(
        cls,
        title: Optional[str] = None,
        author: Optional[str] = None,
        year: Optional[int] = None,
    ) -> List[Book]:
        """Ищет книгу в библиотеке по фильтрам.

        Фильтры
        - `title` (str | None):
            Включить в ответ книги только с этим названием
        - `author` (str | None):
            Включить в ответ книги только от этого автора
        - `year` (int | None):
            Включить в ответ книги только с этим годом написания
        """

        books: List[Book] = cls._books.copy()
        if title:
            # Генератор возвращает только те книги, где совпадает название с `title`
            books = [book for book in books if book.title == title]
        if author:
            books = [book for book in books if book.author == author]
        if year:
            books = [book for book in books if book.year == year]

        return books
