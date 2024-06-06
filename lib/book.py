import sys
import io

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count 

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            raise ValueError("page_count must be an integer")
        self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")  



def test_requires_int_page_count():
    book = Book("And Then There Were None", 272)
    captured_out = io.StringIO()
    sys.stdout = captured_out
    try:
        book.page_count = "not an integer"
    except ValueError as e:
        pass
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "page_count must be an integer\n"

def test_can_turn_page():
    book = Book("The World According to Garp", 69)
    captured_out = io.StringIO()
    sys.stdout = captured_out
    book.turn_page()
    sys.stdout = sys.__stdout__
    assert captured_out.getvalue() == "Flipping the page...wow, you read fast!\n"


test_requires_int_page_count()
test_can_turn_page()
