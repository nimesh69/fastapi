from fastapi import FastAPI

app= FastAPI()


BOOKS = [
    {'title': 'Title One', 'Author': 'Author One', 'category': 'science'},
    {'title': 'Title two', 'Author': 'Author two', 'category': 'science'},
    {'title': 'Title three', 'Author': 'Author three', 'category': 'history'},
    {'title': 'Title four', 'Author': 'Author four', 'category': 'math'},
    {'title': 'Title five', 'Author': 'Author five', 'category': 'math'},
    {'title': 'Title six', 'Author': 'Author two', 'category': 'math'},
]


@app.get("/books")
async def read_all_books():
    return BOOKS 

@app.get("/books/mybook")
async def read_all_books():
    return {'book_title': 'my favorite book'}


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    # return{'dynamic_param': book_title}


# dynamic should keep below static
# @app.get("/books/mybook")
# async def read_all_books():
#     return {'book_title': 'my favorite book'}