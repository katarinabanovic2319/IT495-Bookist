from django.test import TestCase, SimpleTestCase
from django.utils import timezone



class BookAuthorTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        from bookist.books.models import BookAuthor
        BookAuthor.objects.create(author_first_name='Name', author_last_name='Test')

        def test_author_first_name_label(self):
            author = BookAuthor.objects.get(id=1)
            field_label = author._meta.get_field('author_first_name').verbose_name
            self.assertEquals(field_label, 'author_first name')

        def test_date_of_death_label(self):
            author = BookAuthor.objects.get(id=1)
            field_label = author._meta.get_field('author_dod').verbose_name
            self.assertEquals(field_label, 'died')

        def test_author_first_name_max_length(self):
            author = BookAuthor.objects.get(id=1)
            max_length = author._meta.get_field('author_first_name').max_length
            self.assertEquals(max_length, 255)

        def test_get_absolute_url(self):
            author = BookAuthor.objects.get(id=1)
            # This will also fail if the urlconf is not defined.
            self.assertEquals(author.get_absolute_url(), '/books/author/1')
