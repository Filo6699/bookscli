import json
from typing import List, Dict, Self
from uuid import uuid4, UUID


class Book:
    """
    Класс книги.

    Поля:
    - `id` (uuid.UUID):
        UUID книги, генерируется автоматически.
    - `title` (str):
        Название книги.
    - `author` (str):
        Автор книги.
    - `year` (int):
        Год написания книги.
    - `status` (str):
        Статус книги: 'в наличии' или 'выдана'.
    """

    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        id: UUID = None,
        status="в наличии",
    ):
        self._id: UUID = id if id else uuid4()
        self._title: str = title
        self._author: str = author
        self._year: int = year
        self._status: str = status

    @property
    def id(self) -> UUID:
        """Возвращает `id` книги"""
        return self._id

    @property
    def title(self) -> str:
        """Возвращает `title` книги"""
        return self._title

    @property
    def author(self) -> str:
        """Возвращает `author` книги"""
        return self._author

    @property
    def year(self) -> int:
        """Возвращает `year` книги"""
        return self._year

    @property
    def status(self) -> str:
        """Возвращает `status` книги"""
        return self._status

    @status.setter
    def status(self, new_status) -> None:
        """Изменяет статус книги.

        Доступно только два статуса:
        - "в наличии"
        - "выдана"
        """
        if new_status not in ["в наличии", "выдана"]:
            raise ValueError("Incorrect book status")
        self._status = new_status

    @classmethod
    def from_json(cls, obj: Dict) -> Self:
        """Создает экземпляр Book из JSON-словаря."""
        return cls(
            title=obj["title"],
            author=obj["author"],
            year=obj["year"],
            status=obj["status"],
            id=UUID(obj["id"]),
        )

    def to_json(self) -> Dict:
        """Преобразует экземпляр Book в JSON-словарь."""
        return {
            "id": str(self._id),
            "title": self._title,
            "author": self._author,
            "year": self._year,
            "status": self._status,
        }

    def __str__(self) -> str:
        return f"{self._author} - {self._title} ({self._year}) ({self._status}) [{self._id}]"
