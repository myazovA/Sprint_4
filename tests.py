from main import BooksCollector
import pytest

class TestBooksCollector:

    def collector_of_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('МикроГордость')
        collector.set_book_genre('МикроГордость', 'Комедии')
        collector.add_new_book('АнтиГордость')
        collector.set_book_genre('АнтиГордость', 'Ужасы')

        return collector

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books_len_is_2(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_to_horror_genre_is_horror(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', genre)

        assert collector.get_books_genre()['Гордость и предубеждение и зомби'] == genre

    def test_set_book_genre_to_horror_without_book_books_genre_is_empty(self):
        collector = BooksCollector()

        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.get_books_genre() == {}

    def test_get_book_genre_for_fantasy_is_fantasy(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость')
        collector.set_book_genre('Гордость', 'Фантастика')

        assert collector.get_book_genre('Гордость') == 'Фантастика'

    def test_get_books_with_specific_genre_two_books_one_horror_one_not_got_only_horror(self):
        collector = self.collector_of_two_books()

        assert collector.get_books_with_specific_genre('Ужасы') == ['АнтиГордость']

    def test_get_books_genre_add_two_books_print_dict_with_this_books(self):
        collector = self.collector_of_two_books()

        assert collector.get_books_genre() == {'МикроГордость': 'Комедии', 'АнтиГордость': 'Ужасы'}

    def test_get_books_for_children_add_comedy_and_horror_print_comedy(self):
        collector = self.collector_of_two_books()

        assert collector.get_books_for_children() == ['МикроГордость']

    def test_add_book_in_favorites_add_one_book_of_two_print_one_book(self):
        collector = self.collector_of_two_books()

        collector.add_book_in_favorites('АнтиГордость')

        assert collector.favorites == ['АнтиГордость']

    def test_delete_book_from_favorites_one_book_print_empty_list(self):
        collector = self.collector_of_two_books()

        collector.add_book_in_favorites('АнтиГордость')
        collector.delete_book_from_favorites('АнтиГордость')

        assert collector.favorites == []

    def test_get_list_of_favorites_books_add_two_books_print_two_books(self):
        collector = self.collector_of_two_books()

        collector.add_book_in_favorites('АнтиГордость')
        collector.add_book_in_favorites('МикроГордость')

        assert collector.get_list_of_favorites_books() == ['АнтиГордость', 'МикроГордость']
