"""
Example 1: Object Initialization and Representation
Demonstrates: __init__, __repr__, __str__, __format__
"""


class Book:
    """A class representing a book with magic methods for representation."""
    
    def __init__(self, title, author, year, pages):
        """Initialize a Book object."""
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
    
    def __repr__(self):
        """Official representation - should be unambiguous and ideally recreate object."""
        return f"Book('{self.title}', '{self.author}', {self.year}, {self.pages})"
    
    def __str__(self):
        """Informal representation - human-readable."""
        return f"'{self.title}' by {self.author} ({self.year})"
    
    def __format__(self, format_spec):
        """Custom formatting support."""
        if format_spec == 'short':
            return f"{self.title} - {self.author}"
        elif format_spec == 'full':
            return f"{self.title} by {self.author}, published in {self.year} ({self.pages} pages)"
        elif format_spec == 'year':
            return str(self.year)
        else:
            return str(self)


# Examples
if __name__ == "__main__":
    book = Book("1984", "George Orwell", 1949, 328)
    
    print("=== Representation Examples ===")
    print(f"repr(book): {repr(book)}")
    print(f"str(book):  {str(book)}")
    print(f"print(book): ", end="")
    print(book)
    
    print("\n=== Format Examples ===")
    print(f"Short format: {book:short}")
    print(f"Full format:  {book:full}")
    print(f"Year only:    {book:year}")
    
    print("\n=== Recreating Object from repr ===")
    book_repr = repr(book)
    print(f"Original repr: {book_repr}")
    recreated_book = eval(book_repr)
    print(f"Recreated:     {recreated_book}")
    print(f"Are they equal strings? {str(book) == str(recreated_book)}")


class Point:
    """A class representing a 2D point."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"


# Example with Point
if __name__ == "__main__":
    print("\n\n=== Point Examples ===")
    p1 = Point(3, 4)
    print(f"Point repr: {repr(p1)}")
    print(f"Point str:  {str(p1)}")
    
    # When used in collections, __repr__ is called
    points = [Point(1, 2), Point(3, 4), Point(5, 6)]
    print(f"List of points: {points}")
