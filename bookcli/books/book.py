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
        self.id: UUID = id if id else uuid4()
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status

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
            "id": str(self.id),
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    def __str__(self) -> str:
        return json.dumps(self.to_json(), indent=2)
