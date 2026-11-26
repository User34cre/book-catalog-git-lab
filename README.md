# book-catalog-git-lab

# Каталог книг (Book Catalog)

Учебный проект на Python для отработки контроля версий Git и рабочего процесса в GitHub (ветки, Issues, Pull Requests, Code Review и выпуск версии v0.1.0).

## Цель проекта
Освоить управление версиями, декомпозицию задач, оценку трудоёмкости по методу PERT и работу через Pull Request.

## Основные функции
- Добавление книги в каталог с проверкой входных данных.
- Просмотр списка книг каталога.

## Технологии и инструменты
- Python 3
- Git, GitHub, Visual Studio Code

## Запуск
```bash
python -c "from src.catalog import BookCatalog; c = BookCatalog(); c.add_book('Алиса в Стране чудес', 'Льюис Кэрролл', 1865); print(c.list_books())"