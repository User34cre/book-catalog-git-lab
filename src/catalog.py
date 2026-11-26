"""Модуль каталога книг."""

from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    """Модель книги в каталоге."""

    title: str
    author: str
    year: int



class BookCatalog:
    """Класс для управления каталогом книг."""

    def __init__(self) -> None:
        """Инициализирует пустой список книг."""
        self._books: List[Book] = []

    def add_book(self,title: str, author: str, year: int) -> Book:
        """Добавляет книгу в каталог после проверки входных данных.

        Args:
            title: Название книги.
            author: Автор книги.
            year: Год издания.

        Returns:
            Добавленный объект книги.

        Raises:
            ValueError: Если название или автор пустые либо год некорректен.
        """
        clean_title = title.strip()
        clean_author = author.strip()
        if not clean_title or not clean_author:
            raise ValueError("Название и автор книги не должны быть пустыми.")
        if year < 1450 or year > 2026:
            raise ValueError("Указан некорректный год издания.")

        book = Book(title=clean_title, author=clean_author, year=year)
        self._books.append(book)
        return book

    def list_books(self) -> List[Book]:
    """Возвращает список всех книг в каталоге.

    Returns:
        Копия списка книг каталога.
    """
    return list(self._books)