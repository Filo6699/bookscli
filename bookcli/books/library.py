import json
from json.decoder import JSONDecodeError
from os import path
from typing import List, Dict

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
        return len(cls.books)

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

    # @classmethod
    # def add_book(cls, book: Book) -> int:
    #     """Добавляет новую книгу в библиотеку.

    #     return value
    #         Вернёт 0 при успехе
    #         Вернёт -1 при ошибке
    #     """
    #     ...
