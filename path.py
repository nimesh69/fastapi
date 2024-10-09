from fastapi import Body, FastAPI

app= FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title two', 'author': 'Author two', 'category': 'science'},
    {'title': 'Title three', 'author': 'Author three', 'category': 'history'},
    {'title': 'Title four', 'author': 'Author four', 'category': 'math'},
    {'title': 'Title five', 'author': 'Author five', 'category': 'math'},
    {'title': 'Title six', 'author': 'Author two', 'category': 'math'},
]


@app.get("/books")
async def read_all_books():
    return BOOKS 

@app.get("/books/mybook")
async def read_all_books():
    return {'book_title': 'my favorite book'}


# @app.get("/books/{book_title}")
# async def read_book(book_title: str):
#     for book in BOOKS:
#         if book.get('title').casefold() == book_title.casefold():
#             return book
    # return{'dynamic_param': book_title}


# dynamic should keep below static
# @app.get("/books/mybook")
# async def read_all_books():
#     return {'book_title': 'my favorite book'}

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range (len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            # return BOOKS[i]



@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range (len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            # BOOKS.pop(i) can be used pop also
            del BOOKS[i]
            return {"message": f"Book '{book_title}' deleted successfully"}
            break


@app.get("/books/{author_title}")
async def get_author_book(author_title: str):
    books = []
    for i in range (len(BOOKS)):
        if BOOKS[i].get('author').casefold() == author_title.casefold():
            books.append(BOOKS[i].get('category'))
    # for book in BOOKS:
    #     if book.get('author').casefold() == author_title.casefold():
    #         books.append(book.get('category'))
    return books