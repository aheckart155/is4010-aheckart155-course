class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_age(self):
        return 2025 - self.year

    def __str__(self):
        return f"\"{self.title}\" by {self.author} ({self.year})"


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} ({self.file_size} MB)"


if __name__ == '__main__':
    my_book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    print("Book details:", my_book)
    print("Book age:", my_book.get_age())

    my_ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    print("EBook details:", my_ebook)
    print("EBook age:", my_ebook.get_age())