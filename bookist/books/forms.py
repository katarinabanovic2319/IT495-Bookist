from django import forms

from .models import Book, BookAuthor, BookList


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['book_title', 'book_author', 'book_year', 'book_isbn', 'book_genre', 'book_description', 'book_image']


class BookAuthorForm(forms.ModelForm):

    class Meta:
        model = BookAuthor
        fields = '__all__'


class ListForm(forms.ModelForm):

    class Meta:
        model = BookList
        fields = ['list_title', 'list_description', 'list_books']
