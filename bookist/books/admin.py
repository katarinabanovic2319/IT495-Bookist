from django.contrib import admin

from .models import Book, BookAuthor, BookComment, BookGenre, BookList, BookReview, Friend

admin.site.site_header = 'Administration'

class CommentInlineAdmin(admin.TabularInline):
    model = BookComment
    extra = 0

class ReviewInlineAdmin(admin.TabularInline):
    model = BookReview
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =('book_title', 'book_author')
    inlines = [CommentInlineAdmin, ReviewInlineAdmin]

@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display =('author_first_name', 'author_last_name')

@admin.register(BookComment)
class BookCommentAdmin(admin.ModelAdmin):
    list_display = ('comment_author', 'comment_post_date', 'comment_book')

@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ['genre_name']

@admin.register(BookList)
class BookListAdmin(admin.ModelAdmin):
    list_display = ['list_title', 'list_author']
    filter_horizontal = ('list_books',)

@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['review_user', 'review_book', 'review_score']

admin.site.register(Friend)