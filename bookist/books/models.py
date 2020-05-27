from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class BookAuthor(models.Model):
    author_first_name = models.CharField(max_length=255, help_text="Enter authors first name")
    author_last_name = models.CharField(max_length=255)
    author_dob = models.DateField(auto_now=False, null=True)
    author_dod = models.DateField(auto_now=False, null=True)
    author_bio = models.TextField(max_length=255)
    author_nationality = models.CharField(max_length=255)

    def __str__(self):
        return '%s %s'%(self.author_first_name, self.author_last_name)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class BookGenre(models.Model):
    genre_name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        return self.genre_name


class Book(models.Model):
    book_title = models.CharField(max_length=255, help_text="Enter book title")
    book_author = models.ForeignKey(BookAuthor, on_delete=models.SET_NULL, null=True)
    book_isbn = models.BigIntegerField(blank=True, null=True)
    book_year = models.IntegerField(blank=True, null=True)
    book_genre = models.ManyToManyField(BookGenre, help_text='Select a genre for this book')
    book_description = models.TextField(max_length=255)
    book_image = models.ImageField(upload_to='book_image', blank=True)
    book_ratings = models.ManyToManyField(get_user_model(), through='BookReview')

    def __str__(self):
        return self.book_title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookComment(models.Model):
    comment_text = models.TextField(max_length=1000, help_text="Enter your comment here")
    comment_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment_post_date = models.DateTimeField(auto_now_add=True)
    comment_book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        ordering = ["comment_post_date"]

    def __str__(self):
        len_title = 75
        if len(self.comment_text) > len_title:
            titlestring = self.comment_text[:len_title] + '...'
        else:
            titlestring = self.comment_text
        return titlestring


class BookList(models.Model):
    list_title = models.CharField(max_length=255)
    list_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    list_description = models.TextField(max_length=255)
    list_books = models.ManyToManyField(Book)

    def __str__(self):
        return self.list_title

    def get_absolute_url(self):
        return reverse('list-detail', args=[str(self.id)])


class BookReview(models.Model):
    review_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    review_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_score = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.review_score)


class Friend(models.Model):
    users = models.ManyToManyField(get_user_model())
    current_user = models.ForeignKey(get_user_model(), related_name='owner', on_delete=models.CASCADE, null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)