from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/books", tags=["books"])

class Book(BaseModel):
    """Модель книги"""
    id: int
    title: str
    author: str
    year: int

books_db = [
    Book(id=1, title="Мастер и Маргарита", author="М. Булгаков", year=1967),
    Book(id=2, title="Преступление и наказание", author="Ф. Достоевский", year=1866),
]

@router.get("/", response_model=List[Book])
async def get_books():
    """Получение списка всех книг"""
    return books_db

@router.get("/{book_id}", response_model=Book)
async def get_book(book_id: int):
    """Получение книги"""
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

@router.post("/", response_model=Book)
async def create_book(book: Book):
    """Создание книги"""
    books_db.append(book)
    return book
