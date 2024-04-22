import pytest
from main import BooksCollector

@pytest.fixture()
def collector_of_two_books():
    collector = BooksCollector()

    collector.add_new_book('МикроГордость')
    collector.set_book_genre('МикроГордость', 'Комедии')
    collector.add_new_book('АнтиГордость')
    collector.set_book_genre('АнтиГордость', 'Ужасы')

    return collector