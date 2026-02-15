from datetime import datetime


class Book:
    def __init__(self, id: int, title: str, author: str, pages: int):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("id musbat butun son bolishi kerak")

        if not isinstance(title, str) or not title.strip():
            raise ValueError("title bosh bolmasligi kerak")

        if not isinstance(author, str) or not author.strip():
            raise ValueError("author bosh bolmasligi kerak")

        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("pages 0 dan katta bolishi kerak")

        self.id = id
        self.title = title
        self.author = author
        self.pages = pages

        self.is_borrowed = False
        self.borrower = None
        self.borrow_history = []
        self.archived = False

 
    def borrow(self, user: str) -> None:
        if self.archived:
            raise RuntimeError("Arxivlangan kitobni olish mumkin emas")

        if self.is_borrowed:
            raise RuntimeError("Kitob allaqachon olingan")

        self.is_borrowed = True
        self.borrower = user
        self.borrow_history.append((user, datetime.now()))

    def return_book(self) -> None:
        if not self.is_borrowed:
            raise RuntimeError("Kitob olinmagan")

        self.borrower = None
        self.is_borrowed = False

    def change_title(self, new_title: str) -> None:
        if self.archived:
            raise RuntimeError("Arxivlangan kitob nomini ozgartirib bolmaydi")

        if not isinstance(new_title, str) or not new_title.strip():
            raise ValueError("Yangi nom bosh bolmasligi kerak")

        self.title = new_title

    def archive(self) -> None:
        if self.is_borrowed:
            raise RuntimeError("Olingan kitobni arxivlab bolmaydi")

        self.archived = True

    def info(self) -> dict:
        if self.archived:
            status = "archived"
        elif self.is_borrowed:
            status = "borrowed"
        else:
            status = "available"

        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
            "status": status,
            "borrower": self.borrower,
            "times_borrowed": len(self.borrow_history),
        }


    def __str__(self):
        return f"<Book {self.title}>"

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', borrowed={self.is_borrowed})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.id == other.id

    def __len__(self):
        return self.pages

    def __bool__(self):
        return not self.archived



book = Book(1, "Clean Code", "Robert Martin", 464)

book.borrow("Ali")
print(book.borrower)
print(book.is_borrowed)

book.return_book()
print(book.borrower)

book.change_title("Clean Code 2nd Edition")

info = book.info()
print(info["status"])
print(info["times_borrowed"])

print(book)
print(len(book))
print(bool(book))

book.archive()
print(bool(book))
