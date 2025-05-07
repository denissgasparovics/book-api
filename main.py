from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

books_db = []

@app.get("/")
def index():
    return {"result": "Hello! Welcome to the Book API"}

@app.get("/books", response_model=List[Book])
def get_books():
    return books_db

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book)
def add_book(book: Book):
    books_db.append(book)
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    global books_db
    books_db = [book for book in books_db if book.id != book_id]
    return {"message": "Book deleted successfully"} 